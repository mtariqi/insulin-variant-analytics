# Insulin Gene Variant Analytics

A modern bioinformatics pipeline for analyzing insulin gene variants using DBT, DuckDB, and Python.

## 🧬 Project Overview

This project implements a complete genomic data engineering pipeline for insulin gene variant analysis:

- **Data Generation**: Synthetic insulin gene variants with clinical metadata
- **Data Transformation**: DBT models for staging and analytical layers  
- **Population Genetics**: Statistical analysis across ethnic groups
- **Quality Assessment**: Automated variant quality categorization

## 📊 Results Achieved

- ✅ Analytical models built with DBT
- ✅ Synthetic samples with clinical metadata
- ✅ Insulin gene variants with quality metrics
- ✅ Population statistics across EAS, SAS populations
- ✅ Variant quality analysis with categorization

## 🚀 Quick Start

### Install Dependencies
```bash
pip install dbt-core dbt-duckdb duckdb pandas numpy


Generate Synthetic Data

python scripts/generate_mock_data.py

Run Data Transformations

dbt run

View Results
python scripts/demonstrate_success.py



📁 Project Structure


bash
```
insulin-variant-analytics/
├── models/
│   ├── staging/                 # Raw data models
│   │   ├── stg_samples.sql
│   │   ├── stg_variants.sql
│   │   └── schema.yml
│   └── marts/                   # Analytical models
│       ├── sample_statistics.sql
│       ├── variant_analysis.sql
│       ├── variant_quality_analysis.sql
│       └── schema.yml
├── scripts/
│   ├── generate_mock_data.py
│   └── demonstrate_success.py
├── data/
│   └── raw/                     # Source CSV files
├── tests/                       # Data quality tests
├── analysis/                    # Analytical queries
├── dbt_project.yml              # DBT configuration
├── insulin_variants.duckdb      # Generated database
└── requirements.txt             # Python dependencies
```


🧪 Bioinformatics Context
Analyzes variants in the insulin gene region (chr11:2,159,000-2,181,000) including:

Promoter regions: Affecting gene expression

Exonic regions: Protein-coding sequences

Intronic regions: Involved in splicing

🛠 Technical Stack
Data Transformation: DBT (Data Build Tool)

Database: DuckDB for analytical processing

Programming: Python 3.12 with Pandas

Workflow: Automated ETL pipeline

Version Control: Git with professional structure

🏗 Model Architecture
Staging Layer
stg_samples - Patient demographics and clinical data

stg_variants - Genetic variant calls with quality metrics

Analytical Layer
sample_statistics - Population-level summaries

variant_analysis - Aggregated variant metrics

variant_quality_analysis - Quality categorization

Author: Your Name
Location: Your Location
GitHub: @mtariqi
Email: tariqul@scired.com

📄 License
This project is licensed under the MIT License.
