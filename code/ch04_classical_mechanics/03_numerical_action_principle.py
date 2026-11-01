"""
The Principle of Action as a number you can compute — minimum of S(s) on the physical trajectory.

For the harmonic oscillator with x(0)=1, x(pi/2)=0, the physical trajectory is cos(t).
(On [0, pi] there would be conjugate points: the whole family cos t + c·sin t would
have zero action and the minimum would be degenerate — hence the interval [0, pi/2].)
Builds a family x_s(t) = cos(t) + s * eta(t) with eta vanishing at the endpoints,
computes the action S(s) with quad and shows that the minimum occurs at s=0.

Chapter 4: Computational Classical Mechanics — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


omega = 1.0
t1, t2 = 0.0, np.pi/2


def eta(t: float) -> float:
    """Perturbation that vanishes at the endpoints t1 and t2."""
    return np.sin(t) * t * (np.pi/2 - t)


def eta_dot(t: float) -> float:
    # analytical derivative of eta above
    return (np.cos(t) * t * (np.pi/2 - t)
            + np.sin(t) * (np.pi/2 - 2.0 * t))


def x_s(t: float, s: float) -> float:
    return np.cos(t) + s * eta(t)


def xdot_s(t: float, s: float) -> float:
    return -np.sin(t) + s * eta_dot(t)


def acao(s: float) -> float:
    L = lambda t: 0.5*xdot_s(t, s)**2 - 0.5*omega**2 * x_s(t, s)**2
    valor, _ = quad(L, t1, t2)
    return valor


def main() -> None:
    esses = np.linspace(-1, 1, 41)
    S = [acao(s) for s in esses]

    s_min = esses[int(np.argmin(S))]
    print(f"numerical minimum of S(s) occurs at s = {s_min:.4f}")
    print(f"minimum value of S = {min(S):.6f}")
    print(f"S(1) = {acao(1.0):.4f}   S(0.5) = {acao(0.5):.4f}  "
          "(S grows exactly as s²)")

    fig, ax = plt.subplots()
    ax.plot(esses, S)
    ax.axvline(0.0, color="red", linestyle="--", label="physical trajectory (s=0)")
    ax.set_xlabel("s")
    ax.set_ylabel("S(s)")
    ax.set_title("Action along the family of trajectories")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
