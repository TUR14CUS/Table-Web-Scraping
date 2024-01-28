from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

def scrape_and_export_data(web, path, is_headless=False):
    # Get date in format MMDDYYYY
    now = datetime.now()
    month_day_year = now.strftime("%m%d%Y")

    # Prepare the script before converting it to an executable
    application_path = os.path.dirname(sys.executable)

    # Set up Chrome options
    options = Options()
    options.headless = is_headless

    # Create the driver
    driver_service = Service(executable_path=path)
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.get(web)

    # Finding Elements
    containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

    titles = []
    subtitles = []
    links = []
    for container in containers:
        title = container.find_element(by='xpath', value='./a/h2').text
        subtitle = container.find_element(by='xpath', value='./a/p').text
        link = container.find_element(by='xpath', value='./a').get_attribute('href')
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)

    # Exporting data to the same folder where the executable will be located
    my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
    df_headlines = pd.DataFrame(my_dict)
    file_name = f'football_headlines_{month_day_year}.csv'
    final_path = os.path.join(application_path, file_name)
    df_headlines.to_csv(final_path)

    driver.quit()

# Usage examples
web_url = 'https://www.thesun.co.uk/sport/football/'
chrome_driver_path = 'path_to_chrome_driver.exe'  # Update with the actual path

# Scraping data with headless mode
scrape_and_export_data(web_url, chrome_driver_path, is_headless=True)

# Scraping data without headless mode
scrape_and_export_data(web_url, chrome_driver_path, is_headless=False)
