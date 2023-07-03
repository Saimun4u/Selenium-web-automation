from selenium import webdriver
from selenium.webdriver.common.by import By

path = "C:\\Users\Saimun\\Desktop\\chromedriver.exe"
# googleURL = "https://www.google.com"
youtubeURL = "https://www.youtube.com/@freecodecamp"

# Execute the driver and open the path

driver = webdriver.Chrome(executable_path = path)
driver.get(youtubeURL)

subCount = driver.find_element(By.ID, "subscriber-count")

print(subCount.text)