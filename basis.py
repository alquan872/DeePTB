import sisl
import numpy as np


# Load geometry from an FDF input file (SIESTA / AiiDA format)
fdf_sile = sisl.get_sile("/home/alba_quinones/0076-0be5-4d12-9c72-26f8ec9bbaca/aiida.fdf")
geom = fdf_sile.read_geometry()

# -------------------------------------------------------------------
# Print the total number of atoms in the structure
# -------------------------------------------------------------------
print("Num de átomos:", geom.na)

# -------------------------------------------------------------------
# Collect unique atomic symbols present in the geometry
# -------------------------------------------------------------------
symbols = []
for atom in geom.atoms:
    if atom.symbol not in symbols:
        symbols.append(atom.symbol)

# -------------------------------------------------------------------
# Write a basis set definition for each unique element
# -------------------------------------------------------------------
# The output is saved as a .dat file, one line per element, in the format:
# {'Element': '2s2p1d'} You have to choose the basis that you need!!!!!
output_file = "/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/basis.dat"
with open(output_file, "w") as f:
    for sym in symbols:
        f.write(f"{{'{sym}': '2s2p1d'}}\n")
