SELECT 
  CAST("period" AS INT) AS year,
  "msn" as msn,
  "seriesDescription" AS series_description,
  CAST("value" AS FLOAT) AS value,
  "unit" AS units
FROM {{ source('raw_energy', 'ENERGY') }}
WHERE "value" != 'No Data Reported'
AND "value" != 'Not Applicable'
AND "value" != 'Not Available'
AND "value" != 'Withheld'
