"""Author the site's bilingual method diagrams. No photo/video or measured-result plots.
Robot PNGs are transparent mesh renders; see assets/media/robots/SOURCES.md.
Run with Python 3 from the repository root. SVG is the editable, deployed source.
"""
from pathlib import Path
from html import escape
import base64, math, json
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'assets/media/teasers';OUT.mkdir(exist_ok=True)
C={'ink':'#22343e','muted':'#667981','line':'#bfced2','teal':'#287a80','blue':'#527691','amber':'#ac7840','red':'#b26961','bg':'#f5f8f9','soft':'#e6f0f0','white':'#ffffff'}
class Diagram:
 def __init__(self,title,sub,lang):
  self.lang=lang;self.parts=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="960" viewBox="0 0 1440 960" role="img"><title>{escape(title)} — {escape(self.tr(sub))}</title><defs><marker id="arr" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L8 4L0 8" fill="none" stroke="{C['teal']}" stroke-width="2"/></marker><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#dce5e7" stroke-width="1"/></pattern></defs><rect width="1440" height="960" rx="28" fill="{C['bg']}"/><g font-family="-apple-system,BlinkMacSystemFont,Helvetica Neue,Arial,PingFang SC,Hiragino Sans GB,sans-serif">''']
  self.text(38,54,title,38,weight=700);self.text(1402,51,self.tr(sub),26,color='muted',anchor='end')
  self.path('M38 82H1402',color='line',width=2)
 def tr(self,v):return v[self.lang=='zh'] if isinstance(v,(tuple,list)) else v
 def add(self,s):self.parts.append(s)
 def rect(self,x,y,w,h,fill='white',stroke=None,r=16):self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{C.get(fill,fill)}"'+(f' stroke="{C.get(stroke,stroke)}" stroke-width="2"' if stroke else '')+'/>')
 def text(self,x,y,t,size=30,color='ink',weight=500,anchor='start'):
  for i,line in enumerate(self.tr(t).split('\n')):self.add(f'<text x="{x}" y="{y+i*size*1.24}" font-size="{size}" font-weight="{weight}" fill="{C.get(color,color)}" text-anchor="{anchor}">{escape(line)}</text>')
 def path(self,d,color='teal',width=3,fill='none',dash=False,arrow=False):self.add(f'<path d="{d}" fill="{C.get(fill,fill)}" stroke="{C.get(color,color)}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"'+(' stroke-dasharray="8 7"' if dash else '')+(' marker-end="url(#arr)"' if arrow else '')+'/>')
 def circle(self,x,y,r,fill='soft',stroke=None):self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C.get(fill,fill)}"'+(f' stroke="{C.get(stroke,stroke)}" stroke-width="2"' if stroke else '')+'/>')
 def panel(self,x,y,w,h,label,num=None):
  self.rect(x,y,w,h,stroke='line');self.text(x+20,y+37,(str(num)+'  ' if num else '')+self.tr(label),28,'muted',600)
 def node(self,x,y,w,h,title,detail=None,color='soft'):
  self.rect(x,y,w,h,color,'line',12);self.text(x+w/2,y+(h/2+10 if not detail else 40),title,30,weight=600,anchor='middle')
  if detail:self.text(x+w/2,y+78,detail,24,'muted',anchor='middle')
 def image(self,name,x,y,w,h):
  raw=base64.b64encode((ROOT/f'assets/media/robots/{name}.png').read_bytes()).decode();self.add(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/png;base64,{raw}" preserveAspectRatio="xMidYMid meet"/>')
 def arrow(self,x1,y1,x2,y2,dash=False):self.path(f'M{x1} {y1}L{x2} {y2}',arrow=True,dash=dash)
 def pill(self,x,y,w,t,color='soft'):self.rect(x,y,w,42,color,r=9);self.text(x+w/2,y+29,t,24,anchor='middle')
 def footer(self,title,detail):
  self.rect(38,864,1364,66,'soft',r=12);self.text(60,906,title,29,'teal',650);self.text(1380,905,detail,25,'muted',anchor='end')
 def tokens(self,x,y,n=7,cols=1):
  for j in range(cols):
   for i in range(n):self.rect(x+i*25,y+j*26,18,18,['#79a9ad','#b0c4ce','#d6ded7'][j%3],r=4)
 def camera(self,x,y,s=1):
  self.add(f'<g transform="translate({x} {y}) scale({s})">');self.rect(0,8,64,44,'soft','teal',8);self.circle(30,30,13,'white','teal');self.path('M64 22L82 12V48L64 39Z',fill='soft');self.add('</g>')
 def person(self,x,y,s=1):
  self.add(f'<g transform="translate({x} {y}) scale({s})">');self.circle(0,0,15,'blue');self.path('M0 22V67M-30 42L0 25L30 42M0 65L-23 103M0 65L23 103','blue',10);self.add('</g>')
 def cube(self,x,y,s=1):
  self.add(f'<g transform="translate({x} {y}) scale({s})">');self.path('M0 22L39 0L78 22L39 44Z',fill='#d3e3e4');self.path('M0 22V67L39 90V44Z',fill='#b0cdce');self.path('M39 44L78 22V67L39 90Z',fill='#e1eded');self.add('</g>')
 def map(self,x,y,w,h,phase=0):
  self.rect(x,y,w,h,'#edf3f2',r=8)
  for j in range(8):
   for i in range(12):
    v=math.exp(-((i-3-phase*.5)**2+(j-3)**2)/5)+math.exp(-((i-9)**2+(j-5+phase*.5)**2)/4)
    color='#507d89' if v>.72 else '#9abdc0' if v>.3 else '#d5e5e3' if v>.1 else '#edf3f2'
    self.rect(x+i*w/12+1,y+j*h/8+1,w/12-2,h/8-2,color,r=2)
  self.path(f'M{x+10} {y+h-15} C{x+w*.45} {y+h-10} {x+w*.4} {y+10} {x+w-12} {y+18}',width=4,arrow=True)
 def gp(self,x,y,w,h):
  self.path(f'M{x} {y}V{y+h}H{x+w}','line',2)
  def f(t):return .52+.22*math.sin(t*6)-.10*math.cos(t*11)
  top=[];bot=[];mid=[]
  for i in range(61):
   t=i/60;v=f(t);spread=.11+.06*math.cos(t*10);xx=x+t*w
   top.append((xx,y+h*(v-spread)));bot.append((xx,y+h*(v+spread)));mid.append((xx,y+h*v))
  fmt=lambda ps:' '.join(f'{a:.1f},{b:.1f}' for a,b in ps)
  self.add(f'<polygon points="{fmt(top+bot[::-1])}" fill="#d4e7e7"/>');self.path('M'+'L'.join(f'{a:.1f} {b:.1f}' for a,b in mid),width=4)
  for i in range(9):
   t=(i+.35)/9;self.circle(x+t*w,y+h*(f(t)+.05*math.sin(i*11)),5,'blue')
 def finish(self,pid):
  self.add('</g></svg>');(OUT/f'{pid}-{self.lang}.svg').write_text(''.join(self.parts))

def shape(lang):
 d=Diagram('SHAPE',('Human data → dexterous actions','人类数据 → 灵巧操作'),lang)
 d.panel(38,108,464,728,('Cross-embodiment data','跨本体数据'),1)
 d.person(118,190,.65);d.camera(205,173,.8);d.path('M310 185C352 125 410 250 458 185',width=4);d.text(70,277,('Egocentric human video','第一视角人类视频'),28,weight=650)
 d.pill(66,297,207,('Wrist pose','手腕位姿'));d.pill(285,297,190,('Fingertips','指尖轨迹'))
 d.path('M64 355H476','line',2);d.image('shape-platform',64,368,412,384)
 d.text(270,776,('Robot demonstrations','机器人遥操作数据'),28,weight=650,anchor='middle');d.text(270,813,('EEF + joint targets','末端 + 关节动作标签'),24,'muted',anchor='middle')
 d.panel(532,108,870,728,('Shared representations, parallel actions','共享表征，并行动作'),2)
 d.node(568,171,798,112,('Vision–language backbone','视觉语言主干'),('Images · language · robot state','图像 · 语言 · 机器人状态'))
 d.arrow(502,254,563,226)
 d.node(1010,324,356,113,('Discrete FAST tokens','离散 FAST 动作词元'),('Auxiliary supervision only','仅用于辅助监督'),'#f3e9db');d.arrow(1188,283,1188,319,True)
 d.rect(568,331,392,451,'#e6f0f0','line',16);d.text(764,374,('Shared flow expert','共享流匹配专家'),32,weight=650,anchor='middle');d.text(764,413,('Independent streams','相互独立的动作流'),24,'muted',anchor='middle')
 d.tokens(606,452,12);d.node(602,512,324,86,('EEF stream','末端动作流'),color='white');d.node(602,658,324,86,('Joint stream','关节动作流'),color='white')
 d.arrow(764,283,764,326);d.node(1010,510,356,90,('IK → execution','逆运动学 → 执行'),color='white');d.node(1010,656,356,90,('Direct execution','直接执行'),color='white');d.arrow(960,555,1005,555);d.arrow(960,701,1005,701)
 d.text(1188,635,('Human-to-robot transfer','人类到机器人的迁移'),25,'teal',anchor='middle');d.text(1188,781,('Robot-demo precision','机器人示范的执行精度'),25,'teal',anchor='middle')
 d.footer(('One policy, two executable readouts','一个策略，两种可执行输出'),('Discrete supervision + continuous flow','离散监督 + 连续流匹配'));d.finish('li2026shape')

def ct(lang):
 d=Diagram('CT-VAM',('Efficient visuomotor control','高效视觉运动控制'),lang)
 d.panel(38,108,464,728,('Perception & execution','感知与执行'),1)
 d.camera(70,169,.75);d.camera(336,169,.75);d.text(270,257,('Two camera views','双视角视觉输入'),28,anchor='middle');d.image('openarm',65,280,410,395)
 d.cube(362,588,.75);d.path('M365 547C458 494 478 621 427 661',dash=True,arrow=True)
 d.pill(80,693,380,('OpenArm · joint-space control','OpenArm · 关节空间控制'));d.text(270,777,('Vision + proprioception','视觉 + 本体感知'),28,weight=650,anchor='middle');d.text(270,813,('On-device deployment','机载推理部署'),24,'muted',anchor='middle')
 d.panel(532,108,870,728,('Action-centric routing','以动作为中心的路由'),2)
 d.node(568,173,456,104,'DINOv3',('Cross-view visual features','跨视角视觉特征'));d.node(1052,173,314,104,('Task + state','任务 + 状态'));d.arrow(502,210,563,210)
 d.rect(568,322,798,289,'soft','line');d.text(596,366,'TARS',32,weight=700);d.text(1338,366,('Independent attention · gated sum','独立注意力 · 门控聚合'),26,'muted',anchor='end')
 labels=[('Action tokens','动作词元'),('Action queries','动作查询'),('Visual–proprio memory','视觉—本体记忆'),('Task tokens','任务词元')]
 for i,v in enumerate(labels):
  yy=394+i*51;d.text(596,yy+27,v,25);d.tokens(936,yy+5,5);d.arrow(1070,yy+14,1141,yy+14)
 d.node(1148,401,190,185,('Gated\nsum','门控\n聚合'),color='white');d.arrow(796,277,796,317);d.arrow(1208,277,1208,317)
 d.node(568,666,368,116,('Rectified flow','整流流模型'),('Action chunk generation','动作序列生成'));d.node(980,666,386,116,('Flow inpainting','流一致性补全'),('Smooth chunk transitions','平滑衔接动作序列'));d.arrow(758,611,758,661);d.arrow(936,724,975,724)
 d.path('M1173 782V815H520V584H480',arrow=True);d.footer(('Route information around action','围绕动作组织信息'),('Visual memory → action chunks → control','视觉记忆 → 动作序列 → 控制'));d.finish('li2026ctvam')

def ncub(lang):
 d=Diagram('NCUB',('Reliable probabilistic robustness','可靠的概率鲁棒性'),lang)
 d.panel(38,108,464,728,('Constrained motion control','约束运动控制'),1);d.image('fr3',76,197,362,435)
 d.circle(399,408,43,'#dce9e6','teal');d.path('M399 451Q417 478 399 518','muted',2)
 d.pill(84,659,368,'Franka Research 3');d.text(74,751,('Contact / balloon','接触 / 气球任务'),26,weight=650);d.text(74,802,('Trajectory / writing','轨迹 / 书写任务'),26,weight=650)
 d.path('M381 746l30 -44l12 8l-30 44l-20 10Z',fill='soft');d.path('M373 798q15 -22 29 -1q10 -25 28 -1',width=3)
 d.panel(532,108,870,728,('Learning → bounds → feedback','学习 → 误差界 → 闭环'),2)
 d.rect(568,173,380,221,'white','line');d.text(594,213,('Gaussian process','高斯过程'),29,weight=650);d.gp(594,239,325,124)
 d.node(1000,173,366,105,('RWD fitting','RWD 分布拟合'),('Lipschitz estimates','Lipschitz 常数估计'));d.node(1000,301,366,105,('Parameter selection','参数选择'),('Sample-dependent calibration','依样本数量进行校准'))
 d.node(568,466,798,112,('Nonconservative uncertainty bound','非保守不确定性界'),('GP posterior + fitted smoothness bounds','GP 后验 + 拟合的平滑性界'))
 d.arrow(948,235,995,235);d.path('M1366 226H1383V439H985V461',arrow=True);d.arrow(758,394,758,461);d.arrow(1183,406,1183,461)
 d.node(568,658,355,105,('Robust constraints','鲁棒约束'),('GP-based controller','基于 GP 的控制器'));d.node(1000,658,366,105,('System / robot','系统 / 机器人'),('State & observations','状态与观测'),color='white');d.arrow(746,578,746,653);d.arrow(923,709,995,709);d.path('M1183 763V808H550V256H563',arrow=True)
 d.footer(('Calibrate uncertainty for control','面向控制校准不确定性'),('Data-driven calibration in a feedback loop','数据驱动的界校准与闭环控制'));d.finish('li2026gpbound')

def dg(lang):
 d=Diagram('DG-ACMP',('Plan with acceptable contacts','利用可接受接触规划'),lang)
 d.panel(38,108,464,728,('Cluttered, deformable scene','拥挤可变形环境'),1)
 d.rect(66,187,407,447,'url(#grid)',r=10)
 for x,y,w,h in [(70,382,57,170),(397,267,65,256),(258,503,64,113)]:d.rect(x,y,w,h,'#bcd1d1','teal',28)
 d.image('fr3',120,201,299,370);d.path('M399 332C347 340 435 419 345 509C310 533 319 559 320 588',width=5,dash=True,arrow=True)
 d.circle(354,470,24,'#f0dfc9','amber');d.arrow(354,470,395,455);d.text(343,440,('Force','接触力'),25,'amber')
 d.pill(84,659,368,'Franka Research 3');d.text(270,757,('Contact-aware trajectories','接触感知轨迹'),28,weight=650,anchor='middle');d.text(270,801,('Deform rather than avoid everything','允许形变，释放可行空间'),25,'muted',anchor='middle')
 d.panel(532,108,870,728,('Geometry → force → planning','几何 → 力 → 规划'),2)
 d.rect(568,174,798,183,'white','line');d.text(594,214,('Sphere tree + Laplacian deformation','球树 + 拉普拉斯形变'),29,weight=650)
 for offset,shift in [(618,0),(872,21)]:
  for r in range(3):
   for c in range(4):
    xx=offset+c*43+shift*math.sin(r);yy=251+r*31;d.circle(xx,yy,10,'soft','teal')
    if c<3:d.path(f'M{xx+10} {yy}h23','line',2)
    if r<2:d.path(f'M{xx} {yy+10}l{shift*(math.sin(r+1)-math.sin(r))} 11','line',2)
 d.arrow(790,283,837,283);d.text(1125,279,('Local\nshape change','局部\n几何形变'),25,'muted')
 d.node(568,413,364,113,('Strain estimation','应变估计'),('Two-stage approximation','两阶段近似'));d.node(992,413,374,113,('Kelvin–Voigt model','Kelvin–Voigt 模型'),('Elasticity + damping','弹性 + 阻尼'));d.arrow(756,357,756,408);d.arrow(932,469,987,469)
 d.rect(568,594,798,197,'soft','line');d.text(596,640,('Trajectory optimization','轨迹优化'),32,weight=650);d.pill(594,662,308,('GP motion prior','GP 运动先验'),'white');d.pill(942,662,394,('Contact-force factors','接触力因子'),'white');d.text(967,756,('Nonlinear least squares · LM','非线性最小二乘 · LM'),28,'teal',anchor='middle');d.arrow(1179,526,1179,589)
 d.path('M568 742H521V565H476',arrow=True);d.footer(('Model deformation before optimizing motion','先建模形变，再优化运动'),('Geometry + mechanics + trajectory factors','几何 + 力学 + 轨迹因子'));d.finish('guo2026dgacmp')

def stgp(lang):
 d=Diagram('BU-STGP',('Consistent maps, consistent motion','地图一致，运动连贯'),lang)
 d.panel(38,108,464,728,('Navigation in dynamic scenes','动态场景导航'),1)
 d.map(65,183,410,367);d.person(383,291,.67);d.person(169,224,.57);d.image('mobile',98,422,320,234);d.pill(69,671,403,('Four-wheel research platform','自建四轮研究平台'))
 d.text(270,758,('LiDAR + observation history','激光雷达 + 历史观测'),28,weight=650,anchor='middle');d.text(270,801,('Robot model: schematic','按平台结构绘制示意模型'),24,'muted',anchor='middle')
 d.panel(532,108,870,728,('Online spatio-temporal fusion','在线时空融合'),2)
 for i in range(3):
  d.map(568+i*273,178,250,124,i);d.text(693+i*273,336,['t − 2','t − 1','t'][i],25,'muted',anchor='middle')
 d.node(568,390,375,110,('Spatial GP','空间高斯过程'),('Points → signed distances','点云 → 有符号距离'));d.node(991,390,375,110,('Temporal GP','时间高斯过程'),('Historical GP estimates','历史 GP 估计'))
 d.arrow(750,343,750,385);d.arrow(1178,343,1178,385);d.node(568,558,798,107,('One-step Bayesian update','单步贝叶斯更新'),('Fuse current geometry and temporal evidence','融合当前几何与时序证据'));d.arrow(750,500,750,553);d.arrow(1178,500,1178,553)
 d.node(568,723,360,76,('Consistent SDF','一致的距离场'));d.node(1007,723,359,76,('Motion replanning','运动重规划'));d.arrow(747,665,747,718);d.arrow(928,761,1002,761)
 d.footer(('Preserve temporal structure while mapping','建图时保留时间结构'),('Spatial inference + temporal prediction','空间推断 + 时间预测'));d.finish('jiang2026stgp')

def gd(lang):
 d=Diagram('GD-CBF',('Safety at arbitrary relative degree','任意相对阶的安全控制'),lang)
 d.panel(38,108,464,728,('Attitude-constrained system','姿态受约束系统'),1)
 d.add('<ellipse cx="270" cy="445" rx="183" ry="72" fill="#e0ecea" stroke="#94b7b3" stroke-width="2"/>');d.path('M87 445L270 190L453 445',color='teal',width=2,fill='#e6f0f0');d.path('M270 497V190',arrow=True);d.text(288,208,'z',27,'teal')
 d.image('crazyflie',95,350,355,245);d.path('M125 424C161 251 329 268 352 363',width=5,dash=True,arrow=True);d.pill(105,629,330,('Safe attitude set','安全姿态集合'));d.text(270,746,('Quadrotor attitude control','四旋翼姿态控制'),28,weight=650,anchor='middle');d.text(270,795,('Illustrative system model','系统模型示意'),25,'muted',anchor='middle')
 d.panel(532,108,870,728,('From dynamics to safe input','从动力学到安全输入'),2)
 d.node(568,176,378,110,('Discrete dynamics','离散动力学'),('Truncation order N','截断阶数 N'));d.node(992,176,374,110,('Relative degree','相对阶'),('Input–constraint relation','输入与约束的关系'));d.arrow(946,231,987,231)
 d.rect(568,346,798,214,'white','line');d.text(595,392,('Predictive safety horizon','安全预测时域'),31,weight=650)
 for i,lab in enumerate(['k','k + 1','…','k + m']):
  xx=628+i*221;d.circle(xx,474,32,'soft','teal');d.text(xx,484,lab,24,'teal',anchor='middle')
  if i<3:d.arrow(xx+33,474,xx+183,474)
 d.text(967,536,('Account for delayed control influence','考虑控制输入的延迟影响'),26,'muted',anchor='middle');d.arrow(1180,286,1180,341)
 d.node(568,623,373,113,('GD-CBF constraint','GD-CBF 约束'),('Generalized safety condition','广义安全条件'));d.node(993,623,373,113,('Safe controller','安全控制器'),('Compute input u(k)','求解控制输入 u(k)'));d.arrow(754,560,754,618);d.arrow(941,678,988,678);d.path('M1180 736V798H547V589H478',arrow=True)
 d.footer(('Match the safety horizon to the dynamics','让安全时域匹配系统动力学'),('Discrete-time safety · general relative degree','离散时间安全 · 广义相对阶'));d.finish('ma2026dtcbf')

def swarm(lang):
 d=Diagram('Human–swarm control',('Games, learning and safety','博弈、学习与安全'),lang)
 d.panel(38,108,464,728,('Human-guided formation','人类引导的编队'),1);d.person(123,203,.75);d.path('M179 235C298 171 438 193 433 344',arrow=True,dash=True);d.text(280,307,('Human command','人类指令'),26,'blue',anchor='middle')
 pts=[(252,389),(106,500),(375,500),(95,628),(263,651),(405,647)]
 for a,b in [(0,1),(0,2),(1,3),(1,4),(2,4),(2,5),(3,4),(4,5)]:d.path(f'M{pts[a][0]} {pts[a][1]}L{pts[b][0]} {pts[b][1]}','line',3)
 for i,(x,y) in enumerate(pts):
  d.image('crazyflie',x-64,y-35,128,83);d.circle(x+49,y-32,15,'teal' if i==0 else 'blue');d.text(x+49,y-25,'L' if i==0 else str(i),19,'white',anchor='middle')
 d.text(270,762,('Leader + five followers','领导者 + 五个跟随者'),28,weight=650,anchor='middle');d.text(270,806,('Crazyflie micro-quadrotors','Crazyflie 微型四旋翼'),24,'muted',anchor='middle')
 d.panel(532,108,870,728,('Hierarchical coordination','分层协同控制'),2)
 d.node(568,179,798,107,('Stackelberg–Nash game','Stackelberg–Nash 博弈'),('Human / leader · interacting followers','人类与领导者 · 多跟随者交互'))
 d.node(568,350,372,117,('Integral reinforcement','积分强化学习'),('learning · value iteration','价值函数迭代'));d.node(995,350,371,117,('Formation objectives','编队目标'),('Tracking + coordination','跟踪 + 协同'),color='white');d.arrow(755,286,755,345);d.arrow(995,408,945,408)
 d.node(568,530,372,108,('Nominal control','名义控制'),('Approximate optimality','近似最优性'));d.node(995,530,371,108,('CBF safety control','CBF 安全控制'),('Collision constraints','碰撞约束'));d.arrow(755,467,755,525);d.arrow(940,584,990,584)
 d.node(568,707,798,88,('Safe, coordinated swarm motion','安全协同的集群运动'));d.arrow(1180,638,1180,702);d.path('M568 752H522V429H478',arrow=True)
 d.footer(('Learn coordination, enforce safety','学习协同策略，施加安全约束'),('Human intention → collective motion','人类意图 → 集群运动'));d.finish('li2024humanswarm')

def us(lang):
 d=Diagram('US-CBF',('Safe learning in unknown environments','未知环境中的安全学习'),lang)
 d.panel(38,108,464,728,('Two sources of uncertainty','两类不确定性来源'),1);d.map(64,190,410,346);d.image('crazyflie',133,339,300,205);d.person(396,246,.55)
 d.circle(133,620,47,'soft','blue');
 for a in [0,120,240]:d.path(f'M133 620q{40*math.cos(math.radians(a)):.1f} {40*math.sin(math.radians(a)):.1f} {37*math.cos(math.radians(a+60)):.1f} {37*math.sin(math.radians(a+60)):.1f}',color='blue',width=12)
 d.path('M202 593q43 -19 84 0M202 620q52 -20 105 0M202 647q42 -19 82 0','blue',3);d.text(320,698,('Unknown dynamics','未知动力学'),25,'blue',anchor='middle');d.text(270,756,'Crazyflie 2.1',28,weight=650,anchor='middle');d.text(270,801,('Wind + uncertain obstacles','气流扰动 + 不确定障碍'),25,'muted',anchor='middle')
 d.panel(532,108,870,728,('Separate, learn, constrain','分离、学习、约束'),2)
 d.node(568,175,373,109,('Environment GP','环境高斯过程'),('Obstacle observations','障碍观测'));d.node(994,175,372,109,('Dynamics GP','动力学高斯过程'),('State–input observations','状态与输入观测'))
 d.rect(568,344,373,242,'white','line');d.text(754,387,('US-CBF decomposition','US-CBF 分解'),29,weight=650,anchor='middle');d.pill(593,414,323,('Nominal barrier','名义屏障函数'));d.pill(593,485,323,('Uncertainty barrier','不确定性屏障函数'),'#f3e9db');d.text(754,562,('Geometry + confidence','几何 + 置信度'),24,'muted',anchor='middle')
 d.rect(994,344,372,242,'white','line');d.text(1180,387,('Residual dynamics','残差动力学'),29,weight=650,anchor='middle');d.pill(1018,414,324,('Feedforward estimate','前馈估计'));d.pill(1018,485,324,('Robustness margin','鲁棒裕度'),'#f3e9db');d.text(1180,562,('Prediction + uncertainty','预测 + 不确定性'),24,'muted',anchor='middle')
 d.arrow(754,284,754,339);d.arrow(1180,284,1180,339)
 d.node(568,669,798,118,('QP-based safe control','基于二次规划的安全控制'),('Combine barriers with learned compensation','组合屏障约束与学习补偿'));d.arrow(754,586,754,664);d.arrow(1180,586,1180,664);d.path('M568 727H520V545H478',arrow=True)
 d.footer(('Distinguish uncertainty before enforcing safety','先区分不确定性，再施加安全约束'),('Environment learning + dynamics learning','环境学习 + 动力学学习'));d.finish('li2023uscbf')

if __name__=='__main__':
 for lang in ('en','zh'):
  for build in (shape,ct,ncub,dg,stgp,gd,swarm,us):build(lang)
 print('Wrote 16 bilingual SVG diagrams.')
