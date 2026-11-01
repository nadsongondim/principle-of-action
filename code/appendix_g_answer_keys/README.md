# Appendix G — Answer Key to the Challenge Exercises

> This directory contains the runnable examples of the answer keys in Appendix G of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the root of the repository.

## Contents

- `01_ch04_action_principle_lambdas.py` — compact version of the action experiment on the oscillator.
- `02_ch05_verlet_euler_compact.py` — explicit Euler and velocity Verlet steps on the oscillator.
- `03_ch07_infinite_well_convergence.py` — O(dx²) convergence of the eigenvalues of the infinite well.
- `04_ch09_intermediate_b_accumulation.py` — sweeps k1/k2 and measures the peak of B in A→B→C (dense grid).
- `05_ch10_network_normal_vs_knockout.py` — side-by-side panels of the cascaded MM network, normal × knockout.
- `06_ch11_antagonist_family.py` — family of dose-response curves with three values of `[I]`.
- `07_ch12_repeated_doses.py` — `C(t)` under repeated oral doses (sum of Bateman curves), two regimens with the same `C_ss`.
- `08_ch13_windkessel_stiffness.py` — Windkessel comparing normal × stiff compliance.
- `09_ch14_glucose_insulin_two_scenarios.py` — normal × diabetic OGTT in two panels.
- `10_ch15_fn_pulse_sweep.py` — sweep of the pulse amplitude in the FN model to identify the threshold.
- `11_ch16_eqd2_three_regimens.py` — EQD2 of the three regimens (conventional, hypofractionated, SBRT).
- `12_ch17_gompertz_volume_fit.py` — fits the Gompertz `r` to simulated CT volumes.
- `13_ch18_diabetes_three_scenarios.py` — three blood glucose scenarios over 24 h.
- `14_ch19_monte_carlo_hba1c.py` — Monte Carlo of the HbA1c trajectory in two scenarios.
- `15_ch20_index_dicom_folder.py` — function `indexar_pasta_dicom` that builds a DataFrame of metadata.
- `16_ch22_hybrid_renal_model.py` — skeleton of a hybrid CKD-EPI + learned-layer model, with a KDIGO alert (decline > 5 mL/min/1.73 m²/year).

## How to run

Install the requirements (see `requirements.txt` at the root) and run any of the examples:

    python 01_ch04_action_principle_lambdas.py
    python 02_ch05_verlet_euler_compact.py
    ...
