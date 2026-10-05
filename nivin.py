from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

input("Complete the human verification if it appears, then press Enter here...")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Nivin Pauly")
search_box.submit()

input("Press Enter to close the browser...")

driver.quit()