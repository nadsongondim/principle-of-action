"""
Answer key Ch. 20 — Ex. 6 (Challenge): index a DICOM folder and build a DataFrame.

Appendix G: Answer Key to the Challenge Exercises — Volume 4 of
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
import pydicom


def indexar_pasta_dicom(caminho: str | Path) -> pd.DataFrame:
    linhas = []
    for arq in Path(caminho).rglob("*.dcm"):
        try:
            ds = pydicom.dcmread(arq, stop_before_pixels=True)
        except pydicom.errors.InvalidDicomError:
            continue
        linhas.append({
            "arquivo":      str(arq),
            "paciente_id":  getattr(ds, "PatientID", None),
            "paciente_nome": str(getattr(ds, "PatientName", "")),
            "estudo_data":  getattr(ds, "StudyDate", None),
            "modalidade":   getattr(ds, "Modality", None),
            "linhas":       getattr(ds, "Rows", None),
            "colunas":      getattr(ds, "Columns", None),
            "espessura":    getattr(ds, "SliceThickness", None),
            "pixel_mm":     getattr(ds, "PixelSpacing", None),
            "estudo_uid":   getattr(ds, "StudyInstanceUID", None),
        })
    df = pd.DataFrame(linhas)
    if not df.empty:
        df["estudo_data"] = pd.to_datetime(df["estudo_data"],
                                           format="%Y%m%d", errors="coerce")
    return df


def main() -> None:
    df = indexar_pasta_dicom("./dados_dicom")
    print(df.head() if not df.empty else "(empty folder or no DICOM files)")


if __name__ == "__main__":
    main()
