"""
Answer key Ch. 12 — Ex. 6 (Challenge): C(t) under repeated doses, two regimens.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


# one compartment with first-order oral absorption (Example 1 of ch. 12):
# each dose adds its own Bateman curve
F, V, ka, ke = 1.0, 50.0, 1.5, 0.1


def simular(D: float, tau: float, T: float = 120) -> tuple[np.ndarray, np.ndarray]:
    t = np.linspace(0, T, 5000)
    C = np.zeros_like(t)
    for n in range(int(T/tau)+1):
        t0 = n*tau
        mask = t >= t0
        dt = t[mask] - t0
        C[mask] += F*D*ka/(V*(ka-ke)) * (np.exp(-ke*dt) - np.exp(-ka*dt))
    return t, C


def main() -> None:
    t1, C1 = simular(90, 12)
    t2, C2 = simular(45, 6)
    for rotulo, t, C in [("90 mg / 12 h", t1, C1), ("45 mg / 6 h", t2, C2)]:
        regime = C[t >= 96]                    # steady state
        print(f"{rotulo}: peak {regime.max():.2f}  trough {regime.min():.2f}  "
              f"amplitude {regime.max()-regime.min():.2f} mg/L")
    # 90 mg / 12 h: peak 2.18  trough 0.83  amplitude 1.35
    # 45 mg / 6 h:  peak 1.74  trough 1.17  amplitude 0.57

    fig, ax = plt.subplots()
    ax.plot(t1, C1, label="90 mg / 12 h")
    ax.plot(t2, C2, label="45 mg / 6 h")
    ax.axhspan(0.5, 2.5, alpha=0.2, label="therapeutic window")
    ax.set_xlabel("t (h)")
    ax.set_ylabel("C (mg/L)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
