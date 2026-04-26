import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class World:
    def __init__(self, height, width, landmarks):
        self.height = height
        self.width = width
        if landmarks is None :
            self.landmarks=[]
        else :
            self.landmarks=landmarks
    
    def draw(self):
        fig, ax=plt.subplots(figsize=(8, 8))
        ax.set_aspect("equal")
        ax.grid(True)
        ax.set_ylim(-self.height, self.height)
        ax.set_xlim(-self.width, self.width)
        ax.set_title("Simulation Space")
        # ax.plot(6, -6, 'ro', markersize=10) -> red circle landmark

        for landmark_x, landmark_y in self.landmarks :
            ax.scatter(landmark_x, landmark_y, s=100, marker='x')
            ax.text(landmark_x + 0.2, landmark_y + 0.2, "Landmark", fontsize=12)
            
        return fig, ax

landmarks = [(2, 3),
        (-4, 5),
        (5, -2)]
world = World(8, 8, landmarks)
fig, ax = world.draw()

class Robot:
    def __init__(self, x_position, y_position, theta, radius) :
        self.x_position = x_position
        self.y_position = y_position
        self.theta = theta
        self.radius = radius
    
    def makeBody(self, ax):
        circle = Circle((self.x_position, self.y_position), self.radius, fill=False)
        ax.add_patch(circle)

        # add facing direction
        dx = self.radius * np.cos(self.theta)
        dy = self.radius * np.sin(self.theta)

        ax.arrow(self.x_position, self.y_position, dx, dy, head_width=0.2, head_length=0.2, length_includes_head=True)
    
    def move(self, forward, motion_noise, turn, turn_noise) :
        turn = turn + np.random.normal(0, turn_noise)
        self.theta = self.theta % (2 * np.pi)
        self.theta += turn

        forward = forward + np.random.normal(0, motion_noise)
        self.x_position = self.x_position + forward * np.cos(self.theta)
        self.y_position = self.y_position + forward * np.sin(self.theta)
    
    def sense(self, world, sensor_noise=0.3):
        observation = []
        landmarks = world.landmarks
        for landmark_x, landmark_y in landmarks :
            dx = landmark_x - self.x_position
            dy = landmark_y - self.y_position
            distance = np.sqrt(dx**2 + dy**2)
            distance = distance + np.random.normal(0, sensor_noise)

            observation.append(f"{distance:.4f}")
        return (observation)

class Particle:
    def __init__(self, x_position, y_position, theta, weight=1.0):
        self.x_position = x_position
        self.y_position = y_position
        self.theta = theta
        self.weight = weight
    
    def move(self, forward, motion_noise, turn, turn_noise) : 
        noisy_turn = turn * np.random.normal(0, turn_noise)
        self.theta = self.theta + noisy_turn

        noisy_forward = forward * np.random.normal(0, motion_noise)
        self.x_position += noisy_forward * np.cos(self.theta)
        self.y_position += noisy_forward * np.sin(self.theta)
    
    def draw(self, ax):
        ax.scatter(self.x_position, self.y_position, s=10, alpha=0.4, color="blue")
        

robot = Robot(-6, -6, 3.14/6, 1)
robot.makeBody(ax)
observations = robot.sense(world)
print(observations)

plt.show()
