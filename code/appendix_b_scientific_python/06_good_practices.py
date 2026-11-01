"""
Recurring good practices — seeding the random generator.

Appendix B: Quick Guide to Scientific Python — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    # Seed the random generators for reproducibility (chapter 3)
    rng = np.random.default_rng(42)
    amostras = rng.normal(0, 1, 5)
    print("reproducible samples:", amostras)


if __name__ == "__main__":
    main()
