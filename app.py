from selenium import webdriver
from selenium.webdriver.common.by import By

path = "C:\\Users\Saimun\\Desktop\\chromedriver.exe"
# googleURL = "https://www.google.com"
youtubeURL = "https://www.youtube.com/@freecodecamp"

# Execute the driver and open the path

driver = webdriver.Chrome(executable_path = path)
driver.get(youtubeURL)

# Search by ID
# subCount = driver.find_element(By.ID, "subscriber-count")

# Search by Xpath
subCount = driver.find_element(By.XPATH, '//*[@id="subscriber-count"]')

print(subCount.text)

# Close the browser after fetching the data

driver.quit()