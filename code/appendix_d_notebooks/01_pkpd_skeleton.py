"""
PK/PD notebook skeleton — example of how to organize chapter 12.

This script reproduces the skeleton suggested for a pharmacokinetics notebook.
In a real project, dose injection is done with discrete solve_ivp events,
not with an approximate time comparison as here.

Appendix D: Notebooks and Project Organization — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

# notebook: parte4-clinica/12-pkpd.ipynb
# topic: Chapter 12 — computational pharmacokinetics and pharmacodynamics
# author: ...
# date: 2026-XX-XX

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


# parameters
ka, ke = 1.5, 0.3
V, dose = 1.0, 100.0
tau = 6.0
n_doses = 6


# simulation (schematic example — in a real project, use solve_ivp events)
def f(t: float, y: np.ndarray) -> list[float]:
    A, C = y
    if t % tau < 0.01:
        A += dose
    return [-ka * A, ka/V * A - ke * C]


def main() -> None:
    sol = solve_ivp(f, [0, tau * n_doses], [dose, 0.0],
                    t_eval=np.linspace(0, tau * n_doses, 1000),
                    max_step=0.01)

    fig, ax = plt.subplots()
    ax.plot(sol.t, sol.y[1])
    ax.set_xlabel("t (h)")
    ax.set_ylabel("C (mg/L)")
    plt.show()


if __name__ == "__main__":
    main()
