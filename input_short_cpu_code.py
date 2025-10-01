import json
from dptb.data import OrbitalMapper


dicts = []

# basis.dat file
with open("/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/basis.dat") as f:
    for line in f:
        line = line.strip()        
        if not line:               
            continue
        
        # Each line in basis.dat is a Python dictionary string
        # eval() converts the string into an actual dict
        d = eval(line)  
        dicts.append(d)            # Store the dict in the list

# Create an empty dict to merge everything into one
basis = {}
for d in dicts:
    basis.update(d)                # Merge each small dict into the main one


print("Combined basis:", basis)

# Create an OrbitalMapper using the merged basis
idp = OrbitalMapper(basis=basis)

# Get irreps_hidden representation from the basis
irreps_hidden = idp.get_irreps_ess()


print("irreps_hidden:", irreps_hidden)


