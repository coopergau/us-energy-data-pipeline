SELECT 
DISTINCT *
FROM {{ source('raw_carbon', 'RAW_CARBON_EMISSIONS') }}
WHERE state_id != 'US'