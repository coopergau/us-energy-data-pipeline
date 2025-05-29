WITH emissions AS (
    SELECT * FROM {{ ref('stg_emissions')}}
)
SELECT 
DISTINCT *
FROM emissions
WHERE state_id = 'US'