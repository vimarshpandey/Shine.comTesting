from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.shine.com/")
os.makedirs("screenshots", exist_ok=True)

def take_screenshot(name):
    driver.save_screenshot(f"screenshots/{name}.png")

#login
login_button = driver.find_element(By.XPATH, "//button[@class='btn btn-xs btn-outline-secondary mr-15']")
login_button.click()
time.sleep(2)

email_input = driver.find_element(By.ID, "id_email_login")
email_input.send_keys("vimpandey2001@gmail.com")
time.sleep(2)

password_input = driver.find_element(By.ID, "id_password")
password_input.send_keys("REDtiles@2001")
time.sleep(2)

submit_button = driver.find_element(By.XPATH, "//button[@class='cls_base_1_pw_login_btn btn btn-secondary w-100 mt-30']")
submit_button.click()
time.sleep(5)

take_screenshot("01_logged_in")
print("Logged in successfully")
print("Title:", driver.title)
print("URL:", driver.current_url)

#job search
job_title = driver.find_element(By.ID, "skills")
job_title.click()

job_title_box = driver.find_element(By.ID, "id_q")
job_title_box.send_keys("Software Tester")
time.sleep(2)

location_box = driver.find_element(By.ID, "id_loc")
location_box.clear()
location_box.send_keys("Hyderabad")
time.sleep(2)

experience_input = driver.find_element(By.XPATH, "//input[@class='heading-input ']")
experience_input.click()
time.sleep(1)

option_2_years = driver.find_element(By.ID, "item-key-2")
option_2_years.click()
time.sleep(2)

take_screenshot("02_entered_job_search_details")

search_button = driver.find_element(By.ID, "id_new_search_submit_button")
search_button.click()
time.sleep(5)

take_screenshot("03_search_done")

#select second job and apply
job_cards = driver.find_element(By.XPATH, "(//button[@class='jobApplyBtnNova_bigCardBottomApply__z2n7R nova_btn nova_btn-secondary jdbigCardBottomApply '])[2]")
job_cards.click()
time.sleep(10)

no_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='No']")
no_radio.click()
time.sleep(1)

ctc_button = driver.find_element(By.ID, 'q3_2_0')
ctc_button.click()
time.sleep(1)

option_1_select = driver.find_element(By.XPATH, "//option[@value='Rs 0 / Yr']")
option_1_select.click()

notice_period_button = driver.find_element(By.ID, 'q4_2_0')
notice_period_button.click()

option_2_select = driver.find_element(By.XPATH, "//option[@value='Immediate Joiner']")
option_2_select.click()

submit_button = driver.find_element(By.XPATH, "//button[text()='Submit and apply']")
submit_button.click()
time.sleep(1)

take_screenshot("04_applied_successfully")
time.sleep(1)
job_title_element = driver.find_element(By.XPATH, "(//p[@class='jobCardNova_bigCardTopTitleHeading__Rj2sC jdTruncation']/a)[2]")
print("Job Title:", job_title_element.text)
time.sleep(1)
company_element = driver.find_element(By.XPATH, "(//span[@class='jobCardNova_bigCardTopTitleName__M_W_m jdTruncationCompany'])[2]")
print("Company Name:", company_element.text)

time.sleep(10)
driver.quit()