from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#instagram icon
driver = webdriver.Chrome()
driver.get('https://chykalophia.com')
insta_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='https://instagram.com/chykalophia/']")))
insta_btn.click()

#youtube icon
driver = webdriver.Chrome()
driver.get('https://chykalophia.com')
ytb_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='fab fa-youtube']")))
ytb_btn.click()

#github icon
driver = webdriver.Chrome()
driver.get('https://chykalophia.com')
driver.maximize_window()
github_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='fab fa-github']")))
github_btn.click()

#behance icon
driver = webdriver.Chrome()
driver.get('https://chykalophia.com')
driver.maximize_window()
be_btn = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//i[@class='fab fa-behance']")))
be_btn.click()