WITH energy AS (
    SELECT * FROM {{ ref('stg_energy')}}
)
SELECT
*
FROM energy
WHERE series_description ILIKE '%Cooling Degree-Days%'