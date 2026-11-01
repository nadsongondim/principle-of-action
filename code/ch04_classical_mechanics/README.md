# Chapter 4 — Computational Classical Mechanics

> This directory contains the runnable examples of Chapter 4 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_harmonic_oscillator.py` — integrates the harmonic oscillator with `solve_ivp` and plots the trajectory x(t) and the phase portrait.
- `02_oscillator_energy.py` — checks the oscillator's energy conservation with tight tolerances.
- `03_numerical_action_principle.py` — numerical experiment on the Principle of Action: S(s) has its minimum exactly on the physical trajectory.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_harmonic_oscillator.py
    python 02_oscillator_energy.py
    python 03_numerical_action_principle.py
