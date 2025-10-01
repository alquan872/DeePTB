import h5py
import sisl
import numpy as np

# Load Overlaps from a SIESTA HSX file
S_sile = sisl.get_sile("/home/alba_quinones/0076-0be5-4d12-9c72-26f8ec9bbaca/aiida.HSX")

# Convert Overlaps to sparse COO matrix
S = S_sile.read_overlap()  

S_matrix = S.tocsr().tocoo()
Natoms = S.geometry.na          # number of atoms
Norb = S.geometry.no            # total number of orbitals
orbs_per_atom = int(Norb/Natoms)  # assume same number per atom
print(orbs_per_atom)

# -------------------------------------------------------------------
# Build a dictionary of Overlaps blocks
# Key format: (Rx, Ry, Rz, atom_i, atom_j)
# Each block is an orbs_per_atom x orbs_per_atom matrix
# -------------------------------------------------------------------

blocks = {}

for i, j, val in zip(S_matrix.row, S_matrix.col, S_matrix.data):
    atom_i = S.geometry.o2a(i)  # atom index of orbital i
    atom_j = S.geometry.o2a(j)  # atom index of orbital j


    # Orbital index within each atom
    orb_i = i - atom_i * orbs_per_atom
    orb_j = j - atom_j * orbs_per_atom

    

    # Get lattice cell (Rx, Ry, Rz)
    Rx, Ry, Rz = S.geometry.o2isc(j)
    # Key identifies the block by atoms and cell
    key = (Rx, Ry, Rz, atom_i, (atom_j % Natoms))

    if key not in blocks:
        blocks[key] = np.zeros((orbs_per_atom, orbs_per_atom), dtype=np.float32)

    blocks[key][orb_i, orb_j] = val


# Save Overlaps blocks into an HDF5 file
out_path = "/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/overlaps.h5"
with h5py.File(out_path, "w") as f:
    grupo0 = f.create_group("0")

    for (Rx, Ry, Rz, ai, aj), mat in blocks.items():
        key_name = f"{ai}_{aj}_{Rx}_{Ry}_{Rz}"
        grupo0.create_dataset(key_name, data=mat)

datos = []
for (Rx, Ry, Rz, ai, aj), mat in blocks.items():
    datos.append([Rx, Ry, Rz, ai, aj, mat])

print(f"Bloques: {len(datos)}")

