"""
Hybrid mechanistic + learning model — two-compartment PK skeleton
with an oral dose (absorption compartment in the GI tract), in amounts.

The learned layer (placeholder) adjusts the PK parameters as a function of
patient covariates; the mechanistic skeleton guarantees the correct shape
of the concentration-time curve.

Chapter 22: Usability, adoption and perspectives — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp


@dataclass
class Paciente:
    covariaveis: np.ndarray


class RedeStub:
    """Didactic stub — in production, replace with a trained network."""

    def predict(self, x: np.ndarray) -> tuple[float, float, float, float, float]:
        # returns (ka, ke, k12, k21, V1) with plausible values
        idade, peso, tfg = x
        ka = 1.2                     # 1/h
        ke = 0.1 * (tfg / 100.0)     # 1/h
        k12 = 0.2                    # 1/h
        k21 = 0.15                   # 1/h
        V1 = 0.15 * peso             # L (central volume)
        return ka, ke, k12, k21, V1


rede_neural = RedeStub()

dose = 500.0                         # mg, single oral dose (illustrative)


# Mechanistic skeleton: two-compartment PK, oral dose
def pk_modelo(t, y, ka, ke, k12, k21):
    A_tgi, A1, A2 = y        # amounts: GI tract, central, peripheral
    return [-ka*A_tgi,
            ka*A_tgi - (ke + k12)*A1 + k21*A2,
            k12*A1 - k21*A2]


# Learned component: parameters as a function of covariates
def parametros_individuais(covariaveis):
    return rede_neural.predict(covariaveis)  # returns ka, ke, k12, k21, V1


def main() -> None:
    paciente = Paciente(covariaveis=np.array([62.0, 72.0, 80.0]))

    # Hybrid pipeline
    ka, ke, k12, k21, V1 = parametros_individuais(paciente.covariaveis)
    sol = solve_ivp(pk_modelo, [0, 24], [dose, 0, 0], args=(ka, ke, k12, k21),
                    t_eval=np.linspace(0, 24, 200))
    C1 = sol.y[1] / V1           # plasma concentration

    print(f"individualized parameters (ka, ke, k12, k21, V1) = "
          f"({ka:.3g}, {ke:.3g}, {k12:.3g}, {k21:.3g}, {V1:.1f})")
    print(f"C1 max = {C1.max():.3f} mg/L at t = {sol.t[C1.argmax()]:.1f} h")
    print(f"C1 final (24 h) = {C1[-1]:.4f} mg/L")


if __name__ == "__main__":
    main()
