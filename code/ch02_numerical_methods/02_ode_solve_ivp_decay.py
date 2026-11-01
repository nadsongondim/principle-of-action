"""
Decay ODE solved by SciPy's adaptive solve_ivp.

Chapter 2: Essential numerical methods — Volume 4 of the series "The Principle
of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


def f(t: float, y: np.ndarray) -> np.ndarray:
    return -0.3 * y                 # dy/dt = -0.3 y  (decay)


def main() -> None:
    sol = solve_ivp(f, [0, 20], [1.0], t_eval=np.linspace(0, 20, 200))

    fig, ax = plt.subplots()
    ax.plot(sol.t, sol.y[0], label="solve_ivp")
    ax.plot(sol.t, np.exp(-0.3 * sol.t), "--", label="exact solution")
    ax.set_xlabel("t")
    ax.set_ylabel("y(t)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
