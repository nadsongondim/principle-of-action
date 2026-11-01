"""
Parameters of physical, molecular, enzymatic and pharmacological simulations.

Appendix C: Tables of Physical, Chemical and Physiological Parameters — Volume 4
of "The Principle of Action" (Nadson Brito Gondim).

Teaching-value notice: the parameters listed are typical values, chosen for
the purpose of reproducible simulation in this volume; they are not a clinical
recommendation and do not replace primary sources.

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations


# C.2 — Parameters of physical simulations (chs. 4–7)
PARAMETROS_FISICA = {
    "oscilador_harmonico_omega": 1.0,                     # rad/s (normalized)
    "amortecido_gamma_sub":      0.2,
    "pendulo_L_m":               1.0,
    "pendulo_g":                 9.81,
    "kepler_a_ua":               1.0,
    "kepler_T_ano":              1.0,
    "onda_1d_c":                 1.0,
    "onda_1d_CFL_max":           1.0,
}


# C.3 — Molecular and chemical parameters (chs. 8–9)
PARAMETROS_MOLECULAR = {
    "OH_r0_A":                   0.96,
    "OH_kb_kcal_per_mol_A2":     1000.0,   # SPC/Fw (Wu, Tepper & Voth 2006)
    "HOH_theta0_deg":            104.5,
    "HOH_ktheta_kcal_per_mol_rad2": 75.0,
    "LJ_CC_sigma_A":             3.5,
    "LJ_CC_epsilon_kJ_per_mol":  0.4,
    "Ea_tipica_kJ_per_mol_min":  40.0,
    "Ea_tipica_kJ_per_mol_max":  80.0,
    "A_arrhenius_min":           1e10,
    "A_arrhenius_max":           1e14,
}


# C.4 — Enzyme kinetics (ch. 10)
PARAMETROS_ENZIMATICA = {
    "hexoquinase_Km_mM":         0.1,
    "glicoquinase_Km_mM":        10.0,
    "hemoglobina_n_hill":        2.8,
    "hemoglobina_P50_mmHg":      26.0,
    "AChE_kcat_per_s":           1e4,
}


# C.5 — Pharmacological (chs. 11–12)
PARAMETROS_FARMACO = {
    "Kd_alta_afinidade_nM_min":  1.0,
    "Kd_alta_afinidade_nM_max":  100.0,
    "Vd_hidrofilico_L_per_kg_min": 0.3,
    "Vd_hidrofilico_L_per_kg_max": 0.5,
    "Vd_lipofilico_L_per_kg_min":  1.0,
    "Vd_lipofilico_L_per_kg_max":  20.0,
    "F_oral_min":                  0.1,
    "F_oral_max":                  1.0,
}


# C.6 — Hemodynamic and ventilatory (ch. 13)
PARAMETROS_HEMODINAMICOS = {
    "VS_mL":                     70.0,
    "DC_L_per_min":              5.0,
    "MAP_normal_mmHg_min":       70.0,
    "MAP_normal_mmHg_max":       100.0,
    "pressao_pulso_mmHg":        40.0,
    "C_arterial_mL_per_mmHg":    1.5,
    "RVS_mmHg_s_per_mL":         1.0,      # ≈ 17 mmHg·min/L (Wood units)
    "C_pulm_normal_L_per_cmH2O": 0.1,
    "C_pulm_SDRA_min":           0.03,
    "C_pulm_SDRA_max":           0.05,
    "R_vias_min_cmH2O_per_Ls":   1.0,
    "R_vias_max_cmH2O_per_Ls":   3.0,
}


# C.7 — Renal, metabolic and endocrine (ch. 14)
PARAMETROS_RENAL_METABOLICO = {
    "TFG_normal_mL_per_min":     90.0,
    "creatinina_serica_min":     0.7,
    "creatinina_serica_max":     1.2,
    "glicemia_jejum_min":        70.0,
    "glicemia_jejum_max":        99.0,
    "HbA1c_normal_pct_max":      5.7,
    "HbA1c_diabetes_pct_min":    6.5,
    "Na_min":                    135.0,
    "Na_max":                    145.0,
    "osmolaridade_min":          285.0,
    "osmolaridade_max":          295.0,
    "pH_arterial_min":            7.35,
    "pH_arterial_max":            7.45,
    "HCO3_min":                  22.0,
    "HCO3_max":                  26.0,
    "PaCO2_min":                 35.0,
    "PaCO2_max":                 45.0,
}


# C.8 — Neurophysiological and infection (ch. 15)
PARAMETROS_NEURO_INFECCAO = {
    "FN_a":                       0.7,
    "FN_b":                       0.8,
    "FN_eps":                     0.08,
    "duplicacao_bacteriana_min":  20,
    "duplicacao_bacteriana_max":  60,
    "MIC_ceftriaxona_min":        0.5,
    "MIC_ceftriaxona_max":        1.0,
    "T_above_MIC_objetivo_min":   0.4,     # beta-lactams: 40–70 % depending on
    "T_above_MIC_objetivo_max":   0.7,     # the class; higher targets in critically ill patients
    "Cmax_per_MIC_objetivo_min":  8.0,
}


# C.9 — Oncology and radiotherapy (ch. 16)
PARAMETROS_ONCOLOGIA = {
    "Td_tumor_dias_min":         30,
    "Td_tumor_dias_max":         300,
    "K_capacidade_celulas":      1e12,
    "ab_tumor_agudo_Gy":         10.0,
    "ab_tardio_Gy_min":          2.0,
    "ab_tardio_Gy_max":          5.0,
    "RT_mama_convencional_Gy":   50.0,
    "RT_mama_convencional_fr":   25,
    "RT_mama_hipo_Gy_min":       40.0,
    "RT_mama_hipo_Gy_max":       42.5,
    "RT_mama_hipo_fr_min":       15,
    "RT_mama_hipo_fr_max":       16,
}


def main() -> None:
    grupos = {
        "Physics":            PARAMETROS_FISICA,
        "Molecular":          PARAMETROS_MOLECULAR,
        "Enzymatic":          PARAMETROS_ENZIMATICA,
        "Pharmacological":    PARAMETROS_FARMACO,
        "Hemodynamic":        PARAMETROS_HEMODINAMICOS,
        "Renal/Metabolic":    PARAMETROS_RENAL_METABOLICO,
        "Neuro/Infection":    PARAMETROS_NEURO_INFECCAO,
        "Oncology":           PARAMETROS_ONCOLOGIA,
    }
    for nome, tabela in grupos.items():
        print(f"\n[{nome}]")
        for chave, valor in tabela.items():
            print(f"  {chave} = {valor}")


if __name__ == "__main__":
    main()
