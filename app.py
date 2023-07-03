from selenium import webdriver
from selenium.webdriver.common.by import By

path = "C:\\Users\Saimun\\Desktop\\chromedriver.exe"
googleURL = "https://www.google.com"

# Execute the driver and open the path

driver = webdriver.Chrome(executable_path = path)
driver.get(googleURL)