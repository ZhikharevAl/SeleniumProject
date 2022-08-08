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

""" Login to Saucedemo """
driver.find_element(By.ID, "user-name").send_keys(login_standard_user)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CLASS_NAME, "btn_action").click()
text_products = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
assert text_products == "Sauce Labs Backpack"
print("Login successful")

#  Выбрать два товара

driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

# Сохранить в переменные называния и цены товаров

text_product_1 = driver.find_element(By.XPATH,
                                     "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[1]/a/div[1]").text
text_product_2 = driver.find_element(By.XPATH,
                                     "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/a/div").text
text_product_1_price = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div["
                                                     "2]/div").text
text_product_2_price = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div["
                                                     "2]/div").text
print(text_product_1, text_product_1_price, '\n', text_product_2, text_product_2_price, sep='')


# Сравнить названия и цены товаров

assert text_product_1 == "Sauce Labs Bolt T-Shirt"
assert text_product_2 == "Sauce Labs Fleece Jacket"
assert text_product_1_price == "$15.99"
assert text_product_2_price == "$49.99"
print("Products are equal")
