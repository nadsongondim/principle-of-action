"""
Quick guide — SciPy: solve_ivp, optimize, quad, interpolate, ndimage.

Appendix B: Quick Guide to Scientific Python — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import CubicSpline, PchipInterpolator
from scipy.optimize import curve_fit, minimize


# ODEs with solve_ivp (chapter 2, the engine of the volume)
def f(t: float, y: np.ndarray) -> np.ndarray:
    return -0.3 * y                        # dy/dt = -0.3 y


def secao_solve_ivp() -> None:
    sol = solve_ivp(f, [0, 20], [1.0],
                    t_eval=np.linspace(0, 20, 200),
                    rtol=1e-8, atol=1e-10)
    t, y = sol.t, sol.y[0]
    print(f"y(0)={y[0]:.4f}  y(20)={y[-1]:.4f}")


def secao_otimizacao() -> None:
    # minimization
    res = minimize(lambda x: (x[0]-3)**2 + (x[1]+1)**2, x0=[0, 0])
    x_otimo = res.x
    print(f"minimum at {x_otimo}")

    # curve fitting
    def modelo(t, A, k):
        return A * np.exp(-k * t)

    rng = np.random.default_rng(0)
    t_dados = np.linspace(0, 10, 30)
    y_dados = modelo(t_dados, 2.0, 0.3) + rng.normal(0, 0.05, t_dados.size)
    parametros, cov = curve_fit(modelo, t_dados, y_dados, p0=[1.0, 0.1])
    print(f"A={parametros[0]:.4f}  k={parametros[1]:.4f}")


def secao_integracao() -> None:
    valor, erro = quad(lambda x: np.exp(-x**2), 0, np.inf)
    print(f"value={valor:.6f}  error≈{erro:.2e}")


def secao_interpolacao() -> None:
    t_pontos = np.linspace(0, 10, 6)
    y_pontos = np.sin(t_pontos)
    cs = CubicSpline(t_pontos, y_pontos)        # smoother
    pc = PchipInterpolator(t_pontos, y_pontos)  # no overshoot
    t_novo = np.linspace(0, 10, 50)
    y_em_t = pc(t_novo)
    print(f"interpolated y at t=5 → {pc(5.0):.4f}  (expected ~{np.sin(5):.4f})")


def main() -> None:
    secao_solve_ivp()
    secao_otimizacao()
    secao_integracao()
    secao_interpolacao()


if __name__ == "__main__":
    main()
