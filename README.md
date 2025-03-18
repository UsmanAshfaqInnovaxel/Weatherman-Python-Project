# Weatherman Project

Weatherman is a weather report generator that parses weather data from CSV and TXT files and produces multiple types of reports including yearly extremes, monthly averages, and daily temperature charts with color-coded bar graphs.

## Overview

The project reads weather data files (both CSV and TXT formats) stored in a designated data folder, processes the data, and then generates reports based on the user's command-line inputs. The available reports are:

- **Yearly Report:** Displays the highest temperature, lowest temperature, and highest humidity for a given year.
- **Monthly Report:** Shows average highest temperature, average lowest temperature, and average mean humidity for a specified month.
- **Daily Chart Report:** Draws horizontal bar charts (using ANSI color codes—red for high temperatures and blue for low temperatures) to display daily temperatures for a specified month.

## Features

- **Multi-format Support:** Works with CSV and TXT weather data files.
- **Report Flexibility:** Generate multiple reports in one command.
- **Color-coded Output:** Uses ANSI escape codes for colored terminal output.
- **Modular Design:** Clean separation into modules for parsing, calculations, and reporting.
- **PEP-8 Compliant:** Code is written to be clear, concise, and self-explanatory.

## Project Structure

```
Weatherman/
├── Data/              # Contains weather data files (e.g., Murree_2002_01.txt)
├── weatherman.py      # Main entry point for the application.
├── parser.py          # Module for parsing CSV and TXT weather data files.
├── calculations.py    # Module for performing necessary computations on weather data.
└── report.py          # Module for generating and displaying the reports.
```

## Setup

### Prerequisites

- **Python:** Version 3.6 or higher (Python 3.7+ recommended).
- **Git:** To clone the repository (optional if you download the ZIP file).

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Weatherman.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Weatherman
   ```

3. **(Optional) Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   # On Unix or MacOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

4. **Place Your Data Files:**

   - Ensure that there is a folder named `Data` in the project root.
   - Place your weather data files (e.g., `Murree_2002_01.txt`) inside the `Data` folder.  
     *(Note: The project expects data files covering years from 2002 to 2011.)*

## Usage

Run the main script (`weatherman.py`) by specifying the data directory along with one or more of the following options:

### Command Syntax

```bash
python weatherman.py <data_dir> [options]
```

- `<data_dir>`: The path to your data folder (e.g., `Data`).

### Options

- **Yearly Report (`-e` or `--year`):**  
  Generates a report displaying:
  - Highest temperature (with date)
  - Lowest temperature (with date)
  - Highest humidity (with date)

  **Example:**
  ```bash
  python weatherman.py Data -e 2002
  ```

- **Monthly Report (`-a` or `--average`):**  
  Generates a report displaying:
  - Average highest temperature
  - Average lowest temperature
  - Average mean humidity  
  The month should be provided in the format `YYYY/MM`.

  **Example:**
  ```bash
  python weatherman.py Data -a 2005/6
  ```

- **Daily Chart Report (`-c` or `--chart`):**  
  Generates a bar chart report showing:
  - Daily high and low temperatures with a color-coded horizontal bar (red for high, blue for low)  
  The month should be provided in the format `YYYY/MM`.

  **Example:**
  ```bash
  python weatherman.py Data -c 2011/03
  ```

- **Multiple Reports:**  
  You can combine multiple options to generate several reports at once.

  **Example:**
  ```bash
  python weatherman.py Data -e 2011 -a 2011/3 -c 2011/03
  ```

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or new features to add:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Open a pull request describing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- ANSI escape codes are used for color-coding the temperature charts.
- This project structure and code style adhere to PEP-8 conventions for Python code.

---

Happy Coding!
```
