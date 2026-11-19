# Robot render sources

These PNGs are renders of meshes, not cropped experiment photographs. The background alpha comes directly from MuJoCo's geometry segmentation pass. No skybox, floor or backdrop is present. `scripts/render_robot_models.py` defines the camera, pose and lighting. Mesh geometry is not stretched. Render date: 2026-11-19.

| PNG | Source | Use and limits |
| --- | --- | --- |
| `fr3.png` | [MuJoCo Menagerie / Franka FR3](https://github.com/google-deepmind/mujoco_menagerie/tree/main/franka_fr3) | FR3 arm for DG-ACMP and NCUB; original mesh poses are illustrative, not a reconstruction of a recorded experiment. Apache-2.0, derived from Franka's public robot description. |
| `crazyflie.png` | [MuJoCo Menagerie / Crazyflie 2](https://github.com/google-deepmind/mujoco_menagerie/tree/main/bitcraze_crazyflie_2) | Crazyflie-family visual reference for the swarm and US-CBF. US-CBF identifies Crazyflie 2.1; this public mesh is the simplified Crazyflie 2 family model, not a claim of exact revision. In GD-CBF it is a representative quadrotor illustration, not a claimed hardware experiment. MIT. |
| `openarm.png` | [Enactic / OpenArm MuJoCo v1](https://github.com/enactic/openarm_mujoco/tree/master/v1) | Official bimanual OpenArm geometry, with an illustrative bent-arm pose. CT-VAM controls the left arm on a bimanual platform. Apache-2.0. |
| `sharpa.png` | [Sharpa / Wave right-hand model](https://github.com/sharpa-robotics/sharpa-urdf-usd-xml/tree/main/wave_01/right_sharpa_wave) | Official 22-DoF hand geometry. Grayscale material override for the common visual palette. Used as a dexterous-hand embodiment illustration in SHAPE; the paper describes two 7-DoF arms and two 22-DoF hands but does not specify a product revision. Apache-2.0. |
| `mobile.png` | `scripts/models/mobile.xml` | Original simplified geometry based on the paper's self-built four-wheel differential-drive platform with LiDAR. Not a commercial robot model or exact CAD reconstruction. |

License notices are included alongside these files. All arrows, maps, icons and task objects in the teasers are original vector schematics. The GP curve and map fields explain method structure; they are not experimental measurements.
