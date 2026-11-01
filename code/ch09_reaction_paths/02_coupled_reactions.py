"""
Consecutive network A -> B -> C — kinetic intermediate accumulating when k1 > k2.

Chapter 9: Reaction pathways, free energy and kinetics — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


k1, k2 = 1.0, 0.3                # k1 > k2: B accumulates


def f(t: float, y: np.ndarray) -> list[float]:
    A, B, C = y
    return [-k1*A, k1*A - k2*B, k2*B]


def main() -> None:
    sol = solve_ivp(f, [0, 20], [1.0, 0.0, 0.0],
                    t_eval=np.linspace(0, 20, 400))
    A, B, C = sol.y

    fig, ax = plt.subplots()
    ax.plot(sol.t, A, label="A")
    ax.plot(sol.t, B, label="B (intermediate)")
    ax.plot(sol.t, C, label="C")
    ax.set_xlabel("t")
    ax.set_ylabel("concentration")
    ax.legend()
    ax.set_title("Chain A -> B -> C")
    plt.show()


if __name__ == "__main__":
    main()
