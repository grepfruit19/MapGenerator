import random
from PIL import Image

#Current state: Creates seeds and islands well. It might be a little "too" random
#I might want to change it, but eh, we'll see.
#Future plans: Larger scale, create rivers, create image map output (color to number)
#friendlier user interface


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
#Output: Returns given grid with random numbers
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
#Processing: Adds 'isle' number of 1s to the map
#Output: Existing grid with seeds added
def seed_map(grid,dim,isles,coords,seed = None):
    if seed is None:
        random.seed()
    else:
        random.seed(seed)
    for i in range(0,isles):
        x = random.randint(0,dim-1)
        y = random.randint(0,dim-1)
        grid[x][y] = 1
        coords.append([x,y])

#Driver for grow_seeds.
def grow_seeds_wrapper(grid,dim,isles,coords,prob, seed = None):
    if seed is None:
        random.seed()
    else:
        random.seed(seed)
    for i, each in enumerate(coords):
        x = coords[i][0]
        y = coords[i][1]
        grow_seeds(grid,dim,x,y,prob)

#Recursive function to grow seeds. Given a probability, it rolls to see if the
#seed should grow in a given direction.
def grow_seeds(grid, dim, x, y, prob):
    if grid[x][y] is 0:
        grid[x][y] = 1
    if (random.uniform(0,1.0) > prob): #This line gives the inverse probability
        try:
            if grid[x+1][y] is 0: #Skips some extra processing
                grow_seeds(grid,dim,x+1,y,prob)
        except IndexError:
            pass #Important to avoid out of bounds errors
    if (random.uniform(0,1.0) > prob):
        try:
            if grid[x][y+1] is 0:
                grow_seeds(grid,dim,x,y+1,prob)
        except IndexError:
            pass
    if (random.uniform(0,1.0) > prob):
        try:
            if grid[x][y-1] is 0:
                grow_seeds(grid,dim,x,y-1,prob)
        except IndexError:
            pass
    if (random.uniform(0,1.0) > prob):
        try:
            if grid[x-1][y] is 0:
                grow_seeds(grid,dim,x-1,y,prob)
        except IndexError:
            pass

def create_image(grid,dim):
    layout = Image.new("RGB", (dim,dim), (0,0,255))
    for row in range(0,dim):
        for col in range(0,dim):
            if grid[row][col] is 1:
                layout.putpixel((row,col), (255,0,0))
    layout.save("map.jpeg")
    return layout

#Some default values
dimension = 100
tile_range = 1
provided_seed = 182
number_of_seeds = 3
#This probability is inverse, so a low number (such as .01) means a high rate of
#growth. Requires some fiddling, because input numbers are not necessarily
#intuitive.
probability = .5

#stores locations of seeds
seedlocs = []

grid = create_grid(dimension)
seed_map(grid,dimension,number_of_seeds,seedlocs)
grow_seeds_wrapper(grid,dimension,number_of_seeds,seedlocs,probability)
print_grid(dimension)
image = create_image(grid,dimension)
