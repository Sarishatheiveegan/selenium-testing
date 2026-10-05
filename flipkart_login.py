from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")

wait = WebDriverWait(driver, 15)

# Find Login
login_button = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//span[text()='Login']")
    )
)

# Scroll Login into view
driver.execute_script(
    "arguments[0].scrollIntoView({block: 'center'});",
    login_button
)

# Click using JavaScript
driver.execute_script(
    "arguments[0].click();",
    login_button
)

print("Login button clicked!")

input("Press Enter to close...")