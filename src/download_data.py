from sklearn.datasets import fetch_openml
import pandas as pd
from pathlib import Path


def download_ames_housing():
    data_dir = Path(__file__).parent.parent / "data"
    output_path = data_dir / "ames_housing.csv"

    if output_path.exists():
        print(f"Dataset already exists: {output_path}")
        return output_path

    print("Downloading Ames Housing dataset from OpenML...")
    housing = fetch_openml(name="house_prices", version=1, as_frame=True)

    df = housing.frame
    print(f"Downloaded {len(df)} rows, {len(df.columns)} columns")

    df.to_csv(output_path, index=False)
    print(f"Saved to {output_path}")
    return output_path


if __name__ == "__main__":
    download_ames_housing()
