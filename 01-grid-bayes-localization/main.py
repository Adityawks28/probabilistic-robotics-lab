# Making grid bayes localization
import os
import numpy as np
import matplotlib.pyplot as plt

# Make the basic data structure, ignore for now
realGrid = [ ["." , ".", "."],
            [".", "D", "."],
            [".", ".", "."] ]

# Making the grid
def makeTheGrid():
    grid = [
        [".", ".", ".", ".", "."],
        [".", "#", ".", "D", "."],
        [".", ".", ".", ".", "."],
        [".", "D", ".", "#", "."],
        [".", ".", ".", ".", "."],
    ]

    # for row in grid :
    #     print(row)
    # # print("the grid length is : " + str(len(grid)))
    # print("the grid height is : " + str(len(grid[0])))

    return grid

#makeTheGrid()

def initialize_belief(grid) :
    width = len(grid)
    height = len(grid[0])
    free_cells = 0

    for y in range(0, height) :
        for x in range(0, width) :
            if grid[y][x] != "#" :
                free_cells += 1
    
    belief = np.zeros((height, width))

    for y in range(0, height) :
        for x in range(0, width) :
            if grid[y][x] != "#" :
                belief[y][x] = 1.0 / free_cells
    
    for row in belief : 
        print(row)

    return belief

belief = initialize_belief(makeTheGrid())
print(belief)
print(belief.sum())


# Assume we could only move with the command right, left, up, and down
def moveCommand(move, y, x): 
    if move == "up" :
        y = y - 1
    elif move == "down" :
        y = y + 1
    elif move == "left":
        x = x - 1
    elif move == "right":
        x = x + 1
    elif move == "stay" :
        y, x = y, x
    
    else:
        raise ValueError(f"Unknown move: {move}")
    
    return y, x

print(moveCommand("up", 1, 1))

# ccheck if the cell is valid or not
def isValidCell(grid, y, x) :
    height = len(grid)
    width = len(grid[0])

    if x >= width or x < 0 :
        return False
    if y >= height or y < 0 :
        return False
    if grid[y][x] == "#" :
        return False

    return True

# print(isValidCell(makeTheGrid(), 1, 2))

# Make the motion update, probability going to the intended direction is say 0.8
# 0.1 for staying, 0.1 for random 
def motionUpdate(grid, belief, command):
    height = len(grid)
    width = len(grid[0])

    newBelief = np.zeros((height, width))

    for y in range(height) : 
        for x in range(width) :

            if belief[y][x] == 0 :
                continue

            outcome = [
                (command, 0.8), # Intended to move this mf here
                ("stay", 0.1), # failed to move
                ("up", 0.025),
                ("down", 0.025),
                ("left", 0.025),
                ("right", 0.025),
            ]

            for move, moveProbability in outcome:
                new_y, new_x = moveCommand(move, y, x)
    
                if not isValidCell(grid, new_y, new_x) : # If it hits a wall or any other boundaries. stays
                    new_y , new_x = y, x
                
                newBelief[new_y][new_x] += belief[y][x] * moveProbability

    return(normalize(newBelief))

# if the robot were at y,x is there a door nearby?
def isDoorNearby(grid, y, x) :
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (0, 0),
    ]

    for dy, dx in directions :
        new_y = y + dy
        new_x = x + dx
    
        if isValidCell(grid, new_y, new_x):
            if(grid[new_y][new_x]) == "D" :
                return True 
    return False

# How much should i trust this cell after observing?
def sensorLikelihood(observation, y, x, grid):
    if observation == "isDoorNearby":
        if isDoorNearby(grid, y, x):
            return 0.9
        else:
            return 0.1
    
    elif observation == "noDoorNearby":
        if not isDoorNearby(grid, y, x):
            return 0.9
        else:
            return 0.1
    
    else :
        raise ValueError("Unknown observation!")
    
def sensorUpdate(grid, belief, observation):
    height = len(grid)
    width = len(grid[0])

    newBelief = np.zeros((height, width))

    for y in range(height):
        for x in range(width):
            if grid[y][x] == "#":
                continue
        
            likelihood = sensorLikelihood(observation, y, x, grid)
            newBelief[y][x] = belief[y][x] * likelihood
        
    return normalize(newBelief)



# Normalie to make it equal to one
def normalize(belief):
    total = belief.sum()

    return belief / total

# Add visualization using matplotlib
# color = probability
# D = door
# # = wall
# numbers = belief value
def showBelief(grid, belief, title, filename=None):
    plt.figure(figsize=(5, 5))
    plt.imshow(belief, cmap="viridis")
    plt.colorbar(label="Probability")
    plt.title(title)

    height = len(grid)
    width = len(grid[0])

    for y in range(height):
        for x in range(width):
            cell = grid[y][x]

            if cell == "#":
                plt.text(x, y, "#", ha="center", va="center", color="white", fontsize=16)
            elif cell == "D":
                plt.text(x, y, "D", ha="center", va="center", color="white", fontsize=16)

            plt.text(
                x,
                y + 0.25,
                f"{belief[y][x]:.2f}",
                ha="center",
                va="center",
                color="white",
                fontsize=8,
            )

    plt.xticks(range(width))
    plt.yticks(range(height))
    plt.grid(color="white", linewidth=0.5)

    if filename is not None:
        output_folder = "images"
        os.makedirs(output_folder, exist_ok=True)

        save_path = os.path.join(output_folder, filename)
        plt.savefig(save_path, bbox_inches="tight", dpi=150)
        print(f"Saved image: {save_path}")

    plt.show()
    plt.close()

# Experiment 1
def experiment1_sensor_only():
    print("===== Experiment 1: Sensor Update Only =====")

    grid = makeTheGrid()
    belief = initialize_belief(grid)

    print("Initial belief:")
    print(np.round(belief, 3))
    print("sum:", belief.sum())

    showBelief(grid, belief, "Experiment 1: After Sensor Update — Door Nearby", "experiment1_after_sensor.png")

    belief = sensorUpdate(grid, belief, "isDoorNearby")

    print("After observing: isDoorNearby")
    print(np.round(belief, 3))
    print("sum:", belief.sum())

    showBelief(grid, belief, "Experiment 1: After Sensor Update — Door Nearby")

#Experiment 2
def experiment2_motion_only():
    print("===== Experiment 2: Motion Update Only =====")

    grid = makeTheGrid()
    belief = initialize_belief(grid)

    showBelief(grid, belief, "Experiment 2: After Motion Update — Move Right", "experiment2_after_motion.png")

    belief = motionUpdate(grid, belief, "right")

    print("After command: right")
    print(np.round(belief, 3))
    print("sum:", belief.sum())

    showBelief(grid, belief, "Experiment 2: After Motion Update — Move Right")

# Experiment 3
def experiment3_filter_loop():
    print("===== Experiment 3: Full Bayes Filter Loop =====")

    grid = makeTheGrid()
    belief = initialize_belief(grid)

    showBelief(grid, belief, "Experiment 3: Initial Belief", "experiment3_initial.png")

    steps = [
        ("motion", "right"),
        ("sensor", "isDoorNearby"),
        ("motion", "down"),
        ("sensor", "noDoorNearby"),
        ("motion", "left"),
        ("sensor", "isDoorNearby"),
    ]

    for i, (step_type, value) in enumerate(steps, start=1):
        if step_type == "motion":
            belief = motionUpdate(grid, belief, value)
            title = f"Step {i}: Motion Update — {value}"

        elif step_type == "sensor":
            belief = sensorUpdate(grid, belief, value)
            title = f"Step {i}: Sensor Update — {value}"

        print(title)
        print(np.round(belief, 3))
        print("sum:", belief.sum())
        print()

        safe_title = title.lower().replace(" ", "_").replace("—", "-").replace(":", "")
        filename = f"experiment3_{i}_{safe_title}.png"
        showBelief(grid, belief, title, filename)
    
#Experiment 4
def experiment4_opposite_observations():
    print("===== Experiment 4: Opposite Sensor Observations =====")

    grid = makeTheGrid()

    belief1 = initialize_belief(grid)
    belief1 = sensorUpdate(grid, belief1, "isDoorNearby")
    showBelief(grid, belief1, "Experiment 4A: Observation — Door Nearby", "experiment4a_door_nearby.png")

    belief2 = initialize_belief(grid)
    belief2 = sensorUpdate(grid, belief2, "noDoorNearby")
    showBelief(grid, belief2, "Experiment 4B: Observation — No Door Nearby", "experiment4b_no_door_nearby.png")

    print("Belief after isDoorNearby:")
    print(np.round(belief1, 3))
    print()

    print("Belief after noDoorNearby:")
    print(np.round(belief2, 3))

#Experiment 5
def experiment5_boundary_behavior():
    print("===== Experiment 5: Boundary Behavior =====")

    grid = makeTheGrid()

    height = len(grid)
    width = len(grid[0])

    belief = np.zeros((height, width))
    belief[0][0] = 1.0

    showBelief(grid, belief, "Experiment 5: Start at Top-Left Corner", "experiment5_start_corner.png")

    belief = motionUpdate(grid, belief, "up")

    print("After command: up")
    print(np.round(belief, 3))
    print("sum:", belief.sum())

    showBelief(grid, belief, "Experiment 5: After Trying to Move Up", "experiment5_after_move_up.png")

if __name__ == "__main__":
    experiment1_sensor_only()
    experiment2_motion_only()
    experiment3_filter_loop()
    experiment4_opposite_observations()
    experiment5_boundary_behavior()