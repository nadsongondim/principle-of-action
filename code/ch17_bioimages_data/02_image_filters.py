"""
Gaussian and median filters on a synthetic noisy image.

Chapter 17: Bioimaging and clinical data — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter, median_filter


def fantoma(n: int = 200) -> np.ndarray:
    """Create a simple phantom with a background ellipse and two inner objects."""
    y, x = np.mgrid[-1:1:n*1j, -1:1:n*1j]
    img = np.where(x**2/0.7**2 + y**2/0.9**2 < 1, 0.5, 0.0)
    img += np.where((x-0.2)**2 + (y-0.2)**2 < 0.08**2, 0.4, 0.0)
    img += np.where((x+0.3)**2 + (y+0.1)**2 < 0.05**2, -0.2, 0.0)
    return img


def main() -> None:
    rng = np.random.default_rng(0)
    img = fantoma()
    img_ruidosa = img + rng.normal(0.0, 0.08, img.shape)

    img_g = gaussian_filter(img_ruidosa, sigma=1.5)
    img_m = median_filter(img_ruidosa, size=3)

    fig, axes = plt.subplots(1, 4, figsize=(12, 3))
    for ax, dado, titulo in zip(
        axes,
        [img, img_ruidosa, img_g, img_m],
        ["original", "with noise", "Gaussian σ=1.5", "median 3x3"],
    ):
        ax.imshow(dado, cmap="gray")
        ax.set_title(titulo)
        ax.axis("off")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
