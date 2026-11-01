"""
Uncertainty propagation via Monte Carlo — a prediction is a range, not a point.

The generator seed is fixed (seed 42, as in the book) to guarantee that
every run reproduces exactly the same range and the same histogram — the
reproducibility principle discussed in Chapter 3, §3.5. Sampled values of
k <= 0 are discarded (k < 0 would be growth, not decay).

Chapter 2: Essential numerical methods — Volume 4 of the series "The Principle
of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    y0 = 1.0
    t_alvo = 5.0

    # uncertain k: "around 0.3 with a margin of 0.1"
    rng = np.random.default_rng(42)           # fixed seed: reproducible range
    ks = rng.normal(0.3, 0.1, size=10_000)
    ks = ks[ks > 0]                           # k < 0 would be growth, not decay
    y_em_t = y0 * np.exp(-ks * t_alvo)        # a distribution of results
    faixa = np.percentile(y_em_t, [5, 95])    # the 90% range

    print(f"median = {np.median(y_em_t):.4f}")
    print(f"90% range = [{faixa[0]:.4f}, {faixa[1]:.4f}]")

    fig, ax = plt.subplots()
    ax.hist(y_em_t, bins=60)
    ax.axvline(faixa[0], color="red", linestyle="--", label="p5")
    ax.axvline(faixa[1], color="red", linestyle="--", label="p95")
    ax.set_xlabel(f"y at t = {t_alvo}")
    ax.set_ylabel("frequency")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    main()
