select * from {{ source('raw_carbon', 'RAW_CARBON_EMISSIONS') }} limit 10
