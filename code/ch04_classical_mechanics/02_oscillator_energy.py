"""
Harmonic oscillator — energy conservation checked with a high-accuracy solve_ivp.

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
    sol = solve_ivp(f, [0, 20], y0=[1.0, 0.0],
                    t_eval=np.linspace(0, 20, 800),
                    rtol=1e-9, atol=1e-12)
    x, v = sol.y
    E = 0.5*v**2 + 0.5*x**2          # total energy

    print(f"initial E = {E[0]:.12f}")
    print(f"final E   = {E[-1]:.12f}")
    print(f"maximum variation of E = {np.max(np.abs(E - E[0])):.2e}")

    fig, ax = plt.subplots()
    ax.plot(sol.t, E - 0.5)
    ax.set_xlabel("t")
    ax.set_ylabel("E(t) - 0.5")
    ax.set_title("Energy deviation over time")
    plt.show()


if __name__ == "__main__":
    main()
