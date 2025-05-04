import unittest
import pandas as pd
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'src')))
from Var_data_henting import WeatherDataFetcher

# filepath: c:\Users\Marti\Python\tdt4114\Miljoedataanalyseapplikasjon\proj_environment\src\test_Var_data_henting.py


class TestWeatherDataFetcher(unittest.TestCase):
    def setUp(self):
        # Initialize a WeatherDataFetcher instance (mocking API details)
        self.fetcher = WeatherDataFetcher(client_id="dummy_id", 
                                          observations_endpoint="dummy_endpoint", 
                                          stations_endpoint="dummy_endpoint")

    def test_process_data(self):
        # Mock input data
        mock_data = {
            "temperature": [
                {
                    "observations": [
                        {"value": 15.2, "unit": "Celsius", "quality": "good"},
                        {"value": 14.8, "unit": "Celsius", "quality": "good"}
                    ],
                    "referenceTime": "2023-03-01T12:00:00Z",
                    "sourceId": "station_1"
                }
            ],
            "precipitation": [
                {
                    "observations": [
                        {"value": 0.5, "unit": "mm", "quality": "good"}
                    ],
                    "referenceTime": "2023-03-01T12:00:00Z",
                    "sourceId": "station_2"
                }
            ]
        }

        # Process the mock data
        result_df = self.fetcher.process_data(mock_data)

        # Expected DataFrame structure
        expected_columns = ["value", "unit", "quality", "referenceTime", "sourceId", "elementId"]
        self.assertListEqual(list(result_df.columns), expected_columns)

        # Check the number of rows
        self.assertEqual(len(result_df), 3)

        # Verify specific data points
        self.assertEqual(result_df.iloc[0]["value"], 15.2)
        self.assertEqual(result_df.iloc[0]["unit"], "Celsius")
        self.assertEqual(result_df.iloc[0]["elementId"], "temperature")
        self.assertEqual(result_df.iloc[2]["value"], 0.5)
        self.assertEqual(result_df.iloc[2]["elementId"], "precipitation")

if __name__ == "__main__":
    unittest.main()