# US Energy and Carbon Emissions Data Pipeline

## Notice
This project is near completion. It will be finished upon the addition of the Power BI visuals for the energy consumption, generation, and capacity models, as well as descriptions for them and the other visuals below.

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
- Power BI (visualizations) - in progress

## Pipeline Flow
1. (Extract) Python was used to extract the data via the EIA API. Due to the API rates, the data had to be extracted in multiple seperate chunks which were then joined together as pandas dataframes. The initial raw dataframes where energy and emissions.
2. (Load) The raw dataframes where loaded into Snowflake using the python Snowflake connector library.
3. (Transform) Within Snowflake, dbt was used to transform the raw dataframes into stagin models by typecasting certain columns and testing for null values.
4. (Transform) Dbt was again used to split the large staging models into the more specific and organized mart models.
5. (Visualize) The mart models were loaded into Power BI and analyzed in a series of dashboards.

## Power BI Visualizations

### 1. Carbon Emissions

<img src="power bi/images/carbon_emissions.PNG" width="600" />

### 2. Energy Imports and Exports

<img src="power bi/images/import_export.PNG" width="500" />


### 3. Cooling Degree Days

<img src="power bi/images/cooling_deg_days.PNG" width="500" />


### 4. Heating Degree Days

<img src="power bi/images/heating_deg_days.PNG" width="500" />
