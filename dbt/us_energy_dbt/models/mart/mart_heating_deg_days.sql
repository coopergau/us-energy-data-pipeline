WITH energy AS (
    SELECT * FROM {{ ref('stg_energy')}}
)
SELECT
*
FROM energy
WHERE series_description ILIKE '%Heating Degree-Days%'