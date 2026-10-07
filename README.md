# Selenium Testing Automation

This project contains basic **Selenium WebDriver automation tasks using Python**.
The purpose of this project is to learn how Selenium can interact with web pages, locate elements, enter data, click buttons, verify element properties, and automate testing workflows.

## Technologies Used

* Python
* Selenium WebDriver
* Google Chrome
* Chrome WebDriver
* VS Code
* Python Virtual Environment (`venv`)

## Project Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install Selenium

```bash
pip install selenium
```

### 4. Run a Python File

```bash
python filename.py
```

---

# Task 1 – Product Search / SauceDemo Login

This task demonstrates how Selenium can:

* Open a website
* Locate username and password fields
* Clear existing values
* Enter login credentials
* Retrieve entered values
* Check placeholder text
* Check whether a button is enabled
* Check whether an element is displayed
* Click the Login button

### Code

```python
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
```

### Concepts Used

| Selenium Method      | Purpose                              |
| -------------------- | ------------------------------------ |
| `webdriver.Chrome()` | Opens Chrome browser                 |
| `driver.get()`       | Opens a website                      |
| `find_element()`     | Finds an element                     |
| `clear()`            | Clears an input field                |
| `send_keys()`        | Enters text                          |
| `get_attribute()`    | Gets an HTML attribute/value         |
| `is_enabled()`       | Checks whether an element is enabled |
| `is_displayed()`     | Checks whether an element is visible |
| `click()`            | Clicks an element                    |

---

# Task 2 – Search for a Person

This task demonstrates how Selenium can interact with a search engine and enter a person's name into the search box.

For example, the person searched can be **Nivin Pauly**.

### Example Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Nivin Pauly")

search_box.submit()

input("Press Enter to close the browser...")
```

### Concepts Used

* Opening a website using Selenium
* Finding an input field
* Entering search text using `send_keys()`
* Submitting a search using `submit()`

### Note

Search engines may sometimes display human verification or CAPTCHA pages when automated browsers are detected. This is an anti-bot security feature of the website and is not a Selenium error.

---

# Task 3 – Flipkart Login and OTP Testing

This task is intended to demonstrate a login testing workflow using Selenium.

### Automation Flow

```text
Open Flipkart
      ↓
Click Login
      ↓
Enter Mobile Number
      ↓
OTP Generated
      ↓
Test OTP Source
      ↓
Continue Login
```


### Example Test OTP Logic

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.flipkart.com/")

wait = WebDriverWait(driver, 15)

# Find Login button
login_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Login']")
    )
)

login_button.click()

# Find mobile number field
mobile = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@type='text']")
    )
)

mobile.send_keys("YOUR_MOBILE_NUMBER")

print("Mobile number entered.")
print("Enter the OTP manually in the browser.")

input("Press Enter here only after you finish the OTP...")

print("Browser is still open.")
input("Press Enter again to close the browser...")
```


# Task 4 – Web Element Verification

This task demonstrates basic Selenium element verification using SauceDemo.

The program checks:

1. Username field
2. Password field
3. Login button
4. Placeholder text
5. Whether the Login button is enabled
6. Whether the username field is displayed

### Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.ID, "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")

print(username.get_attribute("placeholder"))
print(login.is_enabled())
print(username.is_displayed())

login.click()

# driver.quit()
```

### Expected Output

```text
Username
True
True
```

### Explanation

`get_attribute("placeholder")` retrieves the placeholder text of the username field.

```python
username.get_attribute("placeholder")
```

Output:

```text
Username
```

`is_enabled()` checks whether the Login button can be interacted with.

```python
login.is_enabled()
```

Output:

```text
True
```

`is_displayed()` checks whether the username field is visible on the webpage.

```python
username.is_displayed()
```

Output:

```text
True
```

---

# Project Structure

A simple project structure can be:

```text
testing selinium/
│
├── venv/
│
├── product_search.py
├── person_search.py
├── flipkart_login.py
├── element_verification.py
│
└── README.md
```

## How to Run

Activate the virtual environment:

```powershell
venv\Scripts\Activate.ps1
```

Then run each task separately:

```powershell
python product_search.py
```

```powershell
python person_search.py
```

```powershell
python flipkart_login.py
```

```powershell
python element_verification.py
```

---
## OUTPUT
<img width="1905" height="1078" alt="image" src="https://github.com/user-attachments/assets/f0095c3f-e062-417b-a2f7-929b46acfac2" />

<img width="1307" height="1072" alt="image" src="https://github.com/user-attachments/assets/86a5780e-edef-460b-a54b-dca9f3656db2" />

<img width="1287" height="993" alt="image" src="https://github.com/user-attachments/assets/d36cf009-26ae-4848-9b83-492d86a1e23a" />


This project provides hands-on practice with **web automation and functional testing using Selenium and Python**. It covers basic browser automation, element identification, user input, search automation, login testing, element verification, and test OTP handling.

## github link
https://github.com/Sarishatheiveegan/selenium-testing.git
