"""
Answer key Ch. 22 — Ex. 6 (Challenge): hybrid model of renal function.

Mechanistic skeleton (CKD-EPI 2021 without race adjustment + clearance proportional
to GFR) coupled to a learned layer that fits residuals from demographic
covariates and the temporal pattern of creatinine.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


CL_NR = 0.5        # L/h — non-renal fraction (didactic)
CL_R = 4.5         # L/h — renal fraction at normal GFR (didactic)


@dataclass
class Paciente:
    idade: float
    peso: float
    imc: float
    sexo_F: int
    creat_atual: float
    creat_delta_7d: float
    medicamentos_nefro: int
    diabetes: int
    hipertensao: int
    sexo: str = "M"


class ModeloCorrecaoStub:
    """Teaching placeholder — replace with a model trained on an external cohort."""

    def predict(self, x: np.ndarray) -> np.ndarray:
        # residual correction proportional to the creatinine delta
        delta_creat = x[0, 5]
        return np.array([-15.0 * delta_creat])


modelo_correcao = ModeloCorrecaoStub()


# --- Mechanistic skeleton ---
def tfg_prior_ckd_epi(creat: float, idade: float, sexo: str,
                      raca: str | None = None) -> float:
    """CKD-EPI 2021 (no race adjustment): returns eGFR in mL/min/1.73m²."""
    kappa = 0.7 if sexo == 'F' else 0.9
    alfa = -0.241 if sexo == 'F' else -0.302
    f_sexo = 1.012 if sexo == 'F' else 1.0
    r = creat / kappa
    return 142 * min(r, 1)**alfa * max(r, 1)**(-1.200) \
        * 0.9938**idade * f_sexo


def clearance_mecanistico(tfg: float, fr_renal: float) -> float:
    """Total CL = non-renal CL + fr_renal * (GFR/normal GFR) * renal CL."""
    return CL_NR + fr_renal * (tfg / 100.0) * CL_R


# --- Learned layer: corrections for covariates and dynamics ---
def features(paciente: Paciente) -> np.ndarray:
    return np.array([
        paciente.idade, paciente.peso, paciente.imc,
        paciente.sexo_F,
        paciente.creat_atual, paciente.creat_delta_7d,
        paciente.medicamentos_nefro,
        paciente.diabetes, paciente.hipertensao,
    ])


def tfg_hibrida(paciente: Paciente) -> float:
    prior = tfg_prior_ckd_epi(paciente.creat_atual, paciente.idade,
                              paciente.sexo)
    delta = modelo_correcao.predict(features(paciente).reshape(1, -1))[0]
    return float(prior + delta)


# --- Monitoring pipeline ---
@dataclass
class Historico:
    datas: np.ndarray          # time of each test, in years
    tfg_estimada: np.ndarray   # mL/min/1.73m²


@dataclass
class Regressao:
    slope: float
    intercept: float


def regressao_linear(y: np.ndarray, x: np.ndarray) -> Regressao:
    slope, intercept = np.polyfit(x, y, 1)
    return Regressao(float(slope), float(intercept))


def avaliar(paciente: Paciente, historico: Historico) -> tuple[float, float, bool]:
    tfg_pontual = tfg_hibrida(paciente)
    tendencia = regressao_linear(historico.tfg_estimada,
                                 historico.datas).slope  # mL/min/1.73m²/year
    alerta = tfg_pontual < 60 or tendencia < -5          # KDIGO: decline > 5/year
    return tfg_pontual, tendencia, alerta


def main() -> None:
    paciente = Paciente(idade=68, peso=72, imc=27, sexo_F=1,
                        creat_atual=1.4, creat_delta_7d=0.2,
                        medicamentos_nefro=1, diabetes=1, hipertensao=1,
                        sexo='F')
    tfg = tfg_hibrida(paciente)
    cl = clearance_mecanistico(tfg, fr_renal=0.8)
    print(f"estimated GFR (hybrid) = {tfg:.1f} mL/min/1.73m²")
    print(f"estimated total CL     = {cl:.2f} L/h")

    # synthetic history: quarterly GFR over 2 years, decline of ~6 mL/min/1.73m²/year
    rng = np.random.default_rng(0)
    anos = np.arange(0, 2.01, 0.25)
    historico = Historico(datas=anos,
                          tfg_estimada=50.0 - 6.0*anos + rng.normal(0, 1.0, anos.size))
    tfg_pontual, tendencia, alerta = avaliar(paciente, historico)
    print(f"trend                  = {tendencia:+.1f} mL/min/1.73m²/year")
    print(f"alert (GFR < 60 or decline > 5/year) = {alerta}")


if __name__ == "__main__":
    main()
