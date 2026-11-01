"""
Harmonic oscillator integrated with solve_ivp, and its phase portrait.

Chapter 4: Computational Classical Mechanics — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


omega = 1.0


def f(t: float, y: np.ndarray) -> list[float]:
    x, v = y
    return [v, -omega**2 * x]


def main() -> None:
    # tolerances matched with 02_oscillator_energy.py so that both
    # examples of the chapter produce trajectories comparable point by point.
    sol = solve_ivp(f, [0, 20], y0=[1.0, 0.0],
                    t_eval=np.linspace(0, 20, 800),
                    rtol=1e-9, atol=1e-12)

    x, v = sol.y

    fig, (ax_t, ax_fase) = plt.subplots(1, 2, figsize=(10, 4))
    ax_t.plot(sol.t, x)
    ax_t.set_xlabel("t")
    ax_t.set_ylabel("x(t)")
    ax_t.set_title("Trajectory")

    ax_fase.plot(x, v)
    ax_fase.set_xlabel("x")
    ax_fase.set_ylabel("v")
    ax_fase.set_title("Phase portrait")
    ax_fase.set_aspect("equal")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
