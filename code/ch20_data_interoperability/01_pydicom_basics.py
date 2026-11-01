"""
Reading DICOM and extracting identifiers and the pixel matrix.

Chapter 20: Real-world data, interoperability and security — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

If the file ``estudo/serie/slice_042.dcm`` does not exist, the script generates a
minimal synthetic DICOM (a phantom, with no real patient data) in a temporary
directory and reads that file — so the example runs without external data.

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np
import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian, generate_uid


def criar_dicom_sintetico(caminho: Path) -> None:
    """Minimal synthetic DICOM: a 128x128 axial slice of a phantom."""
    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = "1.2.840.10008.5.1.4.1.1.2"  # CT Image
    file_meta.MediaStorageSOPInstanceUID = generate_uid()
    file_meta.TransferSyntaxUID = ExplicitVRLittleEndian

    ds = Dataset()
    ds.file_meta = file_meta
    ds.PatientName = "Anonimo^Didatico"
    ds.PatientID = "PHANTOM-042"
    ds.Modality = "CT"
    ds.StudyDate = "20260525"
    ds.Rows = 128
    ds.Columns = 128
    ds.BitsAllocated = 16
    ds.BitsStored = 16
    ds.HighBit = 15
    ds.PixelRepresentation = 0
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"
    y, x = np.indices((128, 128))
    r = np.sqrt((x - 64) ** 2 + (y - 64) ** 2)
    ds.PixelData = (1000 + 30 * np.cos(r / 6)).astype(np.uint16).tobytes()
    ds.save_as(caminho, write_like_original=False)


def main() -> None:
    caminho = Path("estudo/serie/slice_042.dcm")
    with tempfile.TemporaryDirectory() as tmp:
        if not caminho.exists():
            print(f"{caminho} not found; using a synthetic DICOM.")
            caminho = Path(tmp) / "slice_042.dcm"
            criar_dicom_sintetico(caminho)
        ds = pydicom.dcmread(caminho)
        print(ds.PatientID, ds.StudyDate, ds.Modality)
        img = ds.pixel_array
        print(f"shape = {img.shape}   dtype = {img.dtype}")


if __name__ == "__main__":
    main()
