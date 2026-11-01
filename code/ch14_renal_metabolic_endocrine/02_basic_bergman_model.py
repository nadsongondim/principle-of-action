"""
Bergman minimal model — skeleton of glucose-insulin dynamics.

Chapter 14: Renal, metabolic and endocrine systems — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


# qualitative parameters for a healthy individual
p1, p2, p3, Gb, Ib = 0.005, 0.1, 0.00004, 5.0, 8.0


def insulina(t: float) -> float:
    """Exogenous insulinemia (mU/L) — simple post-meal peak model."""
    pico = 60.0
    return Ib + (pico - Ib) * np.exp(-((t - 30) / 25.0) ** 2)


def R_meal(t: float) -> float:
    """Glucose input: rectangular pulse during the first hour."""
    return 0.05 if 0 <= t <= 60 else 0.0


def bergman(t: float, y: np.ndarray, R_meal, insulina) -> list[float]:
    # R_meal(t) and insulina(t): inputs
    G, X = y
    return [-p1*(G - Gb) - X*G + R_meal(t),
            -p2*X + p3*(insulina(t) - Ib)]


def main() -> None:
    sol = solve_ivp(lambda t, y: bergman(t, y, R_meal, insulina),
                    [0, 180], [Gb, 0.0],
                    t_eval=np.linspace(0, 180, 600))

    fig, ax = plt.subplots()
    ax.plot(sol.t, sol.y[0], label="G(t)")
    ax.plot(sol.t, sol.y[1] * 1000, label="X(t) ×1000")
    ax.set_xlabel("t (min)")
    ax.set_ylabel("level")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
