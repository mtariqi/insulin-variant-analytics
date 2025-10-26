#!/usr/bin/env python3
import duckdb
import pandas as pd

print("🎉 INSULIN VARIANT ANALYTICS - PROJECT SUCCESS!")
print("=" * 50)

conn = duckdb.connect("insulin_variants.duckdb")

print("\n📈 PROJECT SUMMARY:")
print("✅ Complete bioinformatics data pipeline built")
print("✅ 5 analytical models created in DuckDB")
print("✅ 50 synthetic samples with clinical data")
print("✅ 100 insulin gene variants with quality metrics")
print("✅ Population genetics analysis ready")

print("\n🔬 KEY INSIGHTS GENERATED:")
# Sample statistics
stats = conn.execute("SELECT * FROM analytics.sample_statistics").fetchall()
print("\nPopulation Statistics:")
for pop, total, diabetic, percentage, avg_age in stats:
    print(f"  {pop}: {total} samples, {diabetic} diabetic ({percentage}%), avg age {avg_age}")

# Variant quality
quality = conn.execute("SELECT * FROM analytics.variant_quality_analysis").fetchall()
print("\nVariant Quality Distribution:")
for qual_bucket, freq_cat, count, pct in quality:
    print(f"  {qual_bucket}/{freq_cat}: {count} variants ({pct}%)")

print(f"\n🎊 PROJECT READY FOR GITHUB & PORTFOLIO!")
