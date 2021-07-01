from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Privacy Policy
driver = webdriver.Chrome()
driver.get('https://chykalophia.com')
prv_plcy_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='https://www.iubenda.com/privacy-policy/32384925']")))
prv_plcy_btn.click()

#cookie policy
driver = webdriver.Chrome()
driver.get('https://www.iubenda.com/privacy-policy/32384925/cookie-policy')

#sign up for next draft newsletter
driver = webdriver.Chrome()
driver.get('https://chykalophia.com')
email_input = driver.find_element_by_xpath('//input[@id="ff_3_email"]')
email_input.clear()
email_input.send_keys("evgeniya.vorobyeva@gmail.com")
email_input = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//img[@alt='Submit Form']")))
email_input.click()
