"""
Pharmacokinetics of a single oral dose — absorption/elimination model (Bateman).

The default `method=` (RK45) is adequate here because ka/ke ≈ 5 — the system is
smooth and non-stiff. Switch to `method='BDF'` (or 'LSODA') when ka and ke
are separated by more than one order of magnitude, a situation typical of
delayed release and of combinations with enzyme inhibitors.

Chapter 12: Computational pharmacokinetics and pharmacodynamics — Volume 4 of
the series "The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


ka, ke, F, V, D = 1.5, 0.3, 1.0, 1.0, 100.0


def f(t: float, y: np.ndarray) -> list[float]:
    A, C = y
    return [-ka * A, ka/V * A - ke * C]


def main() -> None:
    sol = solve_ivp(f, [0, 24], [F*D, 0.0],
                    t_eval=np.linspace(0, 24, 400))
    A, C = sol.y

    fig, ax = plt.subplots()
    ax.plot(sol.t, C, label="C(t) — plasma")
    ax.plot(sol.t, A, "--", label="A(t) — gut")
    ax.set_xlabel("t (h)")
    ax.set_ylabel("concentration / amount")
    ax.set_title("Oral absorption model (Bateman)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
