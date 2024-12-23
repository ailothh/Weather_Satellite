#Alexander Winkler
import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from PIL import Image, ImageTk  #Pillow for images

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Satellite Mock")
        
        # default window size
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        
        # background image
        self.set_background_image()

        # Weather caching limit api calls 
        self.last_api_call_time = None
        self.cached_weather_data = None

        # UI
        self.city_label = tk.Label(root, text="City: ", fg="white", bg="black")
        self.city_label.pack(pady=5)

        self.city_entry = tk.Entry(root, fg="white", bg="black", insertbackground="white")  # White text cursor
        self.city_entry.pack(pady=5)

        self.state_label = tk.Label(root, text="State (optional): ", fg="white", bg="black")
        self.state_label.pack(pady=5)

        self.state_entry = tk.Entry(root, fg="white", bg="black", insertbackground="white")
        self.state_entry.pack(pady=5)

        self.country_label = tk.Label(root, text="Country: ", fg="white", bg="black")
        self.country_label.pack(pady=5)

        self.country_entry = tk.Entry(root, fg="white", bg="black", insertbackground="white")
        self.country_entry.pack(pady=5)

        self.unit_label = tk.Label(root, text="Choose Temperature Unit: ", fg="white", bg="black")
        self.unit_label.pack(pady=5)

        # Dropdown(Celsius or Fahrenheit)
        self.unit_var = tk.StringVar(value="Celsius")  # Default Celsius
        self.unit_option = tk.OptionMenu(root, self.unit_var, "Celsius", "Fahrenheit")
        self.unit_option.config(fg="white", bg="black")
        self.unit_option.pack(pady=5)

        self.wind_speed_label = tk.Label(root, text="Wind Speed: ", fg="white", bg="black")
        self.wind_speed_label.pack(pady=5)

        # Dropdown wind units (m/s, mph, knots)
        self.wind_scale_var = tk.StringVar(value="m/s")  # Default is m/s
        self.wind_scale_option = tk.OptionMenu(root, self.wind_scale_var, "m/s", "mph", "knots")
        self.wind_scale_option.config(fg="white", bg="black")
        self.wind_scale_option.pack(pady=5)

        self.temperature_label = tk.Label(root, text="Temperature: ", fg="white", bg="black")
        self.temperature_label.pack(pady=5)

        self.humidity_label = tk.Label(root, text="Humidity: ", fg="white", bg="black")
        self.humidity_label.pack(pady=5)

        self.get_weather_button = tk.Button(root, text="Get Current Weather", command=self.get_current_weather, fg="white", bg="black")
        self.get_weather_button.pack(pady=15)

    def set_background_image(self):
        """Sets the background image for the Tkinter window."""
        # Load image using PIL
        image = Image.open("earrth.jpg")  # Change this to the path of your image
        image = image.resize((500, 500), Image.Resampling.LANCZOS) 
        self.bg_image = ImageTk.PhotoImage(image)

        # Create a Label widget to display the background image
        bg_label = tk.Label(self.root, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)  # Place cover whole window

    def get_current_weather(self):
        """
        Fetches the current weather from OpenWeather API or uses cached data
        10 minutes for api call to limit spam actions by user
        """
        # Get city, state, country from the user
        city = self.city_entry.get().strip()
        state = self.state_entry.get().strip()
        country = self.country_entry.get().strip()

        # Validate 
        if not city or not country:
            messagebox.showerror("Input Error", "City and Country are required!")
            return

        # Construct the location string (City, State, Country)
        location = f"{city},{state},{country}" if state else f"{city},{country}"

        # Check if the cached data is still valid
        if self.last_api_call_time and datetime.now() - self.last_api_call_time < timedelta(minutes=10):
            print("Using cached weather data.")
            self.display_weather(self.cached_weather_data)
            return

        # If no cached data or data is expired, make call
        api_key = "your_openweather_api_key"  #REPLACE 
        unit = "metric" if self.unit_var.get() == "Celsius" else "imperial"  
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={unit}"
        
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                # Cache the data and time of the API call
                self.cached_weather_data = data
                self.last_api_call_time = datetime.now()
                print("Fetched new weather data from API.")
                self.display_weather(data)
            else:
                messagebox.showerror("API Error", "Error fetching weather data.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def convert_wind_speed(self, wind_speed, scale):
        """
        Converts desired : m/s, mph, or knots.
        """
        if scale == "mph":
            # Convert m/s to mph
            return wind_speed * 2.23694
        elif scale == "knots":
            # Convert m/s to knots 
            return wind_speed * 1.94384
        elif scale == "m/s":
            # Wind speed is m/s
            return wind_speed
        else:
            return wind_speed  # Default

    def display_weather(self, data):
        """
        Displays weather Tkinter GUI.
        """
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Get the unit Celsius or Fahrenheit
        unit = self.unit_var.get()
        if unit == "Celsius":
            temp_unit = "°C"
        else:
            temp_unit = "°F"

        # Get selected wind unit
        wind_scale = self.wind_scale_var.get()
        converted_wind_speed = self.convert_wind_speed(wind_speed, wind_scale)

        # Update 
        self.city_label.config(text=f"City: {city}")
        self.temperature_label.config(text=f"Temperature: {temperature:.2f}{temp_unit}")
        self.humidity_label.config(text=f"Humidity: {humidity}%")
        self.wind_speed_label.config(text=f"Wind Speed: {converted_wind_speed:.2f} {wind_scale}")


if __name__ == "__main__":
    # Create Tkinter root window
    root = tk.Tk()
    
    # Create WeatherApp 
    app = WeatherApp(root)
    
    # Start Tkinter event loop
    root.mainloop()
