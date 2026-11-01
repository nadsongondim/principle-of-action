# Chapter 3 — Modeling, Validation and Reproducibility

> This directory contains the runnable examples of Chapter 3 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_train_test_split.py` — calibration/validation split with `train_test_split`, fitting the model on the calibration data only.
- `02_sensitivity_analysis.py` — sweeps a model parameter to assess the model's sensitivity to it.
- `03_reproducible_seed.py` — fixes the seed of NumPy's `default_rng` to obtain reproducible results.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_train_test_split.py
    python 02_sensitivity_analysis.py
    python 03_reproducible_seed.py
