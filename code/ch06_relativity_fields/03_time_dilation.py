"""
Time dilation — five years on the spaceship correspond to eight years on Earth.

Chapter 6: Relativity, fields and electromagnetism — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    beta = 0.8
    gamma = 1.0 / np.sqrt(1.0 - beta**2)
    tempo_nave_anos = 5.0
    tempo_terra_anos = gamma * tempo_nave_anos
    # tempo_terra_anos ≈ 8.33

    print(f"beta = {beta}")
    print(f"gamma = {gamma:.4f}")
    print(f"time on the spaceship: {tempo_nave_anos} years")
    print(f"time on Earth: {tempo_terra_anos:.2f} years")


if __name__ == "__main__":
    main()
