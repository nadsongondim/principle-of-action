"""
Recalibrating a model with good discrimination and poor calibration.

Implements Platt scaling and isotonic regression to correct systematically
overconfident probabilities.

Chapter 21: Validation, regulation and clinical responsibility — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression


def main() -> None:
    # generate synthetic data: the model discriminates but is overconfident
    rng = np.random.default_rng(0)
    n_treino, n_teste = 800, 400
    y_treino = rng.binomial(1, 0.3, n_treino)
    y_teste = rng.binomial(1, 0.3, n_teste)
    # "inflated" predicted probabilities — overconfident model
    p_preditas_treino = np.clip(y_treino * 0.5 + rng.beta(2, 5, n_treino), 0, 1)
    p_preditas_teste = np.clip(y_teste * 0.5 + rng.beta(2, 5, n_teste), 0, 1)

    # Platt scaling (logistic)
    recalibrador = LogisticRegression()
    recalibrador.fit(p_preditas_treino.reshape(-1, 1), y_treino)
    p_corrigidas = recalibrador.predict_proba(p_preditas_teste.reshape(-1, 1))[:, 1]

    # Alternative: isotonic (more flexible)
    iso = IsotonicRegression(out_of_bounds='clip')
    iso.fit(p_preditas_treino, y_treino)
    p_corrigidas_iso = iso.transform(p_preditas_teste)

    print(f"mean predicted (original) = {p_preditas_teste.mean():.3f}")
    print(f"mean predicted (Platt)    = {p_corrigidas.mean():.3f}")
    print(f"mean predicted (isotonic) = {p_corrigidas_iso.mean():.3f}")
    print(f"observed frequency        = {y_teste.mean():.3f}")


if __name__ == "__main__":
    main()
