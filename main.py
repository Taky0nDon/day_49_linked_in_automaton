import os
import time

import selenium.common.exceptions
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dotenv

## Can detect captcha page bt finding H1 element
dotenv.load_dotenv("env.env")
USERNAME = os.environ.get("LI_USERNAME")
PASS = os.environ.get("PASS")
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3628808666&distance=50&" \
      "f_AL=true&geoId=102673369&keywords=python&location=27549%2C%20Louisburg%2C%20" \
      "North%20Carolina%2C%20United%20States&refresh=true"
# scroll_to_bottom = "window.scrollTo(0,document.body.scrollHeight)"
the_bottom_class_name = "div.jobs-company__footer"

stay_open = Options()
stay_open.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=stay_open)

driver.get(url=URL)
# driver.maximize_window()
time.sleep(2)

sign_in_element = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_page_url = sign_in_element.get_attribute("href")
sign_in_element.click()

# driver.get(url=sign_in_page_url)
# time.sleep(2)

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(USERNAME)
pw_input = driver.find_element(By.ID, "password")
pw_input.send_keys(PASS)
sign_in_element = driver.find_element(By.TAG_NAME, "button")
sign_in_element.click()
time.sleep(15)
# if driver.find_element(By.TAG_NAME, "h1"):
#     print("Captcha encountered.")
#     for n in range(14):
#         time.sleep(1)
#         print(n+1)


jobs_container = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div')
# list_elements = jobs_container.find_elements(By.TAG_NAME, "li")
#
# move_to_last_li_and_page_down = ActionChains(driver).scroll_to_element(list_elements[-1])
# move_to_last_li_and_page_down.perform()
# time.sleep(2)

jobs = driver.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
print(f"initial len of jobs = {len(jobs)}")
moving_to_last_job = ActionChains(driver).move_to_element(jobs[-1]).perform()
time.sleep(3)
initial_jobs = jobs
jobs = driver.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
print(f"new len of jobs = {len(jobs)}")

message_minimizer = driver.find_element(By.CSS_SELECTOR, "li-icon[type='chevron-down']")
message_minimizer.click()
number_of_clicked_jobs = 0
cancel_css_selector = "li-icon[type='cancel-icon'] svg path"
for n in range(len(jobs)):
    job = jobs[n]
    job_link = job.find_element(By.TAG_NAME, "a")
    job_link_text = job_link.text

    ActionChains(driver).scroll_to_element(job).move_to_element(job).scroll_to_element(jobs[-1]).perform()

    job_link.click()
    number_of_clicked_jobs += 1
    time.sleep(2)


    print(f"{job_link_text} clicked. That's {number_of_clicked_jobs} jobs.")
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()
    # ActionChains(driver).send_keys(Keys.PAGE_DOWN).send_keys(Keys.PAGE_DOWN).send_keys(Keys.PAGE_DOWN)\
    # .perform()
    time.sleep(2)

    annoying_popup = driver.find_element(By.CSS_SELECTOR, cancel_css_selector)
    annoying_popup.click()

    print(f"Saved {job_link_text}")

# Follow button may not exist.
    try:
        bottom_element = driver.find_element(By.CSS_SELECTOR, the_bottom_class_name)
    except selenium.common.exceptions.NoSuchElementException:
        print(f"{job_link_text} cannot be followed.")
    else:
        ActionChains(driver).move_to_element(bottom_element).perform()
        follow_company_element = driver.find_element(By.CSS_SELECTOR, "button.follow")
        ActionChains(driver)\
            .move_to_element(follow_company_element)\
            .perform()
        follow_company_element.click()
        time.sleep(2)

        annoying_popup = driver.find_element(By.CSS_SELECTOR, cancel_css_selector)
        annoying_popup.click()
        print(f"Followed {job_link_text}")
    print("Refreshing jobs...")
    jobs = driver.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")

print(f"clicked {number_of_clicked_jobs} jobs")

#     job_inner_html = job.get_attribute("innerHTML")
#     try:
#         job_name = job.find_element(By.TAG_NAME, "a")
#     except:
#         with open("failed_cases.html", "a") as file:
#             file.write(f"#########################\n\n{job_inner_html}\n\n")
#     else:
#         print(f"{job_name.text}")
#         with open("successful_cases.html", "a") as file:
#             file.write(f"$$$$$$$$$$$$$$$$$\n\n{job_inner_html}\n\n")
    # company_name_element = job.find_element(By.CLASS_NAME, "job-card-list__title")
    # company_name = company_name_element.text
    # print(f"working on {company_name}")
#
#     job_link = driver.find_element(By.LINK_TEXT, job.text)
#     # Make sure the job link is not obscured so the click can't be interfered with.
#     ActionChains(driver).move_to_element(job).click(job).perform()
#     time.sleep(2)
#

#


