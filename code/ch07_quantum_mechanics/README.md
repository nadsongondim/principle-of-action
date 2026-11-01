# Chapter 7 — Computational quantum mechanics

> This directory contains the runnable examples of Chapter 7 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_discrete_hamiltonian.py` — assembles the sparse tridiagonal matrix of the 1D Hamiltonian with finite differences.
- `02_infinite_well.py` — diagonalizes the infinite well with `eigsh` and compares with the formula `E_n = n² π² / 2`.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_discrete_hamiltonian.py
    python 02_infinite_well.py
