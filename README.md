# Predykcja cen mieszkan - MAPiWD

Projekt zaliczeniowy z przedmiotu "Metody analizy, przetwarzania i wizualizacji danych".

**Zespol:** Jakub Nowosad, Lukasz Iwanek, Piotr Bialas

## Temat

Analiza i predykcja cen nieruchomosci na podstawie Ames Housing Dataset (~1460 domow, 80 atrybutow).

## Wymagania

- Python 3.11+
- [Poetry](https://python-poetry.org/)

## Setup

```bash
poetry install
```

## Pobranie danych

```bash
poetry run python src/download_data.py
```

Dane laduja sie do `data/ames_housing.csv`.

## Notebooki

Notebooki sa w katalogu `notebooks/`. Zeby je odpalic:

```bash
poetry run jupyter notebook
```

| Notebook | Opis |
|----------|------|
| `01_analiza_danych.ipynb` | Raport 1 - import danych, struktura, pierwsze wizualizacje |

## Generowanie raportow

```bash
poetry run python generate_report.py
```

Generuje dwa pliki HTML w `reports/`:
- `01_analiza_danych.html` - raport bez kodu (do oddania)
- `01_analiza_danych_full.html` - raport z kodem

Mozna tez podac nazwe notebooka jako argument:

```bash
poetry run python generate_report.py 02_przetwarzanie
```

## Struktura projektu

```
├── data/                  # datasety (git-ignored)
├── notebooks/             # jupyter notebooki
├── src/                   # skrypty pomocnicze
├── reports/               # wygenerowane raporty HTML
│   └── figures/           # wykresy PNG
├── generate_report.py     # skrypt do generowania raportow
└── pyproject.toml         # konfiguracja Poetry
```
