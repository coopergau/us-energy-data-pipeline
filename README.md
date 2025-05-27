dbt plan:
    from emissions table:
        - total us emissions
        - emissions by state
    from energy table:
        - imports table (filter by msn no ending in 'us')
        - exports table (filter by msn no ending in 'us')
        - energy generation
        - energy capacity

useful for the last two
SELECT
distinct "seriesDescription"
from ENERGY_DB.RAW_DATA.ENERGY
WHERE RIGHT("msn", 2) = 'US'
AND "unit" ILIKE 'Million Kilowatthours'

