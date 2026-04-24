# 2D Grid Bayes Localization From Scratch

## Overview

This project implements a simple Bayes filter for robot localization in a 2D grid world.

The robot does not know its true position. Instead, it maintains a belief distribution over all possible grid cells.

## Grid World

`.` = free cell  
`#` = wall  
`D` = door / landmark

Example map:

```txt
. . . . .
. # . D .
. . . . .
. D . # .
. . . . .

In Experiment 1, the robot starts with no knowledge of its position. Therefore, the belief is uniformly distributed over all non-wall cells. After receiving the observation `isDoorNearby`, the belief increases around cells that are close to doors. This shows that the sensor update reweights each cell based on how consistent it is with the observation.

In Experiment 2, the robot receives a movement command to move right. The motion model assumes that the robot successfully moves in the intended direction with probability 0.8, stays in place with probability 0.1, and moves randomly with probability 0.1. The belief shifts to the right, but some probability remains or spreads to neighboring cells because the motion is uncertain.