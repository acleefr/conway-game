import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the size of the grid
N = 100
# Define the initial state of the grid
grid = np.random.choice([0, 1], N*N, p=[0.2, 0.8]).reshape(N, N)

# Function to update the grid according to the rules of the game
def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Count the number of live neighbors
            total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                     grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                     grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                     grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])
            # Apply Conway's rules
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# Set up the animation
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, frames=100, fargs=(img, grid, N), interval=50, save_count=50)

plt.show()