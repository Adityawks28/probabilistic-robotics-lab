# Robotics Learning System

This page tracks my long-term learning projects across probabilistic robotics, robot vision, deep learning, and robot manipulation.

The goal is to build a strong robotics portfolio by learning from fundamentals, implementing algorithms from scratch, visualizing results, and writing clear explanations.

---

## Status Legend

| Status | Meaning |
|---|---|
| Finished | Project has a working implementation, basic explanation, and committed result |
| WIP | Project is currently being implemented or improved |
| Haven't Started | Project has not been started yet |

---

# Master Progress Dashboard

| Area | Project | Status | Priority | Notes |
|---|---|---|---|---|
| Probabilistic Robotics | 01 Grid Bayes Localization | Finished | High | First completed Bayes filter project |
| Probabilistic Robotics | 02 Kalman Filter Tracking | Haven't Started | Medium | Linear Gaussian filtering |
| Probabilistic Robotics | 03 EKF Landmark Localization | Haven't Started | Medium | Nonlinear localization with landmarks |
| Probabilistic Robotics | 04 Particle Filter Localization | WIP | High | Current Monte Carlo Localization project |
| Probabilistic Robotics | 05 Occupancy Grid Mapping | Haven't Started | High | Mapping with log-odds |
| Probabilistic Robotics | 06 ROS 2 Gazebo SLAM | Haven't Started | High | Practical SLAM with ROS 2 |
| Probabilistic Robotics | 07 CARLA Sensor Fusion | Haven't Started | Medium | Autonomous driving-style localization |
| Robot Vision | 01 Image Processing Basics | Haven't Started | High | Pixels, filters, edges, thresholding |
| Robot Vision | 02 Camera Geometry | Haven't Started | High | 3D-to-2D projection |
| Robot Vision | 03 Camera Calibration | Haven't Started | High | Intrinsics, distortion, reprojection error |
| Robot Vision | 04 Classical Object Detection | Haven't Started | High | Color thresholding and contours |
| Robot Vision | 05 Object Tracking | Haven't Started | Medium | Tracking objects over video |
| Robot Vision | 06 CNN Image Classification | Haven't Started | High | Bridge to deep learning vision |
| Robot Vision | 07 YOLO Object Detection | Haven't Started | Medium | Bounding-box detection |
| Robot Vision | 08 Image Segmentation | Haven't Started | Medium | Pixel-level object masks |
| Robot Vision | 09 RGB-D Object Localization | Haven't Started | High | Estimate 3D position from pixel + depth |
| Robot Vision | 10 Camera-to-Robot Transform | Haven't Started | High | Convert camera frame to robot base frame |
| Robot Vision | 11 Vision-Guided Pick-and-Place | Haven't Started | High | Connect vision to manipulation |
| Robot Vision | 12 Visual Odometry | Haven't Started | Medium | Camera motion from images |
| Deep Learning | 01 Perceptron From Scratch | Haven't Started | High | Foundation of neural networks |
| Deep Learning | 02 Neural Network From Scratch | Haven't Started | High | Multi-layer learning |
| Deep Learning | 03 Backpropagation From Scratch | Haven't Started | High | Core training algorithm |
| Deep Learning | 04 PyTorch Basics | Haven't Started | High | Practical DL framework |
| Deep Learning | 05 CNN Image Classification | Haven't Started | High | Vision model basics |
| Deep Learning | 06 Transfer Learning | Haven't Started | Medium | Use pretrained models |
| Deep Learning | 07 Object Detection Basics | Haven't Started | Medium | Detection model concepts |
| Deep Learning | 08 Segmentation Basics | Haven't Started | Medium | U-Net / mask prediction |
| Robot Manipulation | 01 Forward Kinematics | Haven't Started | High | Joint angles to end-effector position |
| Robot Manipulation | 02 Inverse Kinematics | Haven't Started | High | Target position to joint angles |
| Robot Manipulation | 03 Jacobian IK | Haven't Started | High | Iterative IK |
| Robot Manipulation | 04 Motion Planning RRT | Haven't Started | Medium | Collision-free planning |
| Robot Manipulation | 05 MoveIt 2 Planning | Haven't Started | High | Practical manipulation planning |
| Robot Manipulation | 06 Isaac Sim Pick-and-Place | Haven't Started | High | Simulation-based manipulation |
| Robot Manipulation | 07 Vision-Guided Pick-and-Place | Haven't Started | High | Combine vision and arm control |
| Robot Manipulation | 08 Trash Sorting Manipulator | Haven't Started | High | Long-term flagship project |

---

# Current Focus

## Main Focus

| Current Focus | Status | Why |
|---|---|---|
| Particle Filter Localization | WIP | Next class is about Monte Carlo Localization and particle filters |

## Secondary Focus

| Secondary Focus | Status | Why |
|---|---|---|
| Robot Vision Lab Setup | Haven't Started | Needed for perception and manipulation projects |
| Deep Learning Lab Setup | Haven't Started | Needed for modern computer vision |
| Robot Manipulation Lab Setup | Haven't Started | Needed for Isaac Sim and lab work |

---

# Weekly Battle Plan

## This Week

| Task | Area | Status | Notes |
|---|---|---|---|
| Add weighted particle visualization before resampling | Probabilistic Robotics | Haven't Started | Shows particle weights clearly |
| Add before/after resampling comparison | Probabilistic Robotics | Haven't Started | Shows weight → density transformation |
| Write README for particle filter project | Probabilistic Robotics | Haven't Started | Explain MCL clearly |
| Save particle filter animation GIF | Probabilistic Robotics | WIP | Already has animation save logic |
| Create Robot Vision Lab repo | Robot Vision | Haven't Started | Start computer vision roadmap |
| Create Deep Learning Lab repo | Deep Learning | Haven't Started | Start DL roadmap later |

---

# Probabilistic Robotics Lab

Repository:

```txt
probabilistic-robotics-lab