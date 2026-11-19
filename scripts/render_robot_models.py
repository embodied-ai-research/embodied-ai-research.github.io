from pathlib import Path
import mujoco as m
import numpy as np
from PIL import Image
import argparse
parser=argparse.ArgumentParser(description='Render transparent robot assets with MuJoCo 3.2.7 and Pillow.')
parser.add_argument('model_root',type=Path,help='Directory with franka_fr3/, bitcraze_crazyflie_2/, openarm/ and sharpa/ source repositories')
root=parser.parse_args().model_root
repo=Path(__file__).resolve().parents[1]
out=repo/'assets/media/robots';out.mkdir(parents=True,exist_ok=True)
items=[
 ('fr3',root/'franka_fr3/fr3.xml',[.3,0,.42],2.0,135,-20),
 ('crazyflie',root/'bitcraze_crazyflie_2/cf2.xml',[0,0,.1],.3,135,-30),
 ('openarm',root/'openarm/v1/openarm_bimanual.xml',[0,0,.45],1.6,160,-15),
 ('sharpa',root/'sharpa/wave_01/right_sharpa_wave/right_sharpa_wave.xml',[0,0,.1],.48,20,-15),
 ('mobile',repo/'scripts/models/mobile.xml',[0,0,.15],1.4,125,-25),
]
for name,p,look,dist,az,el in items:
 try:
  model=m.MjModel.from_xml_path(str(p)); data=m.MjData(model)
  if model.nkey:m.mj_resetDataKeyframe(model,data,0)
  if name=='openarm':
   for i in range(model.njnt):
    n=m.mj_id2name(model,m.mjtObj.mjOBJ_JOINT,i);a=model.jnt_qposadr[i]
    if n and n.endswith('joint4'):data.qpos[a]=1.4
    if n and n.endswith('joint2') and 'finger' not in n:data.qpos[a]=-.3 if 'left' in n else .3
  if name=='sharpa':model.geom_rgba[:,:3]=np.mean(model.geom_rgba[:,:3],axis=1)[:,None]
  m.mj_forward(model,data)
  model.vis.global_.offwidth=1200;model.vis.global_.offheight=1200
  model.vis.headlight.diffuse[:]=.65;model.vis.headlight.ambient[:]=.4;model.vis.headlight.specular[:]=.12
  cam=m.MjvCamera();cam.lookat[:]=look;cam.distance=dist;cam.azimuth=az;cam.elevation=el
  opt=m.MjvOption();opt.geomgroup[3]=0;opt.sitegroup[:]=0
  with m.Renderer(model,height=1200,width=1200) as r:
   r.update_scene(data,camera=cam,scene_option=opt);rgb=r.render().copy()
   r.enable_segmentation_rendering();r.update_scene(data,camera=cam,scene_option=opt);seg=r.render().copy()
  alpha=np.where(seg[:,:,1]==int(m.mjtObj.mjOBJ_GEOM),255,0).astype(np.uint8)
  im=Image.fromarray(np.dstack((rgb,alpha)));box=im.getbbox()
  assert box and box[0]>0 and box[1]>0 and box[2]<1200 and box[3]<1200, 'Camera clips the model'
  im.crop(box).save(out/(name+'.png'))
  print(name,box,model.nq,flush=True)
 except Exception as e:raise RuntimeError(f'Failed to render {name}') from e
