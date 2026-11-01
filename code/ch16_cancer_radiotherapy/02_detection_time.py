"""
Time from genesis to detection by imaging (Example 1).

Chapter 16: Cancer, targeted therapies and radiotherapy — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np


def main() -> None:
    r = 0.007
    N0, N_det = 1, 1e9
    t_det = np.log(N_det/N0) / r
    # t_det ≈ 2960 days ≈ 8 years
    print(f"t_detection ≈ {t_det:.0f} days ≈ {t_det/365:.1f} years")


if __name__ == "__main__":
    main()
