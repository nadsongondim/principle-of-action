"""
Detecting deterioration in vital signs — HR and SBP slopes (Example 2).

Chapter 17: Bioimaging and clinical data — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def main() -> None:
    # generate a synthetic CSV with 48 hours of hourly vital signs
    rng = np.random.default_rng(0)
    datas = pd.date_range("2025-06-01", periods=48, freq="h")
    horas = np.arange(48)
    fc = 80 + 0.4 * horas + rng.normal(0, 3, 48)
    pas = 120 - 0.3 * horas + rng.normal(0, 4, 48)
    df = pd.DataFrame({"data": datas, "fc": fc, "pas_sis": pas})
    df.to_csv("pte_054_vitais.csv", index=False)

    dados = pd.read_csv("pte_054_vitais.csv", parse_dates=["data"])
    dados = dados.set_index("data").rolling("12h").mean()

    # slope of the linear regression over the last 24 hours
    recente = dados[dados.index >= dados.index[-1] - pd.Timedelta("24h")]
    horas = (recente.index - recente.index[0]).total_seconds() / 3600
    slope_fc = np.polyfit(horas, recente["fc"], 1)[0]
    slope_pas = np.polyfit(horas, recente["pas_sis"], 1)[0]

    print(f"HR slope over the last 24 h  = {slope_fc:+.2f} bpm/h")
    print(f"SBP slope over the last 24 h = {slope_pas:+.2f} mmHg/h")


if __name__ == "__main__":
    main()
