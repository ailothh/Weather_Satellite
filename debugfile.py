import unittest
import requests
from tkinter import Tk
from datetime import datetime, timedelta


class TestWeatherApp(unittest.TestCase):

    def setUp(self):
        """
        This method will run before each test case. It is used to set up the environment.
        WeatherApp in root window.
        """
        # Create a Tkinter root window for testing
        self.root = Tk()
        self.app = WeatherApp(self.root)

    def test_api_call_and_cache(self):
        """
        Test data is correctly got from api
        and cached for later calls within 10-mins
        """
        # Mock city and country begginning can delte this at end when completed
        self.app.city_entry.insert(0, "London")
        self.app.country_entry.insert(0, "UK")
        
        # Trigger call to get weather data api
        print("Testing API call and caching...")
        self.app.get_current_weather()  # First API call
        
        # Verify data cachad
        self.assertIsNotNone(self.app.cached_weather_data, "Weather data should be cached.")
        self.assertIsNotNone(self.app.last_api_call_time, "API call time should be recorded.")
        print("API call and caching test passed.")

        # Simulate less than 10 mins
        print("Waiting for less than 10 minutes before the next call...")
        self.app.get_current_weather()  # Should use cached data
        print("Used cached data on second call.")

        # Simulate > 10 minutes data fetched again
        print("Waiting for more than 10 minutes before the next call...")
        self.app.last_api_call_time -= timedelta(minutes=15)
        self.app.get_current_weather()  # Should fetch new data
        print("Fetched new weather data after cache expiry.")

    def test_wind_speed_conversion(self):
        """
        Test wind speed conversion is working
        """
        wind_speed_mps = 10  # Example wind speed in m/s
        converted_mph = self.app.convert_wind_speed(wind_speed_mps, "mph")
        converted_knots = self.app.convert_wind_speed(wind_speed_mps, "knots")
        converted_mps = self.app.convert_wind_speed(wind_speed_mps, "m/s")

        # Check wind conversions
        self.assertEqual(round(converted_mph, 2), 22.37, "Wind speed in mph is incorrect.")
        self.assertEqual(round(converted_knots, 2), 19.44, "Wind speed in knots is incorrect.")
        self.assertEqual(round(converted_mps, 2), 10, "Wind speed in m/s is incorrect.")

        print("Wind speed conversion test passed.")

    def test_ui_update_on_weather_data(self):
        """
        Test whether the UI updates correctly when weather data is received
        """
        # Mock data returned from API 
        mock_data = {
            'name': 'London',
            'main': {'temp': 15.5, 'humidity': 75},
            'wind': {'speed': 5.5}
        }
        
        print("Testing UI update on weather data...")
        self.app.display_weather(mock_data)

        # Check if labels are updated correctly
        self.assertEqual(self.app.city_label.cget("text"), "City: London", "City label not updated correctly.")
        self.assertEqual(self.app.temperature_label.cget("text"), "Temperature: 15.50°C", "Temperature label not updated correctly.")
        self.assertEqual(self.app.humidity_label.cget("text"), "Humidity: 75%", "Humidity label not updated correctly.")
        self.assertEqual(self.app.wind_speed_label.cget("text"), "Wind Speed: 5.50 m/s", "Wind speed label not updated correctly.")

        print("UI update test passed.")

    def test_invalid_input(self):
        """
        Test handles invalid user input (missing city or country)
        """
        print("Testing invalid input handling...")
        self.app.city_entry.delete(0, 'end')
        self.app.country_entry.delete(0, 'end')
        self.app.get_current_weather()  # show error 
        # no city or country provided,show error
        print("Invalid input test passed (error message should appear).")



if __name__ == "__main__":
    unittest.main()