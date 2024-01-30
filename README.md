# Web Scraping and Data Export Readme

This Python script is designed to scrape data from a website using Selenium and export the collected data into a CSV file. The script is configured to work in both regular and headless modes, providing flexibility based on the user's preferences. Below is a guide on using and understanding the script.

## Table of Contents
1. [Features](#features)
2. [Usage Instructions](#usage-instructions)
3. [Prerequisites](#prerequisites)
4. [Configuration](#configuration)
5. [Run the Script](#run-the-script)
6. [Review the Output](#review-the-output)
7. [Adjustments](#adjustments)
8. [Notes](#notes)
9. [License](#license)

## Features:

1. **Web Scraping:**
   - Utilizes Selenium to navigate to a specified web page and collect data from elements with the class "teaser__copy-container."

2. **Data Export:**
   - Gathers titles, subtitles, and links from the scraped data.
   - Exports the collected data into a CSV file named `football_headlines_MMDDYYYY.csv`, where MMDDYYYY represents the current date.

3. **Headless Mode:**
   - Supports both regular and headless modes for running the script.

## Usage Instructions:

1. **Prerequisites:**
   - Ensure you have the Chrome WebDriver installed. You can download it from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/).
   - Install the required Python libraries using:
     ```bash
     pip install selenium pandas
     ```

2. **Configuration:**
   - Set the `web_url` variable to the target website URL.
   - Update the `chrome_driver_path` variable with the path to your Chrome WebDriver executable.

3. **Run the Script:**
   - Execute the script using a Python interpreter. You can run the script with or without headless mode, depending on your preference.

     ```bash
     python script_name.py
     ```

4. **Review the Output:**
   - The script will create a CSV file named `football_headlines_MMDDYYYY.csv` in the same directory where the script is located.

5. **Adjustments:**
   - Customize the script based on your specific requirements, such as modifying the XPath or adding additional data points.

6. **Notes:**
   - Use this script responsibly and in compliance with the website's terms of service.
   - Check for updates to ChromeDriver if issues arise due to browser updates.

## License
This project is licensed under the [MIT License](LICENSE).
