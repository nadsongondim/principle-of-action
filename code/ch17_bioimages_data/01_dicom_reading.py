"""
Minimal synthetic DICOM: create a Dataset, save it, read it back.

Pedagogically, showing the anatomy of a DICOM file (header with metadata +
pixel_array) is more valuable than loading an opaque third-party file —
and the example runs without any external data, ensuring reproducibility.

Chapter 17: Bioimaging and clinical data — Volume 4 of the series
"The Principle of Action" (Nadson Brito Gondim).

For the complete book, see https://github.com/nadsongondim/principle-of-action
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pydicom
from pydicom.dataset import Dataset, FileMetaDataset
from pydicom.uid import ExplicitVRLittleEndian, generate_uid


def criar_dicom_sintetico(caminho: Path) -> None:
    """Generate a minimal synthetic DICOM (256x256 axial slice with a gradient)."""
    file_meta = FileMetaDataset()
    file_meta.MediaStorageSOPClassUID = "1.2.840.10008.5.1.4.1.1.2"  # CT Image
    file_meta.MediaStorageSOPInstanceUID = generate_uid()
    file_meta.TransferSyntaxUID = ExplicitVRLittleEndian

    ds = Dataset()
    ds.file_meta = file_meta
    ds.PatientName = "Anônimo^Didático"
    ds.PatientID = "PHANTOM-001"
    ds.Modality = "CT"
    ds.StudyDate = "20260525"
    ds.Rows = 256
    ds.Columns = 256
    ds.PixelSpacing = [0.7, 0.7]          # mm/pixel
    ds.BitsAllocated = 16
    ds.BitsStored = 16
    ds.HighBit = 15
    ds.PixelRepresentation = 0
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"

    # synthetic radial gradient — circular "phantom"
    y, x = np.indices((256, 256))
    r = np.sqrt((x - 128) ** 2 + (y - 128) ** 2)
    pixels = (1000 + 30 * np.cos(r / 8)).astype(np.uint16)
    ds.PixelData = pixels.tobytes()

    ds.save_as(caminho, write_like_original=False)


def main() -> None:
    destino = Path("dicom_sintetico.dcm")
    criar_dicom_sintetico(destino)

    ds = pydicom.dcmread(destino)
    img = ds.pixel_array
    spacing = (ds.PixelSpacing[0], ds.PixelSpacing[1])

    print(f"Patient: {ds.PatientName}")
    print(f"Modality: {ds.Modality}, dimensions: {ds.Rows}x{ds.Columns}")
    print(f"shape = {img.shape}")
    print(f"spacing = {spacing} mm/pixel")
    print(f"dtype = {img.dtype}")
    print(f"central pixel = {img[128, 128]}")


if __name__ == "__main__":
    main()
