# Chapter 20 — Real-world data, interoperability and security

> This directory contains the runnable examples for Chapter 20 of Volume 4 of the series
> *The Principle of Action*. For the complete book, see the root of the repository.

## Contents

- `01_pydicom_basics.py` — reads a DICOM file and prints its essential identifiers.
- `02_longitudinal_labs.py` — slices a laboratory series by LOINC code in pandas.
- `03_fhir_query.py` — FHIR REST query for fasting blood glucose observations.
- `04_selection_bias.py` — assesses the age distribution of a dataset to detect selection bias.

## How to run

Install the requirements (see `requirements.txt` at the root) and run:

    python 01_pydicom_basics.py
    python 02_longitudinal_labs.py
    python 03_fhir_query.py
    python 04_selection_bias.py
