# Chapter 2 — Essential numerical methods

> This directory contains the runnable examples of Chapter 2 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_quad_integration.py` — adaptive integration of a Gaussian with `scipy.integrate.quad`.
- `02_ode_solve_ivp_decay.py` — solves the ODE `dy/dt = -0.3 y` with SciPy's adaptive solver.
- `03_minimize_optimization.py` — finds the minimum of a parabola with `scipy.optimize.minimize`.
- `04_curve_fit_parameters.py` — fits the parameters of a decay model to synthetic data via `curve_fit`.
- `05_monte_carlo_uncertainty.py` — propagates uncertainty through the parameters and turns a point prediction into a range.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_quad_integration.py
    python 02_ode_solve_ivp_decay.py
    python 03_minimize_optimization.py
    python 04_curve_fit_parameters.py
    python 05_monte_carlo_uncertainty.py
