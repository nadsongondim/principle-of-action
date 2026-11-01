"""
Energy minimization of the water molecule with L-BFGS-B (Example 1).

Uses two harmonic potentials for the O-H bonds and one for the H-O-H angle,
starting from an arbitrary initial guess. The minimizer returns the
experimental geometry.

Note: the force constants (k_b, k_t) and the equilibrium distances/angle
are **didactic** values, chosen to make the equilibrium geometry
numerically obvious. They do not correspond to the TIP3P, SPC, SPC/E
force fields or to any other published parameters for water.

Chapter 8: Molecular structure and potential energy — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


# empirical constants (kcal/mol/Å² and kcal/mol/rad²) — didactic values
k_b = 1000.0     # O-H bond constant
k_t = 100.0      # H-O-H angle constant


def U(coord: np.ndarray) -> float:
    r = coord.reshape(3, 3)
    rOH1 = np.linalg.norm(r[0] - r[1])
    rOH2 = np.linalg.norm(r[2] - r[1])
    u = (r[0] - r[1]) / rOH1
    v = (r[2] - r[1]) / rOH2
    theta = np.arccos(np.clip(u @ v, -1, 1))
    return 0.5*k_b*((rOH1-0.96)**2 + (rOH2-0.96)**2) + 0.5*k_t*(theta - 1.824)**2


def main() -> None:
    # messy initial guess
    chute = np.array([
        [-0.8,  0.4, 0.0],
        [ 0.0,  0.0, 0.0],
        [ 0.9,  0.5, 0.0],
    ]).flatten()

    resultado = minimize(U, chute, method="L-BFGS-B")
    r_otima = resultado.x.reshape(3, 3)
    rOH1 = np.linalg.norm(r_otima[0] - r_otima[1])
    rOH2 = np.linalg.norm(r_otima[2] - r_otima[1])
    u = (r_otima[0] - r_otima[1]) / rOH1
    v = (r_otima[2] - r_otima[1]) / rOH2
    theta = np.degrees(np.arccos(np.clip(u @ v, -1, 1)))

    print(f"optimal r(O-H1) = {rOH1:.4f} Å    (target 0.96)")
    print(f"optimal r(O-H2) = {rOH2:.4f} Å    (target 0.96)")
    print(f"optimal H-O-H angle = {theta:.2f}°  (target 104.5°)")
    print(f"minimum energy = {resultado.fun:.6e}")

    # Answer key for Exercise 6 (Appendix G): same U, k_b, k_t = 1000, 100,
    # starting from r0 = H(0.9, 0, 0), O(0, 0, 0), H(0, 0.9, 0)
    r0 = np.array([0.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.9, 0.0])  # H, O, H
    res = minimize(U, r0, method="L-BFGS-B")
    R = res.x.reshape(3, 3)
    rOH1 = np.linalg.norm(R[0]-R[1]); rOH2 = np.linalg.norm(R[2]-R[1])
    u = (R[0]-R[1])/rOH1; v = (R[2]-R[1])/rOH2
    theta_min = np.degrees(np.arccos(np.clip(u@v, -1, 1)))
    print(f"answer key: r_OH = {rOH1:.5f} / {rOH2:.5f} Å   θ = {theta_min:.4f}°  "
          f"(θ0 = 1.824 rad = {np.degrees(1.824):.4f}°)")
    # answer key: r_OH = 0.96000 / 0.96000 Å   θ = 104.5075°


if __name__ == "__main__":
    main()
