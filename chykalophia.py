from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://chykalophia.com')

driver.maximize_window()
#in icon
in_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='https://www.linkedin.com/company/2329060/']")))
in_btn.click()

#Fb icon
driver = webdriver.Chrome()
driver.get('https://chykalophia.com')
driver.maximize_window()
fb_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='https://www.facebook.com/chykalophia/']")))
fb_btn.click()

#twitter icon
driver = webdriver.Chrome()
driver.get('https://chykalophia.com')
driver.maximize_window()
twitter_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='elementor-icon elementor-social-icon elementor-social-icon-twitter elementor-repeater-item-9b65ef0']")))
twitter_btn.click()





