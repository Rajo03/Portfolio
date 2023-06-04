from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import schedule


def view():
    
# Set the TikTok link
    link = 'https://www.tiktok.com/@mileslyes/video/7177869475109293317?is_copy_url=1&is_from_webapp=v1'

# Set the time to wait for the video to play in seconds
    wait_time = 60

# Set the path to the web driver executable
    driver_path = '/path/to/chromedriver'

# Set the web driver options
    options = webdriver.ChromeOptions()

# Disable notifications
    prefs = {'profile.default_content_setting_values.notifications': 2}
    options.add_experimental_option('prefs', prefs)

# Create the web driver
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Open the TikTok link
    driver.get(link)

# Wait for the video to play
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, "//video[@src]")))

# Close the browser
    driver.quit()

schedule.every(2).minutes.do(view)