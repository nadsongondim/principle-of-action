"""
Quick guide — pandas: loading a CSV, filtering and time operations.

Appendix B: Quick Guide to Scientific Python — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    # generates a synthetic teaching file if it does not exist
    rng = np.random.default_rng(0)
    datas = pd.date_range("2024-01-01", periods=120, freq="D")
    valores = 13 + rng.normal(0, 0.7, 120)
    pd.DataFrame({
        "data": datas,
        "exame": ["hemoglobina"] * 120,
        "valor": valores,
    }).to_csv("labs.csv", index=False)

    # load CSV
    df = pd.read_csv('labs.csv', parse_dates=['data'])
    df = df.set_index('data').sort_index()

    # filter
    hb = df[df['exame'] == 'hemoglobina']['valor']

    # time operations
    media_mensal = hb.resample('1ME').mean()
    movimento = hb.rolling('30D').mean()

    print(media_mensal.head())
    print(movimento.tail())


if __name__ == "__main__":
    main()
