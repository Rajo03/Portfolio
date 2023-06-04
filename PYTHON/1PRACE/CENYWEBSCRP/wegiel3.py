from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import schedule
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver_service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service,options=options)


def cena():
  driver.get("https://sklep.pgg.pl/")
  page2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div[8]/div[3]')))
  print(page2.text)


while (True):
 cena()
 time.sleep(10)
 driver.quit()







