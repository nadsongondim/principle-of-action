# Chapter 8 — Molecular structure and potential energy

> This directory contains the runnable examples of Chapter 8 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_molecule_representation.py` — minimal representation of the water molecule (positions, elements, bonds).
- `02_molecular_geometry.py` — the `distancia` (distance) and `angulo` (angle) functions applied to water.
- `03_water_minimization.py` — minimizes the energy of water with L-BFGS-B, starting from a misaligned initial guess.
- `04_generic_minimization.py` — generic minimization skeleton with the gradient passed to `minimize`.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_molecule_representation.py
    python 02_molecular_geometry.py
    python 03_water_minimization.py
    python 04_generic_minimization.py
