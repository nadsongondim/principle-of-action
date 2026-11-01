"""
Scalar optimization with scipy.optimize.minimize — finding the minimum of a parabola.

Chapter 2: Essential numerical methods — Volume 4 of the series "The Principle
of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from scipy.optimize import minimize


def main() -> None:
    resultado = minimize(lambda x: (x - 3.0)**2 + 1.0, x0=0.0)
    print(resultado)
    print(f"x_min = {resultado.x[0]:.6f}    f_min = {resultado.fun:.6f}")


if __name__ == "__main__":
    main()
