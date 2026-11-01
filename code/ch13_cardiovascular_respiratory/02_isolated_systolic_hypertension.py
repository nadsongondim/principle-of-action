"""
Windkessel comparison: normal × elderly with reduced compliance (Example 1).

Chapter 13: Cardiovascular and respiratory systems — Volume 4 of the series
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
    fig, ax = plt.subplots()
    for R_, C_, rotulo in [(1.3, 1.2, "normal"), (1.3, 0.6, "stiff elderly")]:
        sol = solve_ivp(lambda t, P: (Q(t) - P/R_)/C_,
                        [0, 5], [80.0],
                        t_eval=np.linspace(0, 5, 2000), max_step=0.005)
        P = sol.y[0][sol.t > 5 - 2*T_]          # last two cycles
        print(rotulo, round(P.max()), round(P.min()), round(P.mean()))
        print(f"   systolic = {P.max():.0f}  diastolic = {P.min():.0f}  "
              f"pulse pressure = {P.max()-P.min():.0f}  "
              f"cycle mean = {P.mean():.0f}")
        ax.plot(sol.t, sol.y[0], label=rotulo)
    # expected output (book, Chapter 13, Example 1):
    # normal 122 82 101
    # stiff elderly 144 65 101
    ax.set_xlabel("t (s)")
    ax.set_ylabel("P (mmHg)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
