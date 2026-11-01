"""
Integrated hypertension case — Windkessel comparing patient and treatment.

Chapter 18: Integrated cases in quantitative medicine — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


T_, t_sys = 0.9, 0.3
SV = 70.0


def Q(t: float) -> float:
    tt = t % T_
    if tt < t_sys:
        return (np.pi*SV/(2*t_sys)) * np.sin(np.pi*tt/t_sys)
    return 0.0


def main() -> None:
    # Windkessel: simulate two scenarios — without and with a vasodilator
    # (qualitative parameters)
    R_basal, C_basal = 1.5, 1.2         # patient: ↑R, normal C
    R_trat = 1.3                        # after vasodilator

    cenarios = [(R_basal, C_basal, "hypertensive patient"),
                (R_trat, C_basal, "after vasodilator")]

    fig, ax = plt.subplots()
    # 20 s horizon (several τ = R·C) to reach the periodic regime:
    # the MAP (cycle average) tends to R·SV/T — ~117 mmHg with R = 1.5 and
    # ~101 mmHg with R = 1.3 (the normotensive case of Ch. 13), as in the text.
    t_fim = 20.0
    for R_, C_, rotulo in cenarios:
        sol = solve_ivp(lambda t, P: (Q(t) - P/R_)/C_,
                        [0, t_fim], [80.0],
                        t_eval=np.linspace(0, t_fim, 8000), max_step=0.005)
        ax.plot(sol.t, sol.y[0], label=rotulo)
        ultimos = sol.y[0][sol.t > t_fim - 2*T_]    # last two cycles
        sis, dia = float(np.max(ultimos)), float(np.min(ultimos))
        map_ = float(np.mean(ultimos))               # cycle average
        print(f"{rotulo}: sys={sis:.0f}  dia={dia:.0f}  MAP={map_:.0f}")
    # hypertensive patient: MAP ≈ 117;  after vasodilator: MAP ≈ 101
    ax.set_xlabel("t (s)")
    ax.set_ylabel("P (mmHg)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
