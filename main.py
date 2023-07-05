import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import dotenv

dotenv.load_dotenv("env.env")
USERNAME = os.environ.get("LI_USERNAME")
PASS = os.environ.get("PASS")
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3628808666&distance=50&" \
      "f_AL=true&geoId=102673369&keywords=python&location=27549%2C%20Louisburg%2C%20" \
      "North%20Carolina%2C%20United%20States&refresh=true"

stay_open = Options()
stay_open.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=stay_open)
driver.get(url=URL)

sign_in_element = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_page_url = sign_in_element.get_attribute("href")

sign_in_element.click()
driver.get(url=sign_in_page_url)

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(USERNAME)

pw_input = driver.find_element(By.ID, "password")
pw_input.send_keys(PASS)

sign_in_element = driver.find_element(By.TAG_NAME, "button")
sign_in_element.click()

driver.get(URL)
job = driver.find_element(By.CLASS_NAME, "job-card-list__title")
job_link = driver.find_element(By.LINK_TEXT, job.text)
job_url = job_link.get_attribute("href")
job_link.click()

driver.get(job_url)
save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
save_button.click()