# Install Chrome driver that match the Chrome version
# Install Selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chromedriver_win32/chromedriver"
service = Service(r"chromedriver_win32/chromedriver.exe")
option = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=option)
driver.get("https://google.com/")

# https://selenium-python.readthedocs.io/locating-elements.html
element = driver.find_element(By.NAME, 'q')
element.send_keys("Python")
element.submit()

print(driver.current_url)
results = driver.find_elements(By.TAG_NAME, "h3")
for result in results:
    print(result.text)

driver.quit()