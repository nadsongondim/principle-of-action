# Chapter 5 — Lagrangian, Hamiltonian and Phase Space

> This directory contains the runnable examples of Chapter 5 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_euler_lagrange_pendulum_sympy.py` — symbolically derives the Euler-Lagrange equation of the simple pendulum from L = T - V.
- `02_pendulum_full_lagrangian.py` — version from Example 1: Lagrangian with the zero of the potential at the point of suspension.
- `03_verlet_oscillator.py` — implements velocity-Verlet (symplectic) and forward Euler for the oscillator, and compares energy conservation.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_euler_lagrange_pendulum_sympy.py
    python 02_pendulum_full_lagrangian.py
    python 03_verlet_oscillator.py
