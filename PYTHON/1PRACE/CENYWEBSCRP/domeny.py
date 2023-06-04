from pydoc import pager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.whois.com/")
print(driver.title)

search = driver.find_element_by_id("whois_search_input")
search.send_keys("google")
search.send_keys(Keys.RETURN)



try:
    page2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "df-block"))
    
    )
    print(page2.text)
finally:
    driver.quit()
    


