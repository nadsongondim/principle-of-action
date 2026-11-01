"""
Slicing a laboratory series — filtering by LOINC code and by patient.

Chapter 20: Real-world data, interoperability and security — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

If there is no ``labs.csv`` in the longitudinal format (columns paciente_id,
codigo_loinc, valor, unidade, data, ref_inf, ref_sup) in the current directory,
the script generates an equivalent synthetic table in memory — so it runs without
external data and does not clash with the differently formatted ``labs.csv``
written by other examples (Appendix B, Ch. 17).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

COLUNAS = ["paciente_id", "codigo_loinc", "valor", "unidade", "data",
           "ref_inf", "ref_sup"]


def labs_sinteticos(seed: int = 42) -> pd.DataFrame:
    """Synthetic longitudinal table: Hb (718-7) and creatinine (2160-0)."""
    rng = np.random.default_rng(seed)
    linhas = []
    for paciente in (12345, 67890):
        # irregular sampling: tests ordered when indicated
        dias = np.sort(rng.choice(np.arange(0, 180), size=12, replace=False))
        datas = pd.Timestamp("2024-01-01") + pd.to_timedelta(dias, unit="D")
        for d in datas:
            linhas.append((paciente, "718-7", round(rng.normal(12.8, 0.6), 1),
                           "g/dL", d, 12.0, 16.0))
            linhas.append((paciente, "2160-0", round(rng.normal(1.1, 0.15), 2),
                           "mg/dL", d, 0.7, 1.3))
    return pd.DataFrame(linhas, columns=COLUNAS)


def carregar_labs(caminho: str = "labs.csv") -> pd.DataFrame:
    arquivo = Path(caminho)
    if arquivo.exists():
        df = pd.read_csv(arquivo, parse_dates=["data"])
        if set(COLUNAS) <= set(df.columns):
            df["codigo_loinc"] = df["codigo_loinc"].astype(str)
            return df
        print(f"{caminho} exists but is not in the expected longitudinal "
              "format; using synthetic data.")
    return labs_sinteticos()


def main() -> None:
    df = carregar_labs("labs.csv")
    # columns: paciente_id (patient), codigo_loinc, valor (value), unidade (unit), data (date), ref_inf, ref_sup (reference limits)
    hb = df[(df.codigo_loinc == "718-7") & (df.paciente_id == 12345)]
    hb = hb.set_index("data").sort_index()
    print(hb.tail())


if __name__ == "__main__":
    main()
