import requests
import pandas as pd
import time

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

def pull_data():
    API_KEY = {
        "api_key": "YKYhWou9rcfs4mKe5ZVemdBCB9YRCqJ8wXtyv45C",  
    }

    CSV_NAMES = ["carbon_emission_data.csv", "energy_data.csv"]

    STARTING_YEAR = 2010
    ENDING_YEAR = 2022

    for name in CSV_NAMES:
        df = pd.DataFrame()
        for year in range(STARTING_YEAR, ENDING_YEAR):
            if name == CSV_NAMES[0]:
                url = f"https://api.eia.gov/v2/co2-emissions/co2-emissions-aggregates/data/?frequency=annual&data[0]=value&start={year}&end={year + 1}&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"
            else:
                url = f"https://api.eia.gov/v2/total-energy/data/?frequency=annual&data[0]=value&start={year}&end={year + 1}&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"

            this_year_df = get_data_frame(url, API_KEY)
            df = pd.concat([df, this_year_df], axis=0, ignore_index=True)
        print(df)
        df.to_csv(name, index=False)

def main():
    pull_data()

if __name__ == "__main__":
    main()