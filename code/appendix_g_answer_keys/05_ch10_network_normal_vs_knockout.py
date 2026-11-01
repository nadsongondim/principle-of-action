"""
Answer key Ch. 10 — Ex. 6 (Challenge): A→B→C network, normal and with E2 knockout.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def rede(t: float, y: np.ndarray, V2: float) -> list[float]:
    A, B, C = y
    v1 = 1.0*A/(1.0+A)
    v2 = V2*B/(1.0+B)
    return [-v1, v1-v2, v2]


def main() -> None:
    t_eval = np.linspace(0, 100, 400)
    sol_n = solve_ivp(rede, [0, 100], [10, 0, 0], args=(1.0,), t_eval=t_eval)
    sol_k = solve_ivp(rede, [0, 100], [10, 0, 0], args=(0.1,), t_eval=t_eval)

    for nome, sol in [("normal", sol_n), ("knock-out", sol_k)]:
        B = sol.y[1]
        iB = int(np.argmax(B))
        B_em = lambda tt: np.interp(tt, sol.t, B)
        print(f"{nome}: B max {B[iB]:.2f} at t={sol.t[iB]:.1f}; "
              f"B(20)={B_em(20):.2f}  B(30)={B_em(30):.2f}  "
              f"B(100)={B[-1]:.2f}  C(100)={sol.y[2][-1]:.2f}")
    # normal: B max ~2.3 at t≈9, low (~0.02) at t≈20
    # knock-out: B max ~8.8 at t≈15; ~7.5 at t=30; ~1.9 at t=100; C(100) ~8.1

    fig, (ax_n, ax_k) = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    for ax, sol, titulo in [(ax_n, sol_n, "V2 = 1.0 (normal)"),
                             (ax_k, sol_k, "V2 = 0.1 (knockout)")]:
        ax.plot(sol.t, sol.y[0], label="A")
        ax.plot(sol.t, sol.y[1], label="B")
        ax.plot(sol.t, sol.y[2], label="C")
        ax.set_xlabel("t")
        ax.set_title(titulo)
        ax.legend()
    ax_n.set_ylabel("concentration")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
