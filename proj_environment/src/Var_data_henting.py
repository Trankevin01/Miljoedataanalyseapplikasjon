import requests
import pandas as pd
from geopy.distance import geodesic
from datetime import datetime, timedelta

class WeatherDataFetcher:
    def __init__(self, client_id, observations_endpoint, stations_endpoint):
        self.client_id = client_id
        self.observations_endpoint = observations_endpoint
        self.stations_endpoint = stations_endpoint

    def fetch_stations(self):
        """Fetch weather stations from the Frost API."""
        parameters = {'types': 'SensorSystem'}
        r = requests.get(self.stations_endpoint, parameters, auth=(self.client_id, ''))
        stations_json = r.json()
        stations = stations_json['data']
        return {station['id']: (station['geometry']['coordinates'][1], station['geometry']['coordinates'][0]) 
                for station in stations if 'geometry' in station}

    def fetch_data_by_element(self, stations, elements, historic_date, current_date, max_attempts=15):
        """Fetch data for each element from the nearest weather stations."""
        all_data = {}
        for element in elements:
            print(f"Henter data for element: {element}")
            for attempt in range(min(max_attempts, len(stations))):
                parameters = {
                    'sources': stations[attempt],
                    'elements': element,
                    'referencetime': f'{historic_date}/{current_date}',
                }
                r = requests.get(self.observations_endpoint, parameters, auth=(self.client_id, ''))
                json = r.json()

                if r.status_code == 200 and 'data' in json:
                    data = json['data']
                    if data:
                        print(f"Data retrieved for {element} from station {stations[attempt]}!")
                        all_data[element] = data
                        break
                else:
                    print(f"Error retrieving {element} data from station {stations[attempt]}. Trying next station...")
            if element not in all_data:
                print(f"No data found for {element} from any of the attempted stations.")
        return all_data

    def process_data(self, data):
        """Process raw data into a Pandas DataFrame."""
        df_list = []
        for element, data_element in data.items():
            for item in data_element:
                row = pd.DataFrame(item['observations'])
                row['referenceTime'] = item['referenceTime']
                row['sourceId'] = item['sourceId']
                row['elementId'] = element
                df_list.append(row)
        df = pd.concat(df_list, ignore_index=True)
        df['referenceTime'] = pd.to_datetime(df['referenceTime'])
        return df