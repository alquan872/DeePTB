import h5py
import sisl
import numpy as np


# Load Hamiltonian from a SIESTA HSX file
H_sile = sisl.get_sile("/home/alba_quinones/0076-0be5-4d12-9c72-26f8ec9bbaca/aiida.HSX")
H = H_sile.read_hamiltonian()

# Convert Hamiltonian to sparse COO matrix
H_matrix = H.tocsr().tocoo()


Natoms = H.geometry.na         # number of atoms
Norb = H.geometry.no           # total number of orbitals
orbs_per_atom = int(Norb / Natoms)  # assume same number per atom
print("Orbitals per atom:", orbs_per_atom)

# -------------------------------------------------------------------
# Build a dictionary of Hamiltonian blocks
# Key format: (Rx, Ry, Rz, atom_i, atom_j)
# Each block is an orbs_per_atom x orbs_per_atom matrix
# -------------------------------------------------------------------
blocks = {}

for i, j, val in zip(H_matrix.row, H_matrix.col, H_matrix.data):
    atom_i = H.geometry.o2a(i)  # atom index of orbital i
    atom_j = H.geometry.o2a(j)  # atom index of orbital j

    # Orbital index within each atom
    orb_i = i - atom_i * orbs_per_atom
    orb_j = j - atom_j * orbs_per_atom

    # Get lattice cell (Rx, Ry, Rz)
    Rx, Ry, Rz = H.geometry.o2isc(j)

    # Key identifies the block by atoms and cell
    key = (Rx, Ry, Rz, atom_i, atom_j % Natoms)

   
    if key not in blocks:
        blocks[key] = np.zeros((orbs_per_atom, orbs_per_atom), dtype=np.float32)

    
    blocks[key][orb_i, orb_j] = val


# Save Hamiltonian blocks into an HDF5 file
out_path = "/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/hamiltonians.h5"
with h5py.File(out_path, "w") as f:
    group0 = f.create_group("0")
    for (Rx, Ry, Rz, ai, aj), mat in blocks.items():
        key_name = f"{ai}_{aj}_{Rx}_{Ry}_{Rz}"
        group0.create_dataset(key_name, data=mat)


# Checks
datos = []
for (Rx, Ry, Rz, ai, aj), mat in blocks.items():
    datos.append([Rx, Ry, Rz, ai, aj, mat])

print(f"Number of blocks: {len(datos)}")
print("Example block:")
print("Matrix:\n", datos[10777][5])
print("Atoms:", datos[10777][3], datos[10777][4])
print("Translation:", datos[10777][0], datos[10777][1], datos[10777][2])
print("Min Ry:", min(d[1] for d in datos))
print("Min Rz:", min(d[2] for d in datos))


for i, j, val in zip(H_matrix.row[-100:], H_matrix.col[-100:], H_matrix.data[-100:]):
    print(f"H_matrix[{i}, {j}] = {val}")
