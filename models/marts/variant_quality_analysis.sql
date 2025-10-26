{{ config(materialized='table') }}

with variant_quality as (
    select
        case 
            when quality > 50 then 'high_quality'
            when quality > 20 then 'medium_quality'
            else 'low_quality'
        end as quality_bucket,
        case 
            when allele_frequency < 0.01 then 'rare'
            when allele_frequency < 0.05 then 'low_frequency'
            else 'common'
        end as frequency_category,
        count(*) as variant_count
    from {{ ref('stg_variants') }}
    group by 1,2
)

select
    quality_bucket,
    frequency_category,
    variant_count,
    round(100.0 * variant_count / sum(variant_count) over (), 2) as percentage
from variant_quality
order by quality_bucket, frequency_category
