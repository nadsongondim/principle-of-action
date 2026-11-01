"""
Skeleton of a Bayesian update of PK parameters (Example 1).

Implements the skeleton referenced in the chapter: Gaussian prior on
(log CL, log V), likelihood based on a one-compartment PK model
and update via the Laplace approximation — the posterior is locally
Gaussian, with its mean at the MAP and covariance given by the inverse of
the Hessian of the negative log-posterior.

Book scenario (v1.1): vancomycin in a 70 kg adult; population prior
CL = 6.0 L/h (±1.8; log SD 0.30) and V = 0.7 L/kg (log SD 0.14);
peak of 25 mg/L 1 h after the dose and trough of 8 mg/L 11 h after the peak
(before the next dose, 12 h interval). The 900 mg every 12 h dose is the one
that, with these measurements, brings the likelihood to the point cited in the
text: k = ln(25/8)/11 ≈ 0.10 1/h (t½ ≈ 6.7 h), V ≈ 0.65 L/kg (≈ 45 L) and
CL = kV ≈ 4.7 L/h — clearance reduced relative to the prior.

Chapter 19: Prototype of a physiological digital twin — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from typing import Callable

import numpy as np
from scipy.optimize import minimize


PESO_KG = 70.0

# Gaussian prior on (log CL, log V)
mu_prior = np.array([np.log(6.0), np.log(0.7)])
cov_prior = np.diag([0.30**2, 0.14**2])

# nominal residual error of the measurements (mg/L) — peak and trough
sigma_obs = 2.0


def previsao_pico_vale(theta: np.ndarray, esquemas: dict) -> tuple[float, float]:
    """One-compartment IV (bolus) model with repeated doses at steady state."""
    CL = np.exp(theta[0])                       # L/h
    V = np.exp(theta[1]) * esquemas["peso_kg"]  # L/kg × kg = L
    dose, tau = esquemas["dose_mg"], esquemas["intervalo_h"]
    k = CL / V
    c_logo_apos = (dose / V) / (1.0 - np.exp(-k * tau))
    pico = c_logo_apos * np.exp(-k * esquemas["t_pico_h"])
    vale = c_logo_apos * np.exp(-k * tau)
    return pico, vale


def verossimilhanca(theta: np.ndarray, medidas: dict, esquemas: dict) -> float:
    """Gaussian negative log-likelihood (chi^2 / 2) of the peak and trough measurements."""
    pico_pred, vale_pred = previsao_pico_vale(theta, esquemas)
    chi2 = ((medidas["pico_mg_L"] - pico_pred) ** 2
            + (medidas["vale_mg_L"] - vale_pred) ** 2) / sigma_obs**2
    return 0.5 * chi2


def atualizar(mu_prior: np.ndarray, cov_prior: np.ndarray,
              verossimilhanca: Callable[..., float],
              medidas: dict, esquemas: dict) -> tuple[np.ndarray, np.ndarray]:
    """Laplace approximation: minimize -log p(θ|y) and use the Hessian."""
    def neg_log_posterior(theta: np.ndarray) -> float:
        delta = theta - mu_prior
        quad_prior = delta @ np.linalg.solve(cov_prior, delta)
        return verossimilhanca(theta, medidas, esquemas) + 0.5 * quad_prior

    resultado = minimize(neg_log_posterior, x0=mu_prior, method="BFGS")
    mu_post = resultado.x
    # BFGS returns an estimate of the inverse Hessian — the Laplace covariance
    cov_post = resultado.hess_inv
    return mu_post, cov_post


def main() -> None:
    medidas = {"pico_mg_L": 25.0, "vale_mg_L": 8.0}
    esquemas = {"dose_mg": 900, "intervalo_h": 12, "t_pico_h": 1.0,
                "peso_kg": PESO_KG}

    # direct reading of the two measurements (what the likelihood "points to")
    k = np.log(medidas["pico_mg_L"] / medidas["vale_mg_L"]) / 11.0
    fator = np.exp(-k * esquemas["t_pico_h"]) / (1 - np.exp(-k * esquemas["intervalo_h"]))
    V_L = esquemas["dose_mg"] * fator / medidas["pico_mg_L"]
    print(f"likelihood: k = {k:.4f} 1/h  t½ = {np.log(2)/k:.2f} h  "
          f"V = {V_L:.1f} L ({V_L/PESO_KG:.2f} L/kg)  CL = {k*V_L:.2f} L/h")
    # k ≈ 0.10 1/h, t½ ≈ 6.7 h, V ≈ 45 L (0.65 L/kg), CL ≈ 4.7 L/h

    posterior_mu, posterior_cov = atualizar(mu_prior, cov_prior,
                                            verossimilhanca, medidas, esquemas)
    desvios = np.sqrt(np.diag(posterior_cov))

    print("prior     CL ≈ {:.3f} L/h   V ≈ {:.3f} L/kg".format(
        np.exp(mu_prior[0]), np.exp(mu_prior[1])))
    print("posterior mu (log CL, log V):", posterior_mu)
    print("posterior CL ≈ {:.3f} L/h   (sigma log = {:.3f})".format(
        np.exp(posterior_mu[0]), desvios[0]))
    print("posterior V  ≈ {:.3f} L/kg  (sigma log = {:.3f})".format(
        np.exp(posterior_mu[1]), desvios[1]))


if __name__ == "__main__":
    main()
