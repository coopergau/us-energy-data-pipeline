SELECT 
  CAST("period" AS INT) AS year,
  "sectorId" AS sector_id,
  "sector-name" AS sector_name,
  "fuelId" AS fuel_id,
  "fuel-name" AS fuel_name,
  "stateId" AS state_id,
  "state-name" AS state_name,
  CAST("value" AS FLOAT) AS value,
  "value-units" AS value_units
FROM {{ source('raw_carbon_emissions', 'CARBON_EMISSIONS') }}
WHERE state_id != 'US'