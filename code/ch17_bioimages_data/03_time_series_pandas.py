"""
Laboratory time series with pandas — moving average smoothing fasting glucose.

Chapter 17: Bioimaging and clinical data — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    # generate a synthetic CSV if no real file is available
    rng = np.random.default_rng(0)
    datas = pd.date_range("2024-01-01", periods=200, freq="3D")
    glic = 90 + 10*np.sin(np.arange(200)/8) + rng.normal(0, 5, 200)
    df = pd.DataFrame({"data": datas, "glicose_jejum": glic})

    df.to_csv("paciente_001_labs.csv", index=False)

    df = pd.read_csv("paciente_001_labs.csv", parse_dates=["data"])
    df = df.set_index("data")
    glicose = df["glicose_jejum"]
    media_movel = glicose.rolling(window=30, min_periods=3).mean()

    print(media_movel.tail())


if __name__ == "__main__":
    main()
