{{ config(materialized='table') }}

select
    v.chromosome,
    v.position,
    v.ref,
    v.alt,
    v.quality,
    v.allele_frequency,
    count(s.sample_id) as sample_count,
    round(avg(v.quality), 2) as avg_quality
from {{ ref('stg_variants') }} v
cross join {{ ref('stg_samples') }} s
group by 1,2,3,4,5,6
order by v.quality desc
