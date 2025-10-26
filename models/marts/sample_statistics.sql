{{ config(materialized='table') }}

select
    population,
    count(*) as sample_count,
    sum(case when has_diabetes then 1 else 0 end) as diabetic_count,
    round(100.0 * sum(case when has_diabetes then 1 else 0 end) / count(*), 2) as diabetes_percentage,
    round(avg(age), 2) as avg_age
from {{ ref('stg_samples') }}
group by population
order by sample_count desc
