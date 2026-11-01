"""
FHIR REST query for fasting blood glucose observations (LOINC 1558-6).

Chapter 20: Real-world data, interoperability and security — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import os

import pandas as pd
import requests


def main() -> None:
    token = os.environ.get("FHIR_TOKEN", "<insert_token>")
    url = "https://fhir.exemplo.br/api/Observation"
    params = {
        "patient": "12345",
        "code": "1558-6",
        "date": "ge2025-12-01",
        "_sort": "date",
        "_count": 100,
    }
    resposta = requests.get(url, params=params, headers={
        "Accept": "application/fhir+json",
        "Authorization": f"Bearer {token}",
    })
    bundle = resposta.json()
    linhas = [
        {
            "data": e["resource"]["effectiveDateTime"],
            "valor": e["resource"]["valueQuantity"]["value"],
            "unidade": e["resource"]["valueQuantity"]["unit"],
        }
        for e in bundle.get("entry", [])
    ]
    df = pd.DataFrame(linhas)
    df["data"] = pd.to_datetime(df["data"])
    print(df.head())


if __name__ == "__main__":
    main()
