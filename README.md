# Astro Spectral Analysis Pipeline

A compact, reproducible Python pipeline for loading, processing and visualising infrared spectroscopic data. The project is designed as a portfolio-quality example of scientific computing, data handling, code organisation and Git/GitLab workflow.

## Why this project matters

This repository demonstrates the type of technical workflow used in scientific and engineering environments:

- loading structured experimental data;
- validating input data before analysis;
- converting transmittance to absorbance;
- normalising spectral features;
- identifying candidate absorption features automatically;
- producing clean graphical and tabular outputs;
- keeping the workflow reproducible through a single command;
- using automated checks through GitLab CI.

The project is intentionally small, but it is built to professional standards so that it can be discussed confidently on a CV or in an interview.

## Repository structure

```text
astro-spectral-analysis-pipeline/
├── data/
│   └── sample_spectrum.csv
├── docs/
│   └── portfolio_notes.md
├── results/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── load_data.py
│   ├── process_data.py
│   └── plot_results.py
├── tests/
│   └── test_pipeline.py
├── .gitignore
├── .gitlab-ci.yml
├── LICENSE
├── main.py
├── requirements.txt
└── README.md
```

## Method summary

The supplied sample data represent a simple infrared spectrum stored as wavenumber against fractional transmittance. The pipeline converts transmittance to absorbance using:

```text
A = -log10(T)
```

The absorbance values are then normalised between 0 and 1. Candidate absorption features are identified using a transparent local-maximum method, which is deliberately simple enough to audit and explain.

## How to run

Create and activate a Python environment, then install the required packages:

```bash
pip install -r requirements.txt
```

Run the pipeline:

```bash
python main.py
```

The script creates:

```text
results/processed_spectrum.csv
results/identified_features.csv
results/spectrum_analysis.png
```

## Example outputs

The pipeline exports both numerical and graphical results. The most useful output for a portfolio is:

```text
results/spectrum_analysis.png
```

This plot shows the normalised absorbance spectrum with automatically identified candidate absorption features labelled by wavenumber.

## Testing

Run the tests with:

```bash
pytest
```

The tests check that the input data load correctly, that absorbance is calculated, and that candidate absorption features are detected.

## GitLab CI

The included `.gitlab-ci.yml` file runs the tests automatically whenever changes are pushed to GitLab. This is useful because it shows basic familiarity with continuous integration and reproducible development practice.

## CV wording

A concise CV bullet for this project could be:

> Built a reproducible Python spectral-analysis pipeline for infrared data, including data validation, absorbance conversion, automated feature detection, visualisation with Matplotlib, unit testing and GitLab CI integration.

A stronger version for technical roles could be:

> Developed a portfolio-grade scientific Python workflow for infrared spectroscopy analysis, demonstrating structured data ingestion, numerical processing, automated plotting, pytest-based validation and CI/CD using GitLab.

## Technologies used

- Python
- pandas
- NumPy
- Matplotlib
- pytest
- Git / GitLab
- GitLab CI/CD

## Licence

This project is provided under the MIT Licence.
