"""
Answer key Ch. 14 — Ex. 6 (Challenge): glucose-insulin system, normal × diabetic.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def R_meal(t: float, dose: float = 50, tau: float = 60) -> float:
    return dose/tau if 0 <= t <= tau else 0.0


def sistema(t: float, y: np.ndarray, SI: float, k_sec: float,
            Gb: float, Ib: float) -> list[float]:
    G, X, I = y
    dG = -0.005*(G-Gb) - SI*X*G + R_meal(t)/6
    dX = -0.1*X + 0.00004*(I-Ib)
    dI = -0.25*(I-Ib) + k_sec*max(G-Gb, 0)   # basal secretion 0.25*Ib
    return [dG, dX, dI]


def main() -> None:
    sol_n = solve_ivp(sistema, [0, 240], [5.0, 0, 8.0],
                      args=(1.0, 5.0, 5.0, 8.0),
                      t_eval=np.linspace(0, 240, 241), max_step=1.0)
    sol_d = solve_ivp(sistema, [0, 240], [7.0, 0, 10.0],
                      args=(0.5, 1.0, 7.0, 10.0),
                      t_eval=np.linspace(0, 240, 241), max_step=1.0)

    for rotulo, sol in [("normal", sol_n), ("diabetic", sol_d)]:
        G, I = sol.y[0], sol.y[2]
        iG, iI = int(np.argmax(G)), int(np.argmax(I))
        print(f"{rotulo}: G peak {G[iG]:.2f} at t={sol.t[iG]:.0f} min; "
              f"G min {G.min():.2f}; G(120)={G[120]:.2f}; G(240)={G[240]:.2f}; "
              f"I peak {I[iI]:.1f} at t={sol.t[iI]:.0f} min")
    # normal:   G peak ~7.7 (t≈33), min ~4.7 near 2 h, I peak ~61 (t≈38)
    # diabetic: G peak ~13 (t≈60), G(120) ~9.4, G(240) ~7.5, I peak ~33 (t≈62)

    fig, (ax_g, ax_i) = plt.subplots(1, 2, figsize=(10, 4))
    ax_g.plot(sol_n.t, sol_n.y[0], label="normal")
    ax_g.plot(sol_d.t, sol_d.y[0], label="type 2 diabetic")
    ax_g.set_xlabel("t (min)"); ax_g.set_ylabel("G (mmol/L)"); ax_g.legend()
    ax_i.plot(sol_n.t, sol_n.y[2], label="normal")
    ax_i.plot(sol_d.t, sol_d.y[2], label="type 2 diabetic")
    ax_i.set_xlabel("t (min)"); ax_i.set_ylabel("I (mU/L)"); ax_i.legend()
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
