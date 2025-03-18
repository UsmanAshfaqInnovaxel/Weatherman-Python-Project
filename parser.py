import csv
import os
from datetime import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class WeatherReading:
    date: datetime
    max_temp: int
    min_temp: int
    humidity: int

def parse_csv_file(filepath: str) -> List[WeatherReading]:
    readings = []
    with open(filepath, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        # Skip header row
        next(reader, None)
        for row in reader:
            if row:  # ensure the row is not empty
                try:
                    reading_date = datetime.strptime(row[0], "%Y-%m-%d")
                    max_temp = int(row[1])
                    min_temp = int(row[2])
                    humidity = int(row[3])
                    readings.append(WeatherReading(reading_date, max_temp, min_temp, humidity))
                except Exception as e:
                    print(f"Error parsing row {row} in {filepath}: {e}")
    return readings

def parse_txt_file(filepath: str) -> List[WeatherReading]:
    readings = []
    with open(filepath, 'r') as txtfile:
        for line in txtfile:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    # Expecting line format: "2002-02-01 21C 5C 93%"
                    parts = line.split()
                    reading_date = datetime.strptime(parts[0], "%Y-%m-%d")
                    # Remove trailing 'C' and '%' and convert to int
                    max_temp = int(parts[1].rstrip("C"))
                    min_temp = int(parts[2].rstrip("C"))
                    humidity = int(parts[3].rstrip("%"))
                    readings.append(WeatherReading(reading_date, max_temp, min_temp, humidity))
                except Exception as e:
                    print(f"Error parsing line '{line}' in {filepath}: {e}")
    return readings

def parse_weather_data(data_dir: str) -> List[WeatherReading]:
    """
    Parse weather data from CSV and TXT files located in data_dir.
    Returns a list of WeatherReading objects.
    """
    all_readings = []
    # List all files in the directory
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        if os.path.isfile(filepath):
            if filename.lower().endswith('.csv'):
                all_readings.extend(parse_csv_file(filepath))
            elif filename.lower().endswith('.txt'):
                all_readings.extend(parse_txt_file(filepath))
    return all_readings

# If you want to run this module independently for testing purposes:
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python parser.py <data_directory>")
        sys.exit(1)
    data_directory = sys.argv[1]
    readings = parse_weather_data(data_directory)
    for r in readings:
        print(r)
