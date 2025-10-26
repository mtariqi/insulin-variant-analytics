# 🧬 Insulin Gene Variant Analytics

![Python](https://img.shields.io/badge/Python-3.12-blue)
![DBT](https://img.shields.io/badge/DBT-1.10-orange)
![DuckDB](https://img.shields.io/badge/DuckDB-1.9-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modern bioinformatics data pipeline for analyzing insulin gene variants using DBT, DuckDB, and Python.

## 📊 Project Overview

This project demonstrates a complete data engineering pipeline for genomic data analysis:

- **Data Generation**: Synthetic insulin gene variants and sample metadata
- **Data Transformation**: DBT models for staging and analytical layers
- **Population Genetics**: Statistical analysis across ethnic groups
- **Quality Assessment**: Automated variant quality categorization

## 🎯 Results Achieved

- ✅ **5 Analytical Models** built with DBT
- ✅ **50 Synthetic Samples** with clinical metadata
- ✅ **100 Insulin Gene Variants** with quality metrics
- ✅ **Population Statistics** across EUR, AFR, EAS populations
- ✅ **Variant Quality Analysis** with categorization

## 🚀 Quick Start

```bash
# Install dependencies
pip install dbt-core dbt-duckdb duckdb pandas numpy

# Generate synthetic data
python scripts/generate_mock_data.py

# Run data transformations
dbt run

# View results
python scripts/demonstrate_success.py

📁 Project Structure
bash

```
insulin-variant-analytics/
├── models/
│   ├── staging/          # Raw data models
│   └── marts/            # Analytical models
├── scripts/
│   ├── generate_mock_data.py
│   └── demonstrate_success.py
├── data/raw/             # Source CSV files
├── analysis/             # Analytical queries
├── dbt_project.yml       # DBT configuration
└── insulin_variants.duckdb # Generated database

```


 Bioinformatics Context
Analyzes variants in the insulin gene region (chr11:2,159,000-2,181,000) including:

Promoter regions affecting gene expression

Exonic regions with protein-coding sequences

Intronic regions involved in splicing

🛠 Technical Stack
Data Transformation: DBT (Data Build Tool)

Database: DuckDB for analytical processing

Programming: Python 3.12 with Pandas

Workflow: Automated ETL pipeline

Version Control: Git with professional structure

📈 Model Architecture

Staging Layer
stg_samples - Patient demographics and clinical data

stg_variants - Genetic variant calls with quality metrics

Analytical Layer
sample_statistics - Population-level summaries

variant_analysis - Aggregated variant metrics

variant_quality_analysis - Quality categorization

👨‍💻 Author
Md Tariqul Islam
Location: Toronto, Canada
GitHub: @mtariqi

Email: tariqul@scired.com


📄 License
This project is licensed under the MIT License.
