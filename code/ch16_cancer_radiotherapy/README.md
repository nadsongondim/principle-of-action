# Chapter 16 — Cancer, targeted therapies and radiotherapy

> This directory contains the runnable examples for Chapter 16 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the root of the repository.

## Contents

- `01_gompertz.py` — tumor growth with the Gompertz model using `solve_ivp`.
- `02_detection_time.py` — calculates how many days separate an initial cell from detection by imaging.
- `03_eqd2_radiotherapy.py` — calculates EQD2 for two regimens (conventional vs. hypofractionated) in tumor and late-responding tissue.
- `04_lq_model.py` — cell survival curves of the linear-quadratic model for tumor and late-responding tissue.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_gompertz.py
    python 02_detection_time.py
    python 03_eqd2_radiotherapy.py
    python 04_lq_model.py
