#!/usr/bin/env python3
import pandas as pd
import numpy as np
import os

print("🧬 Generating mock insulin gene variant data...")
os.makedirs("data/raw", exist_ok=True)

# Generate samples
samples = pd.DataFrame({
    "sample_id": [f"SAMPLE_{i:04d}" for i in range(50)],
    "population": np.random.choice(["EUR", "AFR", "EAS"], 50),
    "has_diabetes": np.random.choice([True, False], 50, p=[0.3, 0.7]),
    "age": np.random.randint(25, 75, 50)
})

# Generate variants
variants = pd.DataFrame({
    "chromosome": ["chr11"] * 100,
    "position": np.random.randint(2159000, 2181000, 100),
    "ref": np.random.choice(["A", "C", "T", "G"], 100),
    "alt": np.random.choice(["A", "C", "T", "G"], 100),
    "quality": np.random.normal(40, 10, 100),
    "allele_frequency": np.random.uniform(0, 0.5, 100)
})

samples.to_csv("data/raw/samples.csv", index=False)
variants.to_csv("data/raw/variants.csv", index=False)
print(f"✅ Generated: {len(samples)} samples, {len(variants)} variants")
