"""
Quick guide — SymPy: derivative, integral, dsolve and lambdify.

Appendix B: Quick Guide to Scientific Python — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
import sympy as sp


def main() -> None:
    t = sp.symbols('t', real=True)
    y = sp.Function('y')(t)

    # differentiate
    expr = sp.sin(t) * sp.exp(-t)
    print("d/dt:", sp.diff(expr, t))

    # integrate
    print("integral:", sp.integrate(expr, t))

    # solve an ODE
    edo = sp.Eq(y.diff(t) + y, sp.exp(-t))
    print("dsolve:", sp.dsolve(edo, y))

    # convert to a numerical function
    f_num = sp.lambdify(t, expr, 'numpy')
    valores = f_num(np.linspace(0, 5, 100))
    print(f"numerical values: shape {valores.shape}, first = {valores[0]:.4f}")


if __name__ == "__main__":
    main()
