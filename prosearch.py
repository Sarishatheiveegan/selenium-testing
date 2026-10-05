from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.ID, "login-button")

# Clear the boxes first
username.clear()
password.clear()

# Enter credentials
username.send_keys("standard_user")
password.send_keys("secret_sauce")

print("Username:", username.get_attribute("value"))
print("Password:", password.get_attribute("value"))

print("Placeholder text:", username.get_attribute("placeholder"))
print("Is login button enabled?:", login.is_enabled())
print("Is username field displayed?:", username.is_displayed())

login.click()

input("Press Enter to close the browser...")