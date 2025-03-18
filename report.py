def generate_yearly_report(stats, year):
    """
    Generates and prints a yearly report.
    The stats dictionary should have keys:
      - 'highest': {"temp": value, "date": datetime}
      - 'lowest' : {"temp": value, "date": datetime}
      - 'humidity': {"value": value, "date": datetime}
    """
    if not stats:
        print(f"No data found for year {year}.")
        return

    highest = stats["highest"]
    lowest = stats["lowest"]
    humidity = stats["humidity"]

    print(f"\nYear {year} Report:")
    print(f"Highest: {highest['temp']}C on {highest['date'].strftime('%B %d')}")
    print(f"Lowest: {lowest['temp']}C on {lowest['date'].strftime('%B %d')}")
    print(f"Humidity: {humidity['value']}% on {humidity['date'].strftime('%B %d')}")


def generate_monthly_report(avg_stats, year, month):
    """
    Generates and prints a monthly average report.
    The avg_stats dictionary should have keys:
      - 'avg_max'
      - 'avg_min'
      - 'avg_humidity'
    """
    if not avg_stats:
        print(f"No data found for {year}/{month:02d}.")
        return

    print(f"\nMonthly Averages for {year}/{month:02d}:")
    print(f"Highest Average: {avg_stats['avg_max']}C")
    print(f"Lowest Average: {avg_stats['avg_min']}C")
    print(f"Average Mean Humidity: {avg_stats['avg_humidity']}%")


def generate_chart_report(chart_data, year, month):
    """
    Generates and prints a horizontal bar chart for each day in the given month.
    The chart_data is expected to be a list of dictionaries with keys:
      - 'date'     : a datetime object representing the day
      - 'max_temp' : highest temperature on that day
      - 'min_temp' : lowest temperature on that day

    Each day prints two lines:
      - One for the highest temperature (in red)
      - One for the lowest temperature (in blue)
    """
    if not chart_data:
        print(f"No data found for {year}/{month:02d}.")
        return

    # Header with the full month name and year (e.g., "March 2011")
    month_name = chart_data[0]['date'].strftime('%B')
    print(f"\n{month_name} {year}")

    # ANSI escape codes for red and blue
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    # For each day, print the chart lines.
    # One plus sign per degree value.
    for entry in chart_data:
        day = entry['date'].strftime('%d')
        max_temp = entry['max_temp']
        min_temp = entry['min_temp']
        bar_max = RED + ('+' * max_temp) + RESET
        bar_min = BLUE + ('+' * min_temp) + RESET
        print(f"{day} {bar_max} {max_temp}C")
        print(f"{day} {bar_min} {min_temp}C")


# For module testing, you can run this file independently.
if __name__ == "__main__":
    # Example test data to simulate the output:
    from datetime import datetime
    # Simulate chart data for a couple of days
    sample_chart_data = [
        {"date": datetime(2011, 3, 1), "max_temp": 25, "min_temp": 11},
        {"date": datetime(2011, 3, 2), "max_temp": 22, "min_temp": 8},
    ]
    generate_yearly_report({
        "highest": {"temp": 45, "date": datetime(2011, 6, 23)},
        "lowest": {"temp": 1, "date": datetime(2011, 12, 22)},
        "humidity": {"value": 95, "date": datetime(2011, 8, 14)}
    }, 2011)
    generate_monthly_report({
        "avg_max": 39,
        "avg_min": 18,
        "avg_humidity": 71
    }, 2011, 3)
    generate_chart_report(sample_chart_data, 2011, 3)
