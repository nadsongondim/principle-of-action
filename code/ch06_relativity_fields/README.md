# Chapter 6 — Relativity, fields and electromagnetism

> This directory contains the runnable examples of Chapter 6 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_lorentz_transformation.py` — applies the Lorentz matrix to an event and checks the invariance of the interval s².
- `02_relativistic_dynamics.py` — integrates `dp/dt = F` and compares `v_rel(t)` with `v_classical(t)`.
- `03_time_dilation.py` — computes the time measured on Earth for a five-year trip at `v = 0.8 c`.
- `04_laplace_relaxation.py` — solves 2D Laplace by iterative Jacobi relaxation with Dirichlet conditions.
- `05_fdtd_maxwell_1d.py` — 1D FDTD on the Yee grid, with a Gaussian pulse and CFL = 0.5.
- `06_sor_relaxation.py` — solves the same 2D Laplace problem by SOR and compares the iteration count with Gauss-Seidel (ω = 1).

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_lorentz_transformation.py
    python 02_relativistic_dynamics.py
    python 03_time_dilation.py
    python 04_laplace_relaxation.py
    python 05_fdtd_maxwell_1d.py
    python 06_sor_relaxation.py
