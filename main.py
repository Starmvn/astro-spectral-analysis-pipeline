"""Run the full spectral analysis pipeline.

The script loads a sample infrared spectrum, converts transmittance to
absorbance, normalises the result, identifies candidate absorption features and
exports both numerical and graphical outputs.
"""

from pathlib import Path
from src.load_data import load_spectrum
from src.process_data import process_spectrum
from src.plot_results import plot_spectrum

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / "data" / "sample_spectrum.csv"
RESULTS_DIR = PROJECT_ROOT / "results"


def main() -> None:
    spectrum = load_spectrum(DATA_PATH)
    processed, features = process_spectrum(spectrum)

    RESULTS_DIR.mkdir(exist_ok=True)
    processed.to_csv(RESULTS_DIR / "processed_spectrum.csv", index=False)
    features.to_csv(RESULTS_DIR / "identified_features.csv", index=False)
    plot_path = plot_spectrum(processed, features, RESULTS_DIR / "spectrum_analysis.png")

    print("Spectral analysis complete.")
    print(f"Processed spectrum: {RESULTS_DIR / 'processed_spectrum.csv'}")
    print(f"Identified features: {RESULTS_DIR / 'identified_features.csv'}")
    print(f"Figure: {plot_path}")


if __name__ == "__main__":
    main()
