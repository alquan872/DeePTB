with open("/home/alba_quinones/DeePTB/examples2/e3/data/NC64.0/pbc.dat", "w") as f:
    for _ in range(3):
        # Write three identical lines into the file
        # Each line contains the floating-point number 1.0 with 18 decimal places.
        f.write(f"{1.0:.18e}\n")

