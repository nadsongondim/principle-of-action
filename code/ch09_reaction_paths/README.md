# Chapter 9 — Reaction pathways, free energy and kinetics

> This directory contains the runnable examples of Chapter 9 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_arrhenius_rate_ratio.py` — computes the ratio between rates at two temperatures via Arrhenius (the Q10 rule).
- `02_coupled_reactions.py` — simulates the A -> B -> C network with `solve_ivp` and shows the peak of the intermediate B.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_arrhenius_rate_ratio.py
    python 02_coupled_reactions.py
