import sisl

# Load the SIESTA input file (.fdf)
fdf_sile = sisl.get_sile("/home/alba_quinones/0076-0be5-4d12-9c72-26f8ec9bbaca/aiida.fdf")

# Extract the AtomicCoordinatesAndAtomicSpecies block from the .fdf file
coords_block = fdf_sile.get("AtomicCoordinatesAndAtomicSpecies")

# New file to write atomic positions
with open("/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/positions.dat", "w") as fout:

    for line in coords_block:
        parts = line.split()          # Split the line into individual items
        
        x, y, z = map(float, parts[0:3])
        
        # Write the coordinates to positions.dat with 18 decimal places in scientific notation
        fout.write(f"{x:.18e} {y:.18e} {z:.18e}\n")
