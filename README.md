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

<img src="power bi/images/energy_generation.PNG" width="600" />

It can be seen that the overall energy generation has stayed relatively consistent over the 12 years, but there have been some significant changes within specific energy categories.
fossil fuel generation has subtly decreased, while there has been a significant increase in the generation of renewable energy sources. Despite this, natural gas generation has increased over 70 % and fossil fuels are still much more dominant than renewable sources. Nuclear is also shown maintining a steady generation. Note that wood and waste can have different environental impacts than low-carbon sources like solar, wind, geothermal, and hydro, so they have not been included as renewable sources.

### 2. Carbon Emissions

<img src="power bi/images/carbon_emissions.PNG" width="600" />

The carbon emission data is for petroleum, coal, and natural gas. Over the 12 year period, emissions from natural gas have significantly increased while emissions from coal have significantly decreased. Emissions from petroleum have decreased slightly when comparing the 2022 value to 2010, but the line chart shows that the emissions have essentially stayed consistent. Overall there is a slight downtrend in carbon emissions. It can also be seen that Texas has produced almost double the emissions than any other state. California has also produced noticeably more emissions than other states. The Map displays that other than Texas and California the northeast states have produced slightly more emissions that the rest of the country.

### 3. Energy Imports and Exports

<img src="power bi/images/imports_exports.PNG" width="600" />

For the imports and exports page it might be tempting to compare the absolute numbers of natural gas data and petroleum data but this can be misleading. Natural gas is measured in billion cubic feet and petroleum is measured in thousand barrels per day. Instead this page can be used to analyze the difference between imports and exports for a given fuel and how that ratio has changed over time. It can be seen that in 2010 the natural gas imports were more than double their exports, but in 2022 they were less than half due to a drastic increase in exports. Similarly, in 2010 petroleum imports were roughly six times greater than their exports, but in 2022 there were slightly less imports than exports, primarily due to the increase in exports. This data is also depicted based on country, where unsurprisingly, Canada and Mexico are the top two nations whenit comes to trading these resources with the US.

### 4. Cooling Degree Days

<img src="power bi/images/cooling_deg_days.PNG" width="600" />

### 5. Heating Degree Days

<img src="power bi/images/heating_deg_days.PNG" width="600" />
