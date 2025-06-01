WITH energy AS (
    SELECT * FROM {{ ref('stg_energy')}}
)
SELECT
*
FROM energy
WHERE RIGHT(msn, 2) = 'US'
AND units ILIKE 'Million Kilowatts'
AND series_description ILIKE '%capacity%'