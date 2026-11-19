"""Mount the public Franka Hand visual mesh at FR3's attachment site.
Visual-only assembly, with a fixed 56 mm jaw opening; not a dynamics model.
"""
from pathlib import Path
from copy import deepcopy
import xml.etree.ElementTree as ET

def fr3_with_hand(fr3_path, hand_dir):
    fr3_path, hand_dir = Path(fr3_path), Path(hand_dir)
    robot = ET.parse(fr3_path).getroot()
    hand = ET.parse(hand_dir / 'hand.xml').getroot()
    robot.find('compiler').set('meshdir', str(fr3_path.parent / 'assets'))
    assets = robot.find('asset')
    for item in hand.find('asset'):
        if item.tag not in ('mesh', 'material'):
            continue
        item = deepcopy(item)
        name = item.get('name') or Path(item.get('file')).stem
        item.set('name', 'gripper_' + name)
        item.attrib.pop('class', None)
        if item.tag == 'mesh':
            item.set('file', str(hand_dir / 'assets' / item.get('file')))
        assets.append(item)
    def visual_body(source):
        node = ET.Element('body', {k: v for k, v in source.attrib.items() if k in ('pos','quat')})
        for child in source:
            if child.tag == 'geom' and child.get('class') == 'visual':
                geom = deepcopy(child)
                geom.attrib.pop('class', None)
                geom.set('type', 'mesh'); geom.set('group', '2')
                geom.set('contype', '0'); geom.set('conaffinity', '0')
                geom.set('mesh', 'gripper_' + geom.get('mesh'))
                geom.set('material', 'gripper_' + geom.get('material'))
                node.append(geom)
            elif child.tag == 'body':
                finger = visual_body(child)
                finger.set('pos', '0 {} 0.0584'.format(0.028 if child.get('name') == 'left_finger' else -0.028))
                node.append(finger)
        return node
    body = visual_body(hand.find('./worldbody/body'))
    body.set('name', 'franka_hand_visual')
    body.set('pos', robot.find(".//site[@name='attachment_site']").get('pos'))
    body.set('quat', '0.923879533 0 0 -0.382683432')
    robot.find(".//body[@name='fr3_link7']").append(body)
    return ET.tostring(robot, encoding='unicode')
