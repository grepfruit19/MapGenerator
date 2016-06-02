import random

#Land generation: Create two seeds

#Generates an nxn grid
def create_grid(n):
    grid = [[0 for i in range(0,n)] for j in range(0,n)]
    return grid

#Prints grid
def print_grid(n):
    for row in range(0,n):
        print(grid[row])

#Input: Grid, dimensions, range for generation, seed for RNG
#Processing: Adds random numbers to existing grid
#Output: 
def randomize_grid(grid,dim,bound,seed = None):
    if seed is None:
        seed = 182
    random.seed(seed)
    for row in range(0,dim):
        for col in range(0,dim):
            grid[row][col] = random.randint(0,bound)

#Input: Grid (map), dim - dimensions of grid
#isles: Number of seeds to be inserted
#seed: number used for RNG
def seed_map(grid,dim,isles,coords,seed = None):
    if seed is None:
        seed = 182
    random.seed(seed)
    for i in range(0,isles):
        x = random.randint(0,dim-1)
        y = random.randint(0,dim-1)
        grid[x][y] = 1
        coords.append([x,y])


def grow_seeds(grid,dim,isles)

dimension = 10
tile_range = 1
provided_seed = 182

seedlocs = []

grid = create_grid(dimension)
seed_map(grid,dimension,3,seedlocs,provided_seed)
print_grid(dimension)
