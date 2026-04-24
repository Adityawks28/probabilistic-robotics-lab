# Probabilistic Robotics Lab

A personal learning laboratory for implementing core probabilistic robotics algorithms from scratch.

This repository is designed to help me build a deep understanding of robot localization, filtering, mapping, and SLAM by implementing the algorithms step by step instead of only using existing robotics libraries.

The main idea behind this repository is simple:

> A robot usually cannot know its true state perfectly. It must estimate where it is by combining uncertain motion and noisy sensor observations.

This repository starts from basic Bayes filtering in a grid world, then gradually moves toward Kalman filtering, Extended Kalman Filter localization, particle filters, occupancy grid mapping, and eventually SLAM-related projects.

---

## Why I Made This Repository

I am studying robotics and want to understand localization and SLAM from the foundation. Instead of jumping directly into ROS, Gazebo, CARLA, or Isaac Sim, I want to first understand the mathematical and algorithmic ideas behind robot state estimation.

This repository is my roadmap for learning probabilistic robotics through code, experiments, visualizations, and written explanations.

The long-term goal is to become comfortable with:

* Bayes filters
* Motion models
* Sensor models
* Kalman Filters
* Extended Kalman Filters
* Particle Filters
* Occupancy Grid Mapping
* SLAM
* Robotics simulation using ROS 2, Gazebo, CARLA, and eventually Isaac Sim

---

## Core Concept

In probabilistic robotics, the robot does not usually store only one estimated position. Instead, it stores a **belief**.

The belief represents the probability distribution over possible robot states:

```txt
bel(x_t) = p(x_t | z_1:t, u_1:t)
```

This means:

```txt
The probability of the robot being in state x_t,
given all sensor observations and control commands so far.
```

Each filtering algorithm in this repository follows the same basic rhythm:

```txt
Prediction / Motion Update
→ Correction / Sensor Update
→ New Belief
→ Repeat
```

The motion update predicts where the robot may be after executing a command.

The sensor update corrects that prediction using sensor observations.

---

## Repository Structure

Planned structure:

```txt
probabilistic-robotics-lab/
├── 01-grid-bayes-localization/
├── 02-kalman-filter-tracking/
├── 03-ekf-landmark-localization/
├── 04-particle-filter-localization/
├── 05-occupancy-grid-mapping/
├── 06-ros2-gazebo-slam/
├── 07-carla-sensor-fusion/
└── README.md
```

Each project is designed to be self-contained and includes:

```txt
main implementation
experiment scripts
visualizations
README explanation
notes about what I learned
```

---

# Project Roadmap

## Project 1 — Grid Bayes Localization From Scratch

**Status:** Completed first version

### Goal

Implement a simple Bayes filter for robot localization in a 2D grid world.

The robot does not know its true position. Instead, it maintains a probability distribution over all possible grid cells.

### World Model

Example grid:

```txt
. . . . .
. # . D .
. . . . .
. D . # .
. . . . .
```

Where:

```txt
. = free cell
# = wall
D = door / landmark
```

### Core Idea

The robot starts with a uniform belief over all free cells.

Then it repeatedly performs:

```txt
motion update
sensor update
normalization
```

### Motion Update

The motion model assumes:

```txt
80% intended movement
10% stay in place
10% random movement
```

In code, the key idea is:

```python
newBelief[new_y][new_x] += belief[y][x] * moveProbability
```

This means:

```txt
Motion update moves probability mass from old cells to possible new cells.
```

### Sensor Update

The robot can observe:

```txt
isDoorNearby
noDoorNearby
```

The sensor model assumes:

```txt
0.9 likelihood if the observation matches the cell condition
0.1 likelihood if the observation does not match
```

In code, the key idea is:

```python
newBelief[y][x] = belief[y][x] * likelihood
```

This means:

```txt
Sensor update does not move probability.
It reweights each cell based on how well that cell explains the observation.
```

### Experiments

The project includes several experiments:

```txt
Experiment 1: Sensor update only
Experiment 2: Motion update only
Experiment 3: Full Bayes filter loop
Experiment 4: Opposite observations
Experiment 5: Boundary behavior
```

### What I Learned

From this project, I learned:

* Localization is not just estimating one position.
* A robot can represent uncertainty using a belief distribution.
* Motion update spreads or shifts probability.
* Sensor update reweights probability based on observation likelihood.
* Normalization is necessary to keep the belief as a valid probability distribution.
* Even a simple grid world contains the core idea of probabilistic robotics.

---

## Project 2 — Kalman Filter Tracking From Scratch

**Status:** Planned

### Goal

Implement a basic Kalman Filter to estimate the state of a robot moving in one dimension.

This project moves from discrete grid-based belief to continuous Gaussian belief.

### State

The robot state can be represented as:

```txt
x_t = [position, velocity]^T
```

The robot receives noisy position measurements and uses a Kalman Filter to estimate the true position and velocity.

### Core Idea

The Kalman Filter represents belief using:

```txt
mean
covariance
```

The mean is the best estimate.

The covariance represents uncertainty.

### What I Will Implement

* 1D robot motion simulation
* Noisy measurement generation
* Kalman prediction step
* Kalman correction step
* Plot of true position, noisy measurements, and estimated position

### Important Concepts

* Gaussian distribution
* Mean and variance
* Prediction step
* Correction step
* Kalman gain
* Innovation / residual
* Measurement noise
* Motion noise

### Expected Result

The Kalman Filter estimate should be smoother and more accurate than the raw noisy measurements.

### Learning Target

After finishing this project, I should be able to explain:

```txt
Kalman Filter is a smart weighted average between prediction and measurement.
```

---

## Project 3 — Extended Kalman Filter Landmark Localization

**Status:** Planned

### Goal

Implement EKF localization for a 2D robot that observes known landmarks.

This project introduces nonlinear robot motion and nonlinear sensor models.

### Robot State

```txt
x_t = [x, y, theta]^T
```

Where:

```txt
x = horizontal position
y = vertical position
theta = robot heading angle
```

### Sensor Model

The robot observes known landmarks using range and bearing:

```txt
range = distance to landmark
bearing = angle to landmark
```

### Why EKF Is Needed

A normal Kalman Filter assumes linear models.

However, robot motion and landmark observation are usually nonlinear because they involve:

```txt
sin(theta)
cos(theta)
atan2()
square roots
```

The Extended Kalman Filter handles this by linearizing the nonlinear functions using Jacobians.

### What I Will Implement

* 2D robot simulator
* Known landmark map
* Range-bearing sensor model
* EKF prediction step
* EKF correction step
* Jacobian calculation
* Uncertainty ellipse visualization

### Important Concepts

* Nonlinear motion model
* Nonlinear observation model
* Jacobian matrix
* Linearization
* Covariance propagation
* Range-bearing measurement
* Mahalanobis distance, optional extension

### Expected Result

The EKF should estimate the robot trajectory using noisy motion and noisy landmark observations.

The visualization should show:

```txt
true trajectory
estimated trajectory
landmarks
uncertainty ellipse
```

### Learning Target

After this project, I should understand how probabilistic localization works for a continuous 2D robot pose.

---

## Project 4 — Particle Filter / Monte Carlo Localization

**Status:** Planned

### Goal

Implement particle filter localization in a 2D map.

This project introduces sample-based belief representation.

### Core Idea

Instead of representing belief as a grid or a single Gaussian, a particle filter represents belief using many particles.

Each particle is a hypothesis about the robot's pose:

```txt
particle = possible robot pose
weight = how likely that pose is
```

### Algorithm

The particle filter loop is:

```txt
1. Sample motion for each particle
2. Compute sensor likelihood for each particle
3. Normalize weights
4. Resample particles
5. Estimate robot pose
```

### What I Will Implement

* 2D map
* Robot motion model
* Range sensor or landmark sensor model
* Particle initialization
* Particle motion update
* Importance weighting
* Resampling
* Pose estimation
* Particle visualization

### Important Concepts

* Sampling
* Importance weights
* Resampling
* Degeneracy problem
* Multimodal belief
* Kidnapped robot problem

### Expected Result

At first, particles may be spread across the map.

After repeated motion and sensor updates, particles should concentrate around the true robot position.

### Learning Target

After finishing this project, I should understand why particle filters are useful when the belief distribution is not a single Gaussian.

---

## Project 5 — Occupancy Grid Mapping From Scratch

**Status:** Planned

### Goal

Implement occupancy grid mapping using simulated range sensor data.

This project shifts from estimating the robot's position to estimating the environment.

### Core Idea

The map is represented as a grid.

Each cell stores the probability that the cell is occupied:

```txt
p(occupied)
```

### What I Will Implement

* 2D grid map
* Simulated LiDAR/range measurements
* Ray casting
* Inverse sensor model
* Log-odds update
* Map visualization

### Important Concepts

* Occupancy grid
* Free cells
* Occupied cells
* Unknown cells
* Log-odds representation
* Inverse sensor model
* Ray casting

### Expected Result

The robot should gradually build a map from sensor measurements.

The map should show:

```txt
free space
occupied walls/obstacles
unknown regions
```

### Learning Target

After finishing this project, I should understand how robots can build a map from range measurements.

---

## Project 6 — ROS 2 Gazebo SLAM Lab

**Status:** Planned

### Goal

Connect the theory from previous projects to practical robotics tools using ROS 2 and Gazebo.

This project uses existing SLAM tools, but the goal is to understand what they are doing internally.

### Tools

Planned tools:

```txt
ROS 2
Gazebo
TurtleBot3
RViz
SLAM Toolbox
Nav2
```

### What I Will Implement

* Launch TurtleBot3 in Gazebo
* Run SLAM Toolbox
* Visualize `/scan`, `/odom`, `/map`, and `/tf`
* Build an occupancy grid map
* Save the generated map
* Use Nav2 to navigate using the map

### Important Concepts

* ROS 2 nodes
* Topics
* TF frames
* `/scan`
* `/odom`
* `/map`
* `map -> odom`
* `odom -> base_link`
* `base_link -> laser`
* SLAM vs localization

### Expected Result

The robot should be able to explore a simulated environment, build a map, and navigate using that map.

### Learning Target

After this project, I should be able to connect the mathematical ideas of filtering and mapping with practical ROS-based robotics systems.

---

## Project 7 — CARLA Sensor Fusion Localization

**Status:** Optional / Planned

### Goal

Apply probabilistic localization ideas in an autonomous driving simulator.

CARLA provides a more realistic environment for vehicle localization compared to a simple grid or indoor robot simulator.

### Planned Sensors

```txt
GNSS / GPS
IMU
Odometry
LiDAR, optional
```

### What I Will Implement

* Spawn a vehicle in CARLA
* Collect noisy GNSS and IMU data
* Estimate vehicle trajectory using EKF
* Compare estimated trajectory with ground truth
* Plot position error over time

### Important Concepts

* Sensor fusion
* Vehicle state estimation
* GPS noise
* IMU drift
* Coordinate frames
* Ground truth comparison

### Expected Result

The estimated vehicle trajectory should be more stable than raw noisy sensor data.

### Learning Target

After finishing this project, I should understand how filtering is used in autonomous vehicle localization.

---

# Learning Order

Recommended order:

```txt
01 Grid Bayes Localization
→ 02 Kalman Filter Tracking
→ 03 EKF Landmark Localization
→ 04 Particle Filter Localization
→ 05 Occupancy Grid Mapping
→ 06 ROS 2 Gazebo SLAM
→ 07 CARLA Sensor Fusion Localization
```

This order is intentional.

Project 1 teaches discrete belief.

Project 2 teaches Gaussian belief.

Project 3 teaches nonlinear robot localization.

Project 4 teaches sample-based belief.

Project 5 teaches mapping.

Project 6 connects everything to ROS and SLAM tools.

Project 7 applies the same ideas to autonomous driving simulation.

---

# Summary of Concepts by Project

| Project                      | Main Concept                 | Belief Representation          |
| ---------------------------- | ---------------------------- | ------------------------------ |
| Grid Bayes Localization      | Discrete Bayes filter        | Probability grid               |
| Kalman Filter Tracking       | Linear Gaussian filtering    | Mean + covariance              |
| EKF Landmark Localization    | Nonlinear Gaussian filtering | Mean + covariance              |
| Particle Filter Localization | Monte Carlo localization     | Weighted particles             |
| Occupancy Grid Mapping       | Mapping                      | Occupancy probabilities        |
| ROS 2 Gazebo SLAM            | Practical SLAM               | Tool-based map + pose estimate |
| CARLA Sensor Fusion          | Vehicle localization         | EKF / fused state estimate     |

---

# Long-Term Goal

The final goal of this repository is to prepare myself for more advanced robotics projects involving:

* mobile robot localization
* SLAM
* sensor fusion
* autonomous navigation
* robot manipulation with uncertain perception
* mobile manipulation systems

This repository is not only a collection of code. It is a learning record that connects theory, implementation, visualization, and experiments.

---

# Current Progress

* [x] Project 1: Grid Bayes Localization From Scratch
* [ ] Project 2: Kalman Filter Tracking From Scratch
* [ ] Project 3: EKF Landmark Localization
* [ ] Project 4: Particle Filter Localization
* [ ] Project 5: Occupancy Grid Mapping
* [ ] Project 6: ROS 2 Gazebo SLAM
* [ ] Project 7: CARLA Sensor Fusion Localization

---

# Notes to Future Me

When learning robotics, it is easy to jump into big tools too early. But the important thing is to understand what the tools are estimating.

Before using SLAM Toolbox, AMCL, Nav2, or CARLA sensor fusion, I want to understand the basic question:

```txt
How does a robot update its belief about the world when both motion and sensors are uncertain?
```

This repository is my attempt to answer that question step by step.
