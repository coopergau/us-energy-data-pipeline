# US Energy and Carbon Emissions Data Pipeline

## Overview
ELT pipeline processing US energy and carbon emissions data from the U.S. Energy Information Administration (EIA) using Python, Snowflake, dbt, and Power BI.
The data includes:
- Energy generation, capacity, and consumption
- Foreign imports and exports of natural gas and petroleum
- Annual cooling degree days and heating degree days
- National and State carbon emissions

## Tools
- Python (data extraction) - Complete
- Snowflake (data loading) - Complete
- dbt (data transformating) - Complete
- Power BI (visualisations) - in progress

## Pipeline Flow
1. (Extract) Python was used to extract the data via the EIA API. Due to the API rates, the data had to be extracted in multiple seperate chunks which were then joined together as pandas dataframes. The initial raw dataframes where energy and emissions.
2. (Load) The raw dataframes where loaded into Snowflake using the python Snowflake connector library.
3. (Transform) Within Snowflake, dbt was used to transform the raw dataframes into stagin models by typecasting certain columns and testing for null values.
4. (Transform) Dbt was again used to split the large staging models into the more specific and organized mart models.
5. (Vizualise) The mart models were loaded into Power BI and analyzed in a series of dashboards.

