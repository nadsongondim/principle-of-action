"""
Generic wrapper for molecular energy minimization with L-BFGS-B.

Chapter 8: Molecular structure and potential energy — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from typing import Callable

import numpy as np
from scipy.optimize import minimize


def energia_total(R: np.ndarray, parametros_campo_forca: dict) -> float:
    """Didactic stub — sum of harmonic bond terms between the given pairs."""
    energia = 0.0
    for (i, j, k_b, r0) in parametros_campo_forca.get("ligacoes", []):
        r = np.linalg.norm(R[i] - R[j])
        energia += 0.5 * k_b * (r - r0)**2
    return energia


def grad_U(R_flat: np.ndarray) -> np.ndarray:
    # finite-difference gradient — can be replaced by an analytical gradient
    eps = 1e-5
    g = np.zeros_like(R_flat)
    for i in range(R_flat.size):
        passo = np.zeros_like(R_flat)
        passo[i] = eps
        g[i] = (U(R_flat + passo) - U(R_flat - passo)) / (2 * eps)
    return g


# these two objects are filled in main()
parametros_campo_forca: dict = {}
R0: np.ndarray = np.zeros((2, 3))


def U(R_flat: np.ndarray) -> float:                       # R_flat: 3N vector
    R = R_flat.reshape(-1, 3)
    return energia_total(R, parametros_campo_forca)


def main() -> None:
    global parametros_campo_forca, R0
    # minimal example: diatomic pair around r0 = 1.5 Å
    parametros_campo_forca = {"ligacoes": [(0, 1, 1000.0, 1.5)]}
    R0 = np.array([[0.0, 0.0, 0.0], [0.5, 0.0, 0.0]])     # far from equilibrium

    resultado = minimize(U, R0.flatten(), jac=grad_U, method="L-BFGS-B")
    R_otimizada = resultado.x.reshape(-1, 3)
    print("Optimized R:")
    print(R_otimizada)
    print(f"final distance = {np.linalg.norm(R_otimizada[0] - R_otimizada[1]):.4f} Å")


if __name__ == "__main__":
    main()
