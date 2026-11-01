# Chapter 12 — Computational pharmacokinetics and pharmacodynamics

> This directory contains the runnable examples of Chapter 12 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_oral_absorption_bateman.py` — linear two-compartment model (gut + plasma) integrated with `solve_ivp`.
- `02_dose_interval_css.py` — uses the identity `C_ss = F·D / (τ·CL)` to compute the target dose.
- `03_renal_adjustment.py` — adjusts the dose for a patient with reduced renal function.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_oral_absorption_bateman.py
    python 02_dose_interval_css.py
    python 03_renal_adjustment.py
