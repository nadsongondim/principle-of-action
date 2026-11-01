"""
Lagrangian of the simple pendulum (Example 1) — complete symbolic derivation.

Builds L = T - V with the potential energy measured relative to the point of
suspension and applies Euler-Lagrange to obtain the equation of motion.

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

    Lag = sp.Rational(1, 2)*m*(L_*theta.diff(t))**2 + m*g*L_*sp.cos(theta)
    EL = sp.diff(Lag.diff(theta.diff(t)), t) - Lag.diff(theta)
    print(sp.simplify(EL))
    # L*m*(L*Derivative(theta(t), (t, 2)) + g*sin(theta(t)))


if __name__ == "__main__":
    main()
