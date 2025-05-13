import requests
import pandas as pd
from dotenv import load_dotenv
import os
from snowflake.connector import connect
from snowflake.connector.pandas_tools import write_pandas

def get_data_frame(url, params):
    response = requests.get(url, params=params)
    respone_json = response.json()
    if 'response' in respone_json:
        data_dict = respone_json['response']
        data = data_dict['data']
        
        df = pd.DataFrame(data)
        return df
    else:
        print("Error, no data returned")

def pull_data(starting_year = 2010, ending_year = 2022):
    load_dotenv()
    API_KEY = {
        "api_key": os.getenv("API_KEY"),  
    }

    datasets = [
        {"name": "carbon_emissions", "url": "https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/?frequency=annual&data[0]=value&start=", "table": "CARBON_EMISSIONS"},
        {"name": "energy", "url": "https://api.eia.gov/v2/total-energy/data/?frequency=annual&data[0]=value&start=", "table": "ENERGY"}
    ]

    dataframes = []
    for dataset in datasets:
        df = pd.DataFrame()
        for year in range(starting_year, ending_year):
            url = f"{dataset["url"]}{year}&end={year + 1}&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"
            this_year_df = get_data_frame(url, API_KEY)
            df = pd.concat([df, this_year_df], axis=0, ignore_index=True)
        print(df)
        dataframes.append({"df": df, "table": dataset["table"]})

    return dataframes

def export_to_snowflake(df, table):
    load_dotenv()

    connection = connect(
        user= os.getenv("SNOWFLAKE_USER"),
        password= os.getenv("SNOWFLAKE_PASSWORD"),
        account= os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse='ENERGY_WH',
        database='ENERGY_DB',
        schema='RAW_DATA'
    )

    success, _, _, _ = write_pandas(connection, df, table, auto_create_table=True)

    if not success:
        print(f"error exporting {table} data to Snowflake")


def main():
    dataframes = pull_data()

    for dataframe in dataframes:
        export_to_snowflake(dataframe["df"], dataframe["table"])

if __name__ == "__main__":
    main()