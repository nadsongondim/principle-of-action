"""
Nodule volume quantification on CT — simple threshold within an ROI
+ labeling (Example 1).

The synthetic volume mimics a chest: aerated lung (~ -850 HU), a soft-tissue
nodule (~ +40 HU) and the chest wall (also soft tissue) at the edge.
The -400 HU threshold separates soft tissue from aerated lung; the ROI around
the nodule keeps the chest wall out of the segmentation.

Chapter 17: Bioimaging and clinical data — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
from scipy.ndimage import label


def main() -> None:
    # img: 3D array in Hounsfield units — here we use a didactic synthetic volume
    rng = np.random.default_rng(0)
    img = np.full((40, 60, 60), -850.0)   # aerated lung
    img[:, :, :6] = 40.0                  # chest wall (soft tissue)
    img[15:25, 25:40, 25:40] = 40.0       # nodule (soft tissue)
    img += rng.normal(0, 10, img.shape)

    # roi: boolean mask around the nodule (box with a margin)
    roi = np.zeros(img.shape, dtype=bool)
    roi[10:30, 20:45, 20:45] = True

    spacing_x = spacing_y = 0.7        # mm/pixel
    spacing_z = 1.0                     # mm between slices

    # img: 3D array in Hounsfield units; roi: boolean mask around the nodule
    mascara = (img > -400) & roi              # soft tissue vs. aerated lung
    componentes, n = label(mascara)
    volumes_ml = []
    for c in range(1, n+1):
        n_vox = (componentes == c).sum()
        v_mm3 = n_vox * spacing_x * spacing_y * spacing_z
        volumes_ml.append(v_mm3 / 1000.0)

    print(f"components detected: {n}")
    for i, v in enumerate(volumes_ml, start=1):
        print(f"  component {i}: {v:.3f} mL")


if __name__ == "__main__":
    main()
