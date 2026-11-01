"""
Hello, NumPy — the first program of the volume.

Chapter 1: Development environment and project organization — Volume 4 of the
series "The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    # Confirms that the workshop works: prints pi via NumPy
    print(np.pi)        # 3.141592653589793

    # NumPy as the foundation — arrays and vectorization
    t = np.linspace(0, 10, 1000)   # 1000 instants between 0 and 10
    x = np.sin(t)                  # the sine of all of them, at once
    print(f"t with {t.size} points; first sine = {x[0]:.4f}")


if __name__ == "__main__":
    main()
