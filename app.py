from selenium import webdriver
from selenium.webdriver.common.by import By

# ******* GETTING DATA FROM A WEBSITE *******

path = "C:\\Users\Saimun\\Desktop\\chromedriver.exe"
# googleURL = "https://www.google.com"
youtubeURL = "https://www.youtube.com/@freecodecamp"
instaURL = "https://www.instagram.com/"
username = "saimunhas"
password = "Saimun_1983"


# Execute the driver and open the path

driver = webdriver.Chrome(executable_path = path)
# driver.get(youtubeURL)
driver.get(instaURL)

# Search by ID
# subCount = driver.find_element(By.ID, "subscriber-count")

# Search by Xpath
# subCount = driver.find_element(By.XPATH, '//*[@id="subscriber-count"]')

# print(subCount.text)

# Close the browser after fetching the data

# driver.quit()

# ******* FORM SUBMISSION AND AUTOMATION *******


usernameEntry = driver.find_element(BY.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
passwordEntry = driver.find_element(BY.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
usernameEntry.send_keys(username)
passwordEntry.send_keys(password)


driver.quit()
