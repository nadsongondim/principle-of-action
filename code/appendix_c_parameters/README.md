# Appendix C — Tables of Physical, Chemical and Physiological Parameters

> This directory contains the teaching parameters used by the simulations of Volume 4 of the series
> *The Principle of Action*, coded as Python dictionaries for reuse.

**Teaching-value notice.** The parameters listed here are typical values,
chosen for the purpose of reproducible simulation in this volume. In a real
patient, a real clinical study or a real laboratory, the values vary widely and
must be obtained from the appropriate sources (peer-reviewed literature, current
guidelines, the patient's own data). These parameters are not an individual
recommendation of dose, of management or of clinical modeling.

## Contents

- `01_physical_constants.py` — universal physical constants (c, h, kB, R, NA, etc.).
- `02_simulation_parameters.py` — typical parameters of the simulations of chapters 4–16, organized by group.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_physical_constants.py
    python 02_simulation_parameters.py
