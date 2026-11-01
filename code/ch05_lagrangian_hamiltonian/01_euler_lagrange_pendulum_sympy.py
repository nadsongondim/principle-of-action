"""
Symbolic derivation of the Euler-Lagrange equation for the simple pendulum with SymPy.

Chapter 5: Lagrangian, Hamiltonian and Phase Space — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import sympy as sp


def main() -> None:
    t = sp.symbols('t', real=True)
    m, L_, g = sp.symbols('m L g', positive=True)
    theta = sp.Function('theta')(t)

    T = sp.Rational(1, 2) * m * (L_ * theta.diff(t)) ** 2
    V = -m * g * L_ * sp.cos(theta)
    Lag = T - V

    EL = sp.diff(Lag.diff(theta.diff(t)), t) - Lag.diff(theta)
    EL_simplificada = sp.simplify(EL)
    print("Euler-Lagrange equation for the simple pendulum:")
    sp.pprint(EL_simplificada)
    # result: L*m*(L*theta''(t) + g*sin(theta(t)))


if __name__ == "__main__":
    main()
