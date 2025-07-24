# US Energy and Carbon Emissions Data Pipeline

## Overview
ELT pipeline for processing US energy and carbon emissions data from the U.S. Energy Information Administration (EIA) using Python, Snowflake, dbt, and Power BI.
The data includes:
- Energy generation
- Foreign imports and exports of natural gas and petroleum
- National cooling degree days and heating degree days
- National and State carbon emissions

## Pipeline Flow
1. (Extract) Python was used to extract the data via the EIA API. Due to the API rates, the data had to be extracted in multiple seperate chunks which were then joined together as pandas dataframes. The initial raw dataframes where energy and emissions.
2. (Load) The raw dataframes where loaded into Snowflake using the python Snowflake connector library.
3. (Transform) Within Snowflake, dbt was used to transform the raw dataframes into stagin models by typecasting certain columns and testing for null values.
4. (Transform) Dbt was again used to split the large staging models into the more specific and organized mart models.
5. (Visualize) The mart models were loaded into Power BI and analyzed in a series of dashboards.

## Power BI Visualizations

### 1. Energy Generation

It can be seen that the overall energy generation has stayed relatively consistent over the 12 years, but there have been some significant changes within specific energy categories.
fossil fuel generation has subtly decreased, while there has been a significant increase in the generation of renewable energy sources. Despite this, natural gas generation has increased over 70 % and fossil fuels are still much more dominant than renewable sources. Nuclear is also shown maintining a steady generation. Note that wood and waste can have different environental impacts than low-carbon sources like solar, wind, geothermal, and hydro, so they have not been included as renewable sources.
<img src="power bi/images/energy_generation.PNG" width="600" />

### 2. Carbon Emissions

<img src="power bi/images/carbon_emissions.PNG" width="600" />

### 3. Energy Imports and Exports

<img src="power bi/images/imports_exports.PNG" width="600" />

### 4. Cooling Degree Days

<img src="power bi/images/cooling_deg_days.PNG" width="600" />

### 5. Heating Degree Days

<img src="power bi/images/heating_deg_days.PNG" width="600" />
