WITH emissions AS (
    SELECT * FROM {{ ref('stg_emissions')}}
)
SELECT 
DISTINCT *
FROM {{ source('raw_carbon_emissions', 'CARBON_EMISSIONS') }}
WHERE state_id = 'US'