import os
import sys
import argparse

# Import our modules (to be implemented)
from parser import parse_weather_data
from calculations import (
    calculate_yearly_stats,
    calculate_monthly_stats,
    calculate_daily_chart_data,
)
from report import (
    generate_yearly_report,
    generate_monthly_report,
    generate_chart_report,
)


def main():
    parser_arg = argparse.ArgumentParser(
        description="Weatherman Weather Reports Generator"
    )
    parser_arg.add_argument(
        "data_dir", help="Path to the data directory containing weather files."
    )
    parser_arg.add_argument(
        "-e",
        "--year",
        type=int,
        help="Year for displaying highest, lowest temperatures and humidity.",
    )
    parser_arg.add_argument(
        "-a",
        "--average",
        help="Month/Year in the format YYYY/MM for average report.",
    )
    parser_arg.add_argument(
        "-c",
        "--chart",
        help="Month/Year in the format YYYY/MM for chart report.",
    )
    
    args = parser_arg.parse_args()
    
    # Verify the data directory exists
    if not os.path.isdir(args.data_dir):
        print(f"Error: Data directory '{args.data_dir}' does not exist.")
        sys.exit(1)
    
    # Parse the weather data files from the data directory
    # This function should handle both CSV and TXT files
    readings = parse_weather_data(args.data_dir)
    
    # Generate reports based on the command-line options
    if args.year:
        # Compute yearly statistics
        year_stats = calculate_yearly_stats(readings, args.year)
        generate_yearly_report(year_stats, args.year)
        
    if args.average:
        try:
            year, month = map(int, args.average.split('/'))
        except ValueError:
            print("Error: Invalid format for -a option. Use YYYY/MM.")
            sys.exit(1)
        avg_stats = calculate_monthly_stats(readings, year, month)
        generate_monthly_report(avg_stats, year, month)
        
    if args.chart:
        try:
            year, month = map(int, args.chart.split('/'))
        except ValueError:
            print("Error: Invalid format for -c option. Use YYYY/MM.")
            sys.exit(1)
        chart_data = calculate_daily_chart_data(readings, year, month)
        generate_chart_report(chart_data, year, month)


if __name__ == "__main__":
    main()
