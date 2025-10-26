{{ config(materialized='view') }}

select
    sample_id,
    population,
    has_diabetes,
    age
from read_csv('data/raw/samples.csv', header=true)
