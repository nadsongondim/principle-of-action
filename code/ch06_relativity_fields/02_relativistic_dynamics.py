"""
Relativistic dynamics under a constant force — the velocity approaches c asymptotically.

Chapter 6: Relativity, fields and electromagnetism — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


m, c, F = 1.0, 1.0, 0.4


def rel(t: float, p: np.ndarray) -> float:                # dp/dt = F (relativistic)
    return F


def main() -> None:
    sol_p = solve_ivp(rel, [0, 20], [0.0], t_eval=np.linspace(0, 20, 400))
    p = sol_p.y[0]
    v = p / np.sqrt(m**2 + (p/c)**2)        # from p to v
    v_classica = F * sol_p.t / m

    fig, ax = plt.subplots()
    ax.plot(sol_p.t, v, label="relativistic")
    ax.plot(sol_p.t, v_classica, "--", label="classical")
    ax.axhline(c, color="k", linestyle=":", label="c")
    ax.set_xlabel("t")
    ax.set_ylabel("v(t)")
    ax.set_ylim(0, 1.5 * c)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
