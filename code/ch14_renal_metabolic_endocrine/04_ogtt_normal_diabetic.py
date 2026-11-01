"""
Oral glucose tolerance test — comparison: normal × type 2 diabetic.

Chapter 14: Renal, metabolic and endocrine systems — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def R_meal(t: float, dose: float = 50, tau: float = 60) -> float:
    if 0 <= t <= tau:
        return dose / tau
    return 0.0


def sistema(t: float, y: np.ndarray, SI: float, k_sec: float,
            Gb: float, Ib: float) -> list[float]:
    G, X, I = y
    R = R_meal(t)
    dG = -0.005*(G - Gb) - SI*X*G + R/6
    dX = -0.1*X + 0.00004*(I - Ib)
    dI = -0.25*(I - Ib) + k_sec*max(G - Gb, 0)   # basal secretion 0.25*Ib
    return [dG, dX, dI]


def main() -> None:
    # Normal:    SI=1.0, k_sec=5.0, Gb=5.0, Ib=8.0   -> y0 = [5.0, 0, 8.0]
    # Diabetic:  SI=0.5, k_sec=1.0, Gb=7.0, Ib=10.0  -> y0 = [7.0, 0, 10.0]
    cenarios = [("Normal", 1.0, 5.0, 5.0, 8.0),
                ("Type 2 diabetic", 0.5, 1.0, 7.0, 10.0)]

    fig, (ax_g, ax_i) = plt.subplots(1, 2, figsize=(10, 4))
    for rotulo, SI, k_sec, Gb, Ib in cenarios:
        sol = solve_ivp(sistema, [0, 240], [Gb, 0.0, Ib],
                        args=(SI, k_sec, Gb, Ib),
                        t_eval=np.linspace(0, 240, 241), max_step=1.0)
        G, I = sol.y[0], sol.y[2]
        iG, iI = int(np.argmax(G)), int(np.argmax(I))
        print(f"{rotulo}: G peak {G[iG]:.2f} at t={sol.t[iG]:.0f} min; "
              f"G min {G.min():.2f} (t={sol.t[np.argmin(G)]:.0f}); "
              f"G(120)={G[120]:.2f}; G(240)={G[240]:.2f}; "
              f"I peak {I[iI]:.1f} at t={sol.t[iI]:.0f} min")
        ax_g.plot(sol.t, sol.y[0], label=rotulo)
        ax_i.plot(sol.t, sol.y[2], label=rotulo)

    ax_g.set_xlabel("t (min)")
    ax_g.set_ylabel("G (mmol/L)")
    ax_g.set_title("Blood glucose")
    ax_g.legend()

    ax_i.set_xlabel("t (min)")
    ax_i.set_ylabel("I (mU/L)")
    ax_i.set_title("Insulin")
    ax_i.legend()

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
