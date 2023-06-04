from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver_service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service,options=options)

#driver2 = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
#driver3 = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")




driver.get("https://www.youtube.com/watch?v=U_BOxTODBMA&list=PLHAfo0kzPsgpicia6C8cqtTBoN9WfNWyg&index=67&t=85s")
driver.implicitly_wait(2)
l = driver.find_element("xpath",'//*[@id="button"]')
l.click()
print(driver.title)

driver.refresh()

  