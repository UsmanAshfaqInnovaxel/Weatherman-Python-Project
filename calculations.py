from collections import defaultdict
from parser import WeatherReading

def calculate_yearly_stats(readings, year):
    """
    For the given year, compute:
      - Highest temperature and its date.
      - Lowest temperature and its date.
      - Highest humidity and its date.
    Returns a dictionary with the results.
    """
    # Filter readings for the given year
    year_readings = [r for r in readings if r.date.year == year]
    if not year_readings:
        return None

    highest_reading = max(year_readings, key=lambda r: r.max_temp)
    lowest_reading = min(year_readings, key=lambda r: r.min_temp)
    highest_humidity_reading = max(year_readings, key=lambda r: r.humidity)

    stats = {
        "highest": {"temp": highest_reading.max_temp, "date": highest_reading.date},
        "lowest": {"temp": lowest_reading.min_temp, "date": lowest_reading.date},
        "humidity": {"value": highest_humidity_reading.humidity, "date": highest_humidity_reading.date}
    }
    return stats

def calculate_monthly_stats(readings, year, month):
    """
    For the given year and month, compute:
      - Average highest temperature.
      - Average lowest temperature.
      - Average humidity.
    Returns a dictionary with the average values (rounded to nearest integer).
    """
    month_readings = [r for r in readings if r.date.year == year and r.date.month == month]
    if not month_readings:
        return None

    avg_max = round(sum(r.max_temp for r in month_readings) / len(month_readings))
    avg_min = round(sum(r.min_temp for r in month_readings) / len(month_readings))
    avg_humidity = round(sum(r.humidity for r in month_readings) / len(month_readings))

    stats = {
        "avg_max": avg_max,
        "avg_min": avg_min,
        "avg_humidity": avg_humidity
    }
    return stats

def calculate_daily_chart_data(readings, year, month):
    """
    For the given year and month, group readings by day and compute:
      - The highest temperature of the day.
      - The lowest temperature of the day.
    Returns a list of dictionaries with each dictionary containing:
      'date'     : the datetime object,
      'max_temp' : highest temperature on that day,
      'min_temp' : lowest temperature on that day.
    """
    month_readings = [r for r in readings if r.date.year == year and r.date.month == month]
    if not month_readings:
        return None

    # Group readings by day (in case there are multiple per day)
    daily_data = defaultdict(list)
    for r in month_readings:
        daily_data[r.date.day].append(r)

    chart_data = []
    # Process days in sorted order
    for day in sorted(daily_data.keys()):
        day_readings = daily_data[day]
        max_temp = max(r.max_temp for r in day_readings)
        min_temp = min(r.min_temp for r in day_readings)
        # Use the first reading's date to represent the day
        date_obj = day_readings[0].date
        chart_data.append({"date": date_obj, "max_temp": max_temp, "min_temp": min_temp})
    return chart_data

# For module testing, run this file with a test case if needed.
if __name__ == "__main__":
    # This block can be used for quick module testing.
    from parser import parse_weather_data
    data_dir = "data"  # Update the path if necessary
    readings = parse_weather_data(data_dir)
    year_stats = calculate_yearly_stats(readings, 2002)
    print("Yearly Stats for 2002:", year_stats)
    
    monthly_stats = calculate_monthly_stats(readings, 2002, 2)
    print("Monthly Stats for 2002/02:", monthly_stats)
    
    daily_chart = calculate_daily_chart_data(readings, 2002, 2)
    print("Daily Chart Data for 2002/02:")
    for entry in daily_chart:
        print(entry)
