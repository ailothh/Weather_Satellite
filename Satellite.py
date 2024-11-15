#Satellite class
class Satellite:
    def __init__(self, satellite_id="Joint Polar Satellite System-2", launch_date="11/10/2022", status="Operational"):
        self.satellite_id = satellite_id
        self.launch_date = launch_date
        self.status = status

    def TransmitData(self):
        print(f"Satellite {self.satellite_id} transmitting data...")

    def CheckStatus(self):
        print(f"Satellite {self.satellite_id} current status is: {self.status}")

#Sensors class
class Sensors:
    def __init__(self, sensor_id="SENSOR-1", sensor_type="TemperatureCollector"):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type

    def CollectReading(self):
        print(f"Sensor {self.sensor_id} of type {self.sensor_type} collecting reading...")

# Weather_Data class
class Weather_Data:
    def __init__(self, humidity=60, wind_speed=15, temperature=22, precipitation=2):
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.temperature = temperature
        self.precipitation = precipitation

    def StoreData(self):
        # pass the values into dic to combine all of them to only pass one variable to class
        weather_info = {
            "Humidity": self.humidity,
            "Wind Speed": self.wind_speed,
            "Temperature": self.temperature,
            "Precipitation": self.precipitation
        }
        print(f"Storing weather data... Humidity: {self.humidity}%, Wind Speed: {self.wind_speed} mph, Temperature: {self.temperature} degrees, Precipitation: {self.precipitation} cm")
        return weather_info # pass to weather_station class

# Weather_Station class
class Weather_Station:
    def __init__(self, station_id="WeatherStation-01", location="Orlando", contact_number="321-098-4673"):
        self.station_id = station_id
        self.location = location
        self.contact_number = contact_number

    def ReceiveData(self, weather_info):
        print(f"Weather station {self.station_id} located at {self.location} successfully received data:")
        print(f"Humidity: {weather_info['Humidity']}%, Wind Speed: {weather_info['Wind Speed']} mph, Temperature: {weather_info['Temperature']} degrees, Precipitation: {weather_info['Precipitation']} cm")

#Data_Processor class
class Data_Processor:
    def __init__(self, data="Sample data"):
        self.data = data

    def AnalyzeData(self):
        print("Analyzing data...")

    def GenerateReport(self):
        print("Generating report...")
        
#Weather_Report class
class Weather_Report:
    def __init__(self, report_id="REPORT-01", report_data="Sample data", agencies = "FEMA, NOAA"):
        self.report_id = report_id
        self.report_data = report_data
        self.agencies = agencies

    def CreateReport(self):
        print("Creating weather report...")

    def StoreReport(self):
        print("Storing weather report into appropriate databases...")

    def SendReport(self):
        print(f"Sending weather report to requesting agencies: {self.agencies}")

#Power_System class
class Power_System:
    def __init__(self, signal_strength=40, battery_level=50):
        self.signal_strength = signal_strength
        self.battery_level = battery_level

    def CheckConnectionStatus(self):
        print("Checking connection status...")
        #alert if level low, if
        if (self.signal_strength < 80):
            print(f"WARNING: Low signal strength {self.signal_strength}%")
        else:
            print(f"Signal strength is {self.signal_strength}%.")

    def CheckBatteryStatus(self):
        print("Checking battery level...")
        #alert if level low, if 
        if (self.battery_level < 60):
            print(f"WARNING: Low battery level {self.battery_level}%")
        else:
            print(f"Battery level is {self.battery_level}%.")

#test calls
if __name__ == "__main__":
    #calls
    satellite = Satellite()
    satellite.TransmitData()
    satellite.CheckStatus()

    sensor = Sensors()
    sensor.CollectReading()

    weather_data = Weather_Data()
    collected_data = weather_data.StoreData()

    weather_station = Weather_Station()
    weather_station.ReceiveData(collected_data)
    
    data_processor = Data_Processor()
    data_processor.AnalyzeData()
    data_processor.GenerateReport()

    weather_report = Weather_Report()
    weather_report.CreateReport()
    weather_report.StoreReport()
    weather_report.SendReport()

    power_system = Power_System()
    power_system.CheckConnectionStatus()
    power_system.CheckBatteryStatus()
