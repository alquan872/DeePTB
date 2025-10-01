import numpy as np

# Define a range of values from 0 to 5
r = range(6)

# Initialize an empty list to store coordinates
coords = []

# Triple nested loop to generate grid points in 3D space
for x in r:
    for y in r:
        for z in r:
            # Each coordinate is normalized by dividing by 6
            coords.append([x/6, y/6, z/6])


coords = np.array(coords)


print(coords)


print("Total number of points:", len(coords))

np.save("/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/kpoints.npy", coords)
