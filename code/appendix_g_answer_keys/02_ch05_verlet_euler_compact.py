"""
Answer key Ch. 5 — Ex. 6 (Challenge): Euler and Verlet steps in compact form.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def passo_euler(x: float, v: float, h: float) -> tuple[float, float]:
    return x + h*v, v - h*x          # a(x) = -x


def passo_verlet(x: float, v: float, h: float) -> tuple[float, float]:
    a = -x
    xn = x + h*v + 0.5*h**2*a
    an = -xn
    vn = v + 0.5*h*(a + an)
    return xn, vn


def main() -> None:
    h, N = 0.1, 200
    x_e, v_e = 1.0, 0.0
    x_v, v_v = 1.0, 0.0
    E_e = np.empty(N + 1)
    E_v = np.empty(N + 1)
    E_e[0] = 0.5 * (x_e**2 + v_e**2)
    E_v[0] = 0.5 * (x_v**2 + v_v**2)
    for i in range(1, N + 1):
        x_e, v_e = passo_euler(x_e, v_e, h)
        x_v, v_v = passo_verlet(x_v, v_v, h)
        E_e[i] = 0.5 * (x_e**2 + v_e**2)
        E_v[i] = 0.5 * (x_v**2 + v_v**2)

    t = np.arange(N + 1) * h
    print(f"Verlet: E between {E_v.min():.6f} and {E_v.max():.6f} "
          f"(range {E_v.max()-E_v.min():.4e} ≈ h²/8 = {h**2/8:.4e})")
    print(f"Euler:  E(t={t[-1]:.0f}) = {E_e[-1]:.3f}")
    # Verlet: 0.498750 to 0.5 (range ≈ 1.25e-3);  Euler: E(20) ≈ 3.658
    fig, ax = plt.subplots()
    ax.plot(t, E_e, label="explicit Euler")
    ax.plot(t, E_v, label="velocity Verlet")
    ax.axhline(0.5, color="k", linestyle=":", label="exact E")
    ax.set_xlabel("t")
    ax.set_ylabel("E(t)")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
