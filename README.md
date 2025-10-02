# DeePTB
Repository containing code to convert SIESTA outputs into DeePTB-compatible formats.

# Preparing SIESTA Data for DeePTB Training

We have explored how to convert data from **SIESTA** to train a **Deep Tight-Binding (DeePTB)** model. Using the scripts we developed, it is possible to automatically create the **input folder** containing all the files required by the model. This setup allows the model to start training with minimal manual intervention.

So far, we have successfully trained the model, but it only works with a **1S1P basis**, regardless of the material. For the elements we are studying, **Nitrogen (N) and Carbon (C)**, the expected basis would be **2s2p1d**, but the model does not accept this configuration even after modifying the `hidden irreps`. 

This limitation suggests that the current model implementation might not fully support more complex bases. To diagnose the issue, we would need to examine the **DFTIO data** provided by DeePTB to see if the model fails at any specific point during training or input processing. You can check an example input file [here](https://github.com/floatingCatty/dftio/blob/main/test/data/abacus/INPUT).

---
# SIESTA to DeePTB Workflow

```mermaid
flowchart TD
    A[SIESTA .fdf / basis.dat / pbc.dat] --> B[Data Processing Scripts]
    B --> C[Generate DeePTB Input Folder]
    C --> D[DeePTB Model Training]
    D --> E[Trained Hamiltonian / Predictions]

    %% Optional step for validation
    D --> F[Validate using DFTIO / Reference Data]


---


## About DeePTB

DeePTB is a **deep learning-based tight-binding package** designed to learn Hamiltonians and electronic properties directly from ab initio data. Key features include:

- **Automatic construction of input datasets** from DFT calculations (e.g., SIESTA `.fdf` files).  
- **Flexible model architectures** for electronic embedding, including support for `irreps_hidden` to encode orbital symmetries.  
- **Active learning integration**, allowing selection of the most informative data points to reduce computational cost.  
- **Efficient training** for large-scale atomic structures, with support for both CPU and GPU computation.  
- **Prediction of Hamiltonians** for super-large-scale systems, including defects, interfaces, and heterostructures.

For installation and quick start instructions, see the official DeePTB documentation [here](https://deeptb.readthedocs.io/en/latest/quick_start/easy_install.html).

While DeePTB provides a robust framework for training tight-binding models, it currently has limitations when dealing with bases larger than 1S1P. Investigating the DFTIO outputs may reveal the source of this limitation and guide adjustments to allow training with more complex bases like 2s2p1d.

---

## Next Steps

1. **Validate the input data** from SIESTA using the DeePTB DFTIO format.  
2. **Test the model** with more complex bases by comparing predictions against known Hamiltonians using first dftio data and after siesta  
4. **Document any failures or discrepancies** to guide future improvements in DeePTB training scripts.

