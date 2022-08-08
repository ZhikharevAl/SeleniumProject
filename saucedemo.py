import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
base_url = "https://www.saucedemo.com/"
driver.get(base_url)

login_standard_user = "standard_user"
password = "secret_sauce"

driver.find_element(By.ID, "user-name").send_keys(login_standard_user)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CLASS_NAME, "btn_action").click()
text_products = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
assert text_products == "Sauce Labs Backpack"
print("Login successful")
