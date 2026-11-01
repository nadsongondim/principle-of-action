# Chapter 10 — Enzyme kinetics and biochemical networks

> This directory contains the runnable examples of Chapter 10 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_michaelis_menten_full.py` — integrates the full kinetic system S, ES, P without the steady-state approximation.
- `02_mm_fit.py` — fits V_max and K_m to seven experimental points with `curve_fit`.
- `03_network_knockout_e2.py` — simulates the A -> B -> C network with MM kinetics and a partial knockout of E2.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_michaelis_menten_full.py
    python 02_mm_fit.py
    python 03_network_knockout_e2.py
