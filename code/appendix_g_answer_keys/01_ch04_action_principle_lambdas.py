"""
Answer key Ch. 4 — Ex. 6 (Challenge): minimum of the action for the oscillator via lambdas.

Endpoints x(0) = 1 and x(π/2) = 0 (interval [0, π/2]; on [0, π] there would be
conjugate points and the family cos t + c·sin t would have zero action for every c).

Compact version with anonymous functions for η, x_s and ẋ_s.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def main() -> None:
    eta = lambda t: np.sin(t) * t * (np.pi/2 - t)
    deta = lambda t: np.cos(t)*t*(np.pi/2-t) + np.sin(t)*(np.pi/2 - 2*t)
    x = lambda t, s: np.cos(t) + s*eta(t)
    xd = lambda t, s: -np.sin(t) + s*deta(t)
    S = lambda s: quad(lambda t: 0.5*xd(t, s)**2 - 0.5*x(t, s)**2, 0, np.pi/2)[0]
    ss = np.linspace(-1, 1, 41)
    Svals = np.array([S(s) for s in ss])

    s_min = ss[int(np.argmin(Svals))]
    print(f"numerical minimum at s = {s_min:.3f}  (expected: 0)")
    print(f"S(0) = {S(0.0):.1e}  (expected: 0)")
    print(f"S(±1) = {S(1.0):.4f} / {S(-1.0):.4f}   S(±0.5) = {S(0.5):.4f} / {S(-0.5):.4f}")
    # S(0) ~ 1e-17;  S(±1) ≈ 0.3230;  S(±0.5) ≈ 0.0807 (= S(1)/4: exact parabola)

    fig, ax = plt.subplots()
    ax.plot(ss, Svals)
    ax.axvline(0, color="red", linestyle="--")
    ax.set_xlabel("s")
    ax.set_ylabel("S(s)")
    plt.show()


if __name__ == "__main__":
    main()
