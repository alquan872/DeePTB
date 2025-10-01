import sisl
import numpy as np

# get_sile opens the file and automatically detects its format (.fdf here)
fdf_sile = sisl.get_sile("/home/alba_quinones/0076-0be5-4d12-9c72-26f8ec9bbaca/aiida.fdf")
# read_geometry extracts the atomic structure (positions, elements, etc.)
geom = fdf_sile.read_geometry()   

# -------------------------------------------------------------------
# Print basic information about the structure
# -------------------------------------------------------------------
print("Number of atoms:", geom.na)

# -------------------------------------------------------------------
# Write atomic numbers of all atoms to a .dat file
# -------------------------------------------------------------------
# One atomic number per line, plain text format
output_file = "/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/atomic_numbers.dat"
with open(output_file, "w") as f:
    for atom in geom.atoms:
        f.write(f"{atom.Z}\n")  # atom.Z returns the atomic number
