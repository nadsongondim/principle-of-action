"""
Ventilatory mechanics — V(t) under a periodic driving pressure (pulmonary RC model).

Chapter 13: Cardiovascular and respiratory systems — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


Cp = 0.05            # L/cmH2O — lung compliance
Rv = 5.0             # cmH2O / (L/s) — airway resistance
T_resp = 4.0         # respiratory period (s)
P_max = 10.0         # peak driving pressure (cmH2O)


def P_drive(t: float) -> float:
    # positive sinusoidal driving pressure during "inspiration"
    return max(0.0, P_max * np.sin(2*np.pi*t/T_resp))


def f(t: float, V: np.ndarray) -> float:
    return (P_drive(t) - V / Cp) / Rv


def main() -> None:
    sol = solve_ivp(f, [0, 12], [0.0],
                    t_eval=np.linspace(0, 12, 1200), max_step=0.05)

    fig, ax = plt.subplots()
    ax.plot(sol.t, sol.y[0])
    ax.set_xlabel("t (s)")
    ax.set_ylabel("V (L)")
    ax.set_title("Tidal volume under periodic driving pressure")
    plt.show()


if __name__ == "__main__":
    main()
