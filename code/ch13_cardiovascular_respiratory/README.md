# Chapter 13 — Cardiovascular and respiratory systems

> This directory contains the runnable examples of Chapter 13 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the repository root.

## Contents

- `01_windkessel.py` — arterial Windkessel model integrated with `solve_ivp`.
- `02_isolated_systolic_hypertension.py` — compares the pressure curve of a normal subject vs an elderly subject with reduced compliance.
- `03_ventilatory_mechanics.py` — pulmonary RC ODE with a periodic driving pressure.
- `04_plateau_pressure_ards.py` — compares V_T of 10 mL/kg and 6 mL/kg in terms of plateau pressure.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_windkessel.py
    python 02_isolated_systolic_hypertension.py
    python 03_ventilatory_mechanics.py
    python 04_plateau_pressure_ards.py
