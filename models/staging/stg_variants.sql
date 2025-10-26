{{ config(materialized='view') }}

select
    chromosome,
    position,
    ref,
    alt,
    quality,
    allele_frequency
from read_csv('data/raw/variants.csv', header=true)
where chromosome = 'chr11'
