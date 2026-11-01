"""
A -> B -> C network with MM kinetics and a partial numerical knockout of E2 (Example 2).

Chapter 10: Enzyme kinetics and biochemical networks — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


V1, K1, V2, K2 = 1.0, 1.0, 0.1, 1.0          # V2 reduced 10×


def f(t: float, y: np.ndarray) -> list[float]:
    A, B, C = y
    v1 = V1 * A / (K1 + A)
    v2 = V2 * B / (K2 + B)
    return [-v1, v1 - v2, v2]


def main() -> None:
    sol = solve_ivp(f, [0, 100], [10.0, 0.0, 0.0],
                    t_eval=np.linspace(0, 100, 400))
    A, B, C = sol.y

    fig, ax = plt.subplots()
    ax.plot(sol.t, A, label="A")
    ax.plot(sol.t, B, label="B (accumulates under E2 knockout)")
    ax.plot(sol.t, C, label="C")
    ax.set_xlabel("t")
    ax.set_ylabel("concentration")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
