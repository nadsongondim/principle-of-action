"""
Full kinetic system E + S <-> ES -> E + P (without the Briggs-Haldane approximation).

Chapter 10: Enzyme kinetics and biochemical networks — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


E_tot = 1.0
k1, km1, k2 = 100.0, 1.0, 10.0     # fast formation of ES


def f(t: float, y: np.ndarray) -> list[float]:
    S, ES, P = y
    E = E_tot - ES
    return [-k1*E*S + km1*ES, k1*E*S - (km1+k2)*ES, k2*ES]


def main() -> None:
    # Stiff system (ratio between time scales ~10^2 with k1=100, k2=10);
    # BDF is an appropriate implicit integrator — the default RK45 decouples poorly.
    # Formal justification in Chapter 5, §5.6.
    sol = solve_ivp(f, [0, 5], [10.0, 0.0, 0.0], method='BDF',
                    rtol=1e-8, atol=1e-10,
                    t_eval=np.linspace(0, 5, 400))
    S, ES, P = sol.y

    fig, ax = plt.subplots()
    ax.plot(sol.t, S, label="S")
    ax.plot(sol.t, ES, label="ES")
    ax.plot(sol.t, P, label="P")
    ax.set_xlabel("t")
    ax.set_ylabel("concentration")
    ax.legend()
    ax.set_title("Full enzyme kinetics")
    plt.show()


if __name__ == "__main__":
    main()
