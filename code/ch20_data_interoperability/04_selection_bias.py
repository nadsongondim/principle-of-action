"""
Simple assessment of selection bias — age distribution of the dataset.

Chapter 20: Real-world data, interoperability and security — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    # didactic synthetic dataset: sample skewed toward older adults
    rng = np.random.default_rng(0)
    n = 1000
    idade = rng.normal(72, 12, n).clip(20, 100)
    df = pd.DataFrame({"idade": idade})

    # age and socioeconomic distribution of the dataset
    df["faixa_etaria"] = pd.cut(df.idade, bins=[0, 40, 60, 75, 200],
                                labels=["<=40", "41-60", "61-75", ">75"],
                                include_lowest=True)
    print(df.faixa_etaria.value_counts(normalize=True))

    # compare with population data (IBGE; SUS)
    # ...


if __name__ == "__main__":
    main()
