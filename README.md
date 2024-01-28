# Web Scraping and Data Extraction Scripts

These Python scripts utilize the Selenium library to scrape football headlines from "The Sun" website (https://www.thesun.co.uk/sport/football/). The data is then processed and exported to CSV files. Three versions of the script are provided: `extract-data.py`, `automation.py`, and `headless.py`.

## 1. `extract-data.py`

This script extracts football headlines data from the website, specifically the title, subtitle, and link. The extracted data is then saved to a CSV file named `headline.csv`.

### Usage:
1. Set the `path` variable to the path of your ChromeDriver executable.
2. Run the script.
3. Provide the required information when prompted.
4. Check the generated `headline.csv` file for the extracted data.

## 2. `automation.py`

This script automates the process of extracting football headlines and exporting the data to a CSV file. It includes the current date in the CSV filename to differentiate between runs.

### Usage:
1. Set the `path` variable to the path of your ChromeDriver executable.
2. Run the script.
3. The script will generate a CSV file with a filename like `football_headlines_MMDDYYYY.csv`.
4. Check the file in the same directory as the script.

## 3. `headless.py`

Similar to `automation.py`, this script runs in headless mode, meaning the browser is not visibly launched. It extracts football headlines and saves the data to a CSV file named `headline-headless.csv`.

### Usage:
1. Set the `path` variable to the path of your ChromeDriver executable.
2. Run the script.
3. Check the generated `headline-headless.csv` file for the extracted data.

### Important Notes:
- Ensure you have the required dependencies installed (`selenium` and `pandas`). You can install them using `pip install selenium pandas`.
- Make sure to have the ChromeDriver executable compatible with your Chrome browser version.
- Use responsibly and be aware of website terms of service regarding web scraping.

Feel free to customize these scripts based on your specific needs.
