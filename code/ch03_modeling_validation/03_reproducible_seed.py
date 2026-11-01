"""
Computational reproducibility — fixing the seed of the random generator.

Chapter 3: Modeling, Validation and Reproducibility — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    rng = np.random.default_rng(42)        # fixed seed: reproducible result
    amostras = rng.normal(loc=0.0, scale=1.0, size=5)
    print("samples (seed 42):", amostras)

    # rerunning with the same seed returns the same sequence
    rng2 = np.random.default_rng(42)
    amostras2 = rng2.normal(loc=0.0, scale=1.0, size=5)
    print("are they equal?", np.allclose(amostras, amostras2))


if __name__ == "__main__":
    main()
