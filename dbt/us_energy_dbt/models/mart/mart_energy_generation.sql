WITH energy AS (
    SELECT * FROM {{ ref('stg_energy')}}
)
SELECT
*
FROM energy
WHERE RIGHT(msn, 2) = 'US'
AND units ILIKE 'Million Kilowatthours'
AND series_description ILIKE '%generation%'