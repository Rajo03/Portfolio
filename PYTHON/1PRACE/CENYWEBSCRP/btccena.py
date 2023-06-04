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

driver_service = Service(executable_path="C:\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service,options=options)


def cena():
  driver.get("https://e-kursy-walut.pl/kurs-bitcoin")
  page2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/strong/span[1]')))
  page3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/small/span'))
  )
  print(page3.text)
  print(page2.text)

schedule.every(1).minutes.do(cena)



while (True):
 schedule.run_pending()
 time.sleep(1)
    
    








