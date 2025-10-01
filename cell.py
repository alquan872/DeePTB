import sisl
import numpy as np


# Load geometry from an FDF input file (SIESTA / AiiDA format)
fdf_sile = sisl.get_sile("/home/alba_quinones/0076-0be5-4d12-9c72-26f8ec9bbaca/aiida.fdf")
geom = fdf_sile.read_geometry()

# -------------------------------------------------------------------
# Extract the cell (lattice vectors of the simulation box)
# -------------------------------------------------------------------
cell = geom.cell

# Print the cell matrix to the terminal
print("Cell:")
print(cell)

# -------------------------------------------------------------------
# Save the cell matrix into a .dat file
# -------------------------------------------------------------------
# Each row corresponds to a lattice vector
# Values are written in scientific notation with 18 decimal places
output_file = "/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/cell.dat"
with open(output_file, "w") as f:
    for row in cell:
        f.write(" ".join([f"{val:.18e}" for val in row]) + "\n")



