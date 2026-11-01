"""
Answer key Ch. 18 — Ex. 6 (Challenge): three blood glucose scenarios over 24 h.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


# glucose-insulin model of Example 2 of ch. 14, with three meals
refeicoes = [7*60, 12*60, 19*60]                        # start (min)


def R_total(t: float, dur: float = 60) -> float:        # dur: duration (min)
    return sum(50/dur if t0 <= t <= t0+dur else 0 for t0 in refeicoes)


def diabetes(t: float, y: np.ndarray, SI: float, k_sec: float,
             Gb: float, Ib: float, dur: float) -> list[float]:
    G, X, I = y
    dG = -0.005*(G-Gb) - SI*X*G + R_total(t, dur)/6
    dX = -0.1*X + 0.00004*(I-Ib)
    dI = -0.25*(I-Ib) + k_sec*max(G-Gb, 0)
    return [dG, dX, dI]


def main() -> None:
    Ib = 10.0
    # (label, SI, k_sec, Gb, dur) — illustrative parameters
    cenarios = [
        ("no treatment",          0.3, 1.0, 10.0,  60),
        ("metformin",             0.3, 1.0,  7.5,  60),   # Gb -> 7.5
        ("metformin + GLP-1",     0.5, 2.0,  6.5, 120),   # k_sec, SI, Gb, R(t)
    ]
    t_span = (0.0, 24*60.0)
    t_eval = np.linspace(*t_span, 24*60 + 1)

    fig, ax = plt.subplots()
    for rotulo, SI, k_sec, Gb, dur in cenarios:
        sol = solve_ivp(diabetes, t_span, [Gb, 0.0, Ib],
                        args=(SI, k_sec, Gb, Ib, dur), t_eval=t_eval,
                        max_step=1.0)
        G = sol.y[0]
        print(f"{rotulo}: peak {G.max():.1f} mmol/L "
              f"(t = {sol.t[G.argmax()]/60:.1f} h); baseline {G[0]:.1f}")
        ax.plot(sol.t/60, G, label=rotulo)
    # no treatment: peak 16.5; baseline 10.0
    # metformin:    peak 14.2; baseline 7.5
    # met + GLP-1:  peak 9.8;  baseline 6.5
    ax.axhspan(4.4, 7.2, alpha=0.15, label="fasting target (4.4–7.2)")
    ax.set_xlabel("t (h)")
    ax.set_ylabel("G (mmol/L)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
