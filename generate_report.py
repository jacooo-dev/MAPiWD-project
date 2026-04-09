import subprocess
import sys
from pathlib import Path


def generate_report(notebook_name: str = "01_analiza_danych"):
    notebooks_dir = Path("notebooks")
    reports_dir = Path("reports")
    notebook_path = notebooks_dir / f"{notebook_name}.ipynb"

    if not notebook_path.exists():
        print(f"Notebook not found: {notebook_path}")
        sys.exit(1)

    print(f"Generating report from {notebook_path}...")

    # HTML without code (clean report)
    subprocess.run([
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "html",
        "--no-input",
        "--output-dir", str(reports_dir),
        str(notebook_path),
    ], check=True)

    print(f"Report: {reports_dir / f'{notebook_name}.html'}")

    # HTML with code
    subprocess.run([
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "html",
        "--output", f"{notebook_name}_full.html",
        "--output-dir", str(reports_dir),
        str(notebook_path),
    ], check=True)

    print(f"Report (with code): {reports_dir / f'{notebook_name}_full.html'}")


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "01_analiza_danych"
    generate_report(name)
