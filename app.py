from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# ******* GETTING DATA FROM A WEBSITE *******

path = "C:\\Users\Saimun\\Desktop\\chromedriver.exe"
youtubeURL = "https://www.youtube.com/@freecodecamp"
instaURL = "https://www.instagram.com/"
username = ""
password = ""


# Execute the driver and open the path

driver = webdriver.Chrome(executable_path = path)
# driver.get(youtubeURL)
driver.get(instaURL)

time.sleep(3)

# Search by ID
# subCount = driver.find_element(By.ID, "subscriber-count")

# Search by Xpath
# subCount = driver.find_element(By.XPATH, '//*[@id="subscriber-count"]')

# print(subCount.text)

# Close the browser after fetching the data

# driver.quit()

# ******* FORM SUBMISSION AND AUTOMATION *******

usernameEntry = driver.find_element(BY.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
usernameEntry.send_keys(username)

passwordEntry = driver.find_element(BY.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
passwordEntry.send_keys(password)

# Select XPATH after entering login credentials

loginButton = driver.find_element(BY.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()


