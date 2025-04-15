import time
import csv
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


print("Current working directory:", os.getcwd())


chrome_options = Options()
chrome_options.add_argument('--headless')  
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


print("Launching Chrome browser...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    print("Navigating to the website...")
    driver.get("https://vacancymail.co.zw/jobs/")

    print("Waiting for job listings to load...")
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-listing")))

    job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-listing")
    print(f"Found {len(job_listings)} job listings.")

    filename = 'scraped_jobs.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Location", "Expiry Date", "Job Description"])

        for job in job_listings:
            try:
                title = job.find_element(By.CSS_SELECTOR, ".job-listing-title").text
            except:
                title = "N/A"

            try:
                company = job.find_element(By.CSS_SELECTOR, ".job-listing-company").text
            except:
                try:
                    company = job.find_element(By.CSS_SELECTOR, ".job-listing-description").text.split('\n')[0]
                except:
                    company = "N/A"

            try:
                location = job.find_element(By.CSS_SELECTOR, ".icon-material-outline-location-on").find_element(By.XPATH, "..").text
            except:
                location = "N/A"

            try:
                expiry_date = job.find_element(By.CSS_SELECTOR, ".icon-material-outline-access-time").find_element(By.XPATH, "..").text
            except:
                expiry_date = "N/A"

            try:
                description = job.find_element(By.CSS_SELECTOR, ".job-listing-description").text
            except:
                description = "N/A"

            writer.writerow([title, company, location, expiry_date, description])

    print(f"✅ Job listings have been successfully saved to '{filename}'.")

except Exception as e:
    print("❌ An error occurred:", e)

finally:
    driver.quit()
    print("Browser closed.")
