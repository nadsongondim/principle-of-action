# Chapter 17 — Bioimaging and clinical data

> This directory contains the runnable examples for Chapter 17 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the root of the repository.

## Contents

- `01_dicom_reading.py` — opens a DICOM file with `pydicom` and reads the `PixelSpacing`.
- `02_image_filters.py` — applies Gaussian and median filters to a synthetic noisy phantom.
- `03_time_series_pandas.py` — moving average of a fasting glucose series in pandas.
- `04_ct_volume_quantification.py` — thresholds a synthetic CT volume and calculates the nodule volume in mL.
- `05_deterioration_time_series.py` — calculates the HR and SBP slopes over the last 24 h.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_dicom_reading.py
    python 02_image_filters.py
    python 03_time_series_pandas.py
    python 04_ct_volume_quantification.py
    python 05_deterioration_time_series.py
