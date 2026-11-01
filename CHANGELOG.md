# Changelog

## v1.1 (2026-10-31) — English edition of the repository, synchronized with the corrected v1.1 of the book

First release of the English edition of the repository, which accompanies
the English edition of *Volume 4 — Unified Computational Modeling*. It is a
translation of the Portuguese repository
(https://github.com/nadsongondim/principle-of-action) at its v1.1, which is
already synchronized with the corrected v1.1 of the book (see below).

- Comments, docstrings, printed output, plot titles, labels and legends,
  error messages and READMEs translated into English. Where a code block
  appears in the English edition of the book, the same wording is used.
- Directories and `.py`/`.md` files renamed to English, keeping the
  numeric prefixes (`codigo/` → `code/`, `capNN_…` → `chNN_…`,
  `apendice_…` → `appendix_…`, `figuras/` → `figures/`, `docs/capas/` →
  `docs/covers/` with the covers of the English editions).
- **Variable, function, class and parameter names and dictionary keys
  were not changed** — they keep their Portuguese spelling, exactly as in
  the English edition of the book (e.g. `insulina`, `bergman`). Logic and
  numbers are identical to the Portuguese repository.
- Decimal commas in printed output and labels became decimal points.
- `figures/figures_volume4.py` — figure texts identical to those of the
  English edition of the book; images are saved to `figures/output/`.

### Inherited from the Portuguese repository v1.1 — code synchronized with the corrected v1.1 of the book

Code synchronized with the corrected errata of Volume 4 (v1.1 edition of the
book). Rule followed: the code's result prevails — parameters, formulas and
commented outputs were reconciled with the corrected text, and every changed
script was run and checked against the numbers quoted in the book. (File
names below are those of the English repository.)

#### Changed scripts

**Chapters**

- `ch02_numerical_methods/05_monte_carlo_uncertainty.py` — seed 42 and discarding k ≤ 0.
- `ch04_classical_mechanics/03_numerical_action_principle.py` — endpoints x(0)=1, x(π/2)=0; η = sin t · t(π/2 − t); prints S(±1) ≈ 0.323 and S(±0.5) ≈ 0.0807.
- `ch05_lagrangian_hamiltonian/01_euler_lagrange_pendulum_sympy.py`, `02_pendulum_full_lagrangian.py` — output comment in SymPy's literal form.
- `ch08_molecular_structure/03_water_minimization.py` — added the answer-key case (initial guess r0 from Appendix G): r_OH = 0.96000 Å, θ = 104.5075°.
- `ch09_reaction_paths/01_arrhenius_rate_ratio.py` — comment ratio ≈ 1.93.
- `ch10_enzyme_kinetics/01_michaelis_menten_full.py` — comment "rapid formation of ES".
- `ch10_enzyme_kinetics/02_mm_fit.py` — comment Vmax ≈ 1.01.
- `ch11_drug_receptor/01_kd_to_delta_g.py` — comment ΔG°(B) = −53.4 kJ/mol.
- `ch13_cardiovascular_respiratory/01_windkessel.py` — R, C = 1.3, 1.2.
- `ch13_cardiovascular_respiratory/02_isolated_systolic_hypertension.py` — R, C = 1.3, 1.2 / 1.3, 0.6; reading of the last two cycles; output 122/82/101 and 144/65/101.
- `ch14_renal_metabolic_endocrine/02_basic_bergman_model.py` — p1, p2, p3 = 0.005, 0.1, 0.00004; `insulina` as an argument of `bergman`.
- `ch14_renal_metabolic_endocrine/04_ogtt_normal_diabetic.py` — corrected model (basal secretion, Gb/Ib per scenario, SI = 0.5 in the diabetic, max_step = 1); prints peaks and G(120)/G(240).
- `ch15_neuro_immuno_infection/01_fitzhugh_nagumo.py` — rest y0 = [−1.1994, −0.6243], stimuli 0.60 × 1.20, `max_step = 0.05`; peaks ≈ −0.46 and ≈ +1.80.
- `ch15_neuro_immuno_infection/03_pkpd_antimicrobials.py` — T>MIC as `np.mean(C > MIC)`.
- `ch16_cancer_radiotherapy/02_detection_time.py` — comment t_det ≈ 2960 days.
- `ch17_bioimages_data/04_ct_volume_quantification.py` — segmentation `(img > -400) & roi`; synthetic volume with aerated lung, nodule and chest wall.
- `ch17_bioimages_data/05_deterioration_time_series.py` — `dados.last("24h")` (removed from pandas) replaced by a `Timedelta` filter.
- `ch18_quantitative_medicine_cases/01_hypertension_windkessel_treatment.py` — R_basal, C_basal = 1.5, 1.2; MAP as the mean over the steady-state cycle: ≈ 117 → ≈ 101 mmHg.
- `ch18_quantitative_medicine_cases/03_eqd2_three_regimens.py` — commented output 5×5.20 Gy: 32.9 / 42.6.
- `ch19_digital_twin/02_bayesian_update.py` — prior CL = 6.0 L/h; `atualizar(mu_prior, cov_prior, verossimilhanca, medidas, esquemas)`; V in L/kg × 70 kg, peak 1 h after the dose, 900 mg every 12 h: k ≈ 0.104 1/h, V ≈ 45 L (0.65 L/kg), CL ≈ 4.7 L/h.
- `ch20_data_interoperability/01_pydicom_basics.py` — generates a synthetic DICOM if `estudo/serie/slice_042.dcm` does not exist.
- `ch20_data_interoperability/02_longitudinal_labs.py` — fixes an `AttributeError` (`codigo_loinc`): uses a synthetic longitudinal table when `labs.csv` is not in the expected format.
- `ch20_data_interoperability/04_selection_bias.py` — `pd.cut(..., include_lowest=True)`.
- `ch22_usability_perspectives/01_hybrid_pk_model.py` — PK in amounts with an absorption compartment (A_tgi, A1, A2), `V1` returned by the learned layer, `C1 = A1 / V1`.

**Appendices**

- `appendix_b_scientific_python/01_numpy_basics.py` — `ints` → `seq`; comment "element-wise".
- `appendix_c_parameters/02_simulation_parameters.py` — k_b, k_θ in kcal; SVR in mmHg·s/mL; T>MIC target 40–70 %.
- `appendix_g_answer_keys/01_ch04_action_principle_lambdas.py` — interval [0, π/2]; S(0) = 0, S(±1) ≈ 0.323.
- `appendix_g_answer_keys/02_ch05_verlet_euler_compact.py` — prints the Verlet energy range (≈ h²/8) and Euler's E(20).
- `appendix_g_answer_keys/04_ch09_intermediate_b_accumulation.py` — B_max evaluated on a dense grid (0.0774 / 0.3679 / 0.7742).
- `appendix_g_answer_keys/05_ch10_network_normal_vs_knockout.py` — prints the peaks and the B values quoted in the answer key.
- `appendix_g_answer_keys/07_ch12_repeated_doses.py` — oral model (Bateman, ka = 1.5) instead of an IV bolus; peaks/troughs 2.18/0.83 and 1.74/1.17.
- `appendix_g_answer_keys/08_ch13_windkessel_stiffness.py` — Q(t) from section 13.1, R = 1.3, C = 1.2/0.6; output 122 82 40 101 / 144 65 79 101.
- `appendix_g_answer_keys/09_ch14_glucose_insulin_two_scenarios.py` — model of Example 2 of ch. 14.
- `appendix_g_answer_keys/10_ch15_fn_pulse_sweep.py` — rest state, `max_step`, sweep over [0.30, 1.20]; threshold 0.61 (bisection 0.6065).
- `appendix_g_answer_keys/13_ch18_diabetes_three_scenarios.py` — model of ch. 14 with three meals and `dur`; peaks 16.5 / 14.2 / 9.8 mmol/L.
- `appendix_g_answer_keys/14_ch19_monte_carlo_hba1c.py` — prints medians, band and P(H ≤ 7 %).
- `appendix_g_answer_keys/16_ch22_hybrid_renal_model.py` — `avaliar` pipeline with the trend in mL/min/1.73 m²/year and a KDIGO alert (decline > 5/year).

**Figures and tests**

- `figures/figures_volume4.py` — aligned with the corrected version of the book (figures 13, 14, 19, 21 and 22; also the labels of figure 8 and the target of figure 19).
- `tests/test_smoke.py` — `PYTHONUTF8=1` and `PYTHONIOENCODING=utf-8` in the subprocess environment and output read as UTF-8 (Windows cp1252 console).
