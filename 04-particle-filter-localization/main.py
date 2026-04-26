import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation


class World:
    # Stores the simulation world size and landmark positions.
    def __init__(self, height, width, landmarks):
        self.height = height
        self.width = width

        if landmarks is None:
            self.landmarks = []
        else:
            self.landmarks = landmarks

    # Draws the world boundary, grid, and landmarks.
    def draw(self, ax):
        ax.set_aspect("equal")
        ax.grid(True)
        ax.set_ylim(-self.height, self.height)
        ax.set_xlim(-self.width, self.width)
        ax.set_title("Simulation Space")

        for landmark_x, landmark_y in self.landmarks:
            ax.scatter(landmark_x, landmark_y, s=100, marker="x", color="black")
            ax.text(landmark_x + 0.2, landmark_y + 0.2, "Landmark", fontsize=12)


class Robot:
    # Stores the true robot pose.
    def __init__(self, x_position, y_position, theta, radius):
        self.x_position = x_position
        self.y_position = y_position
        self.theta = theta
        self.radius = radius

    # Draws the true robot body and heading direction.
    def makeBody(self, ax):
        circle = Circle((self.x_position, self.y_position), self.radius, fill=False)
        ax.add_patch(circle)

        dx = self.radius * np.cos(self.theta)
        dy = self.radius * np.sin(self.theta)

        ax.arrow(
            self.x_position,
            self.y_position,
            dx,
            dy,
            head_width=0.2,
            head_length=0.2,
            length_includes_head=True,
            color="green",
        )

    # Moves the true robot using noisy forward and turning commands.
    def move(self, forward, motion_noise, turn, turn_noise):
        turn = turn + np.random.normal(0, turn_noise)
        self.theta += turn
        self.theta = self.theta % (2 * np.pi)

        forward = forward + np.random.normal(0, motion_noise)
        self.x_position = self.x_position + forward * np.cos(self.theta)
        self.y_position = self.y_position + forward * np.sin(self.theta)

    # Returns noisy distance observations from the true robot to each landmark.
    def sense(self, world, sensor_noise=0.3):
        observation = []
        landmarks = world.landmarks

        for landmark_x, landmark_y in landmarks:
            dx = landmark_x - self.x_position
            dy = landmark_y - self.y_position

            distance = np.sqrt(dx**2 + dy**2)
            distance = distance + np.random.normal(0, sensor_noise)

            observation.append(distance)

        return observation


class Particle:
    # Stores one possible robot pose hypothesis.
    def __init__(self, x_position, y_position, theta, weight=1.0):
        self.x_position = x_position
        self.y_position = y_position
        self.theta = theta
        self.weight = weight

    # Moves this particle using the same motion model as the robot.
    def move(self, forward, motion_noise, turn, turn_noise):
        noisy_turn = turn + np.random.normal(0, turn_noise)
        self.theta = self.theta + noisy_turn
        self.theta = self.theta % (2 * np.pi)

        noisy_forward = forward + np.random.normal(0, motion_noise)
        self.x_position += noisy_forward * np.cos(self.theta)
        self.y_position += noisy_forward * np.sin(self.theta)

    # Predicts what this particle would sense if it were the true robot.
    def predictSense(self, world):
        predicted_observations = []
        landmarks = world.landmarks

        for landmark_x, landmark_y in landmarks:
            dx = landmark_x - self.x_position
            dy = landmark_y - self.y_position

            distance = np.sqrt(dx**2 + dy**2)
            predicted_observations.append(distance)

        return predicted_observations

    # Draws this particle as a small blue dot.
    def draw(self, ax):
        ax.scatter(self.x_position, self.y_position, s=10, alpha=0.4, color="blue")


# Converts sensor error into likelihood using a Gaussian-like function.
def gaussianLikelihood(error, sigma):
    return np.exp(-(error**2) / (2 * sigma**2))


# Creates random particles across the whole world.
def createParticles(number_of_particles, world):
    particles = []

    for _ in range(number_of_particles):
        x = np.random.uniform(-world.width, world.width)
        y = np.random.uniform(-world.height, world.height)
        theta = np.random.uniform(0, 2 * np.pi)
        weight = 1.0 / number_of_particles

        particle = Particle(x, y, theta, weight)
        particles.append(particle)

    return particles


# Updates particle weights by comparing predicted observations with real robot observations.
def updateParticleWeights(particles, observations, world, sensor_noise):
    for particle in particles:
        predicted_observations = particle.predictSense(world)

        weight = 1.0

        for predicted_observation, observation in zip(predicted_observations, observations):
            error = observation - predicted_observation
            likelihood = gaussianLikelihood(error, sensor_noise)
            weight *= likelihood

        particle.weight = weight


# Normalizes particle weights so the total becomes 1.
def normalizeParticleWeights(particles):
    total_weight = sum(particle.weight for particle in particles)

    if total_weight == 0:
        uniform_weight = 1.0 / len(particles)

        for particle in particles:
            particle.weight = uniform_weight

        return

    for particle in particles:
        particle.weight /= total_weight


# Resamples particles based on their weights.
def resampleParticles(particles):
    weights = [particle.weight for particle in particles]

    selected_indices = np.random.choice(
        range(len(particles)),
        size=len(particles),
        replace=True,
        p=weights,
    )

    new_particles = []

    for index in selected_indices:
        selected_particle = particles[index]

        # Add tiny noise after resampling so copied particles do not become exactly identical.
        new_particle = Particle(
            selected_particle.x_position + np.random.normal(0, 0.03),
            selected_particle.y_position + np.random.normal(0, 0.03),
            selected_particle.theta + np.random.normal(0, 0.01),
            weight=1.0 / len(particles),
        )

        new_particles.append(new_particle)

    return new_particles


# Estimates the robot pose by averaging all particle poses.
def estimatePose(particles):
    x = np.mean([particle.x_position for particle in particles])
    y = np.mean([particle.y_position for particle in particles])

    sin_sum = np.mean([np.sin(particle.theta) for particle in particles])
    cos_sum = np.mean([np.cos(particle.theta) for particle in particles])
    theta = np.arctan2(sin_sum, cos_sum)

    return x, y, theta


# Draws the estimated robot pose as a red X.
def drawEstimatedPose(ax, estimated_pose):
    estimated_x, estimated_y, _ = estimated_pose
    ax.scatter(estimated_x, estimated_y, s=120, marker="x", color="red", label="Estimated Pose")

def drawWeightedParticles(particles, ax):
    xs = [particle.x_position for particle in particles]
    ys = [particle.y_position for particle in particles]
    weights = [particle.weight for particle in particles]

    max_weight = max(weights)

    if max_weight == 0:
        sizes = [10 for _ in particles]
    else:
        sizes = [10 + 500 * (weight / max_weight) for weight in weights]

    ax.scatter(xs, ys, s=sizes, alpha=0.35, color="blue", label="Weighted Particles")


# Main simulation loop.
def main():
    landmarks = [
        (2, 3),
        (-4, 5),
        (5, -2),
    ]

    world = World(8, 8, landmarks)
    robot = Robot(-6, -6, np.pi / 6, 1)
    particles = createParticles(500, world)

    motion_noise = 0.1
    turn_noise = 0.05
    sensor_noise = 1.0

    commands = [
        (0.3, 0.03),
        (0.3, 0.03),
        (0.3, 0.03),
        (0.3, 0.03),
        (0.3, -0.05),
        (0.3, -0.05),
        (0.3, -0.05),
        (0.3, 0.00),
        (0.3, 0.00),
        (0.3, 0.00),
        (0.3, 0.05),
        (0.3, 0.05),
        (0.3, 0.05),
        (0.3, 0.00),
        (0.3, 0.00),
        (0.3, 0.00),
        (0.3, -0.04),
        (0.3, -0.04),
        (0.3, -0.04),
        (0.3, 0.00),
    ]

    fig, ax = plt.subplots(figsize=(8, 8))

    # Updates one animation frame.
    def update(frame):
        nonlocal particles

        ax.clear()

        forward, turn = commands[frame]

        robot.move(
            forward=forward,
            motion_noise=motion_noise,
            turn=turn,
            turn_noise=turn_noise,
        )

        for particle in particles:
            particle.move(
                forward=forward,
                motion_noise=motion_noise,
                turn=turn,
                turn_noise=turn_noise,
            )

        observations = robot.sense(world, sensor_noise=sensor_noise)

        updateParticleWeights(
            particles,
            observations,
            world,
            sensor_noise=sensor_noise,
        )

        normalizeParticleWeights(particles)

        particles = resampleParticles(particles)

        estimated_pose = estimatePose(particles)

        world.draw(ax)

        for particle in particles:
            particle.draw(ax)

        robot.makeBody(ax)
        drawEstimatedPose(ax, estimated_pose)

        ax.set_title(f"Step {frame + 1}: Particle Filter Localization")
        ax.legend(loc="upper right")

        print(f"Step {frame + 1}")
        print("Robot observation:", np.round(observations, 2))
        print(
            "True robot:",
            round(robot.x_position, 2),
            round(robot.y_position, 2),
        )
        print(
            "Estimated:",
            round(estimated_pose[0], 2),
            round(estimated_pose[1], 2),
        )
        print()

    animation = FuncAnimation(
        fig,
        update,
        frames=len(commands),
        interval=900,
        repeat=False,
    )

    animation.save("particle_filter_localization.gif", writer="pillow", fps=3)

    plt.show()


if __name__ == "__main__":
    main()