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
driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]').send_keys(login_standard_user)
driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys(password)
driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn_action"]').click()
text_products = driver.find_element(By.CSS_SELECTOR, 'span[class="title"]').text
assert text_products == "PRODUCTS"
print("Login successful")

#  Выбрать два товара
driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-fleece-jacket"]').click()
driver.find_element(By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

# Сохранить в переменные называния и цены товаров

text_product_1 = driver.find_element(By.CSS_SELECTOR, 'a[id="item_1_title_link"]').text
text_product_2 = driver.find_element(By.CSS_SELECTOR, 'a[id="item_5_title_link"]').text
price_product_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[3]/div[2]/div[2]/div').text
price_product_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[4]/div[2]/div[2]/div').text
print(text_product_1, ' ', price_product_1, '\n', text_product_2, ' ', price_product_2, sep='')
Text_product_1 = text_product_1
Text_product_2 = text_product_2
Price_product_1 = price_product_1
Price_product_2 = price_product_2

# Сравнить названия и цены товаров

assert text_product_1 == Text_product_1
assert text_product_2 == Text_product_2
assert price_product_1 == Price_product_1
assert price_product_2 == Price_product_2
print("Products are equal")

# Перейти в корзину
driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

# Проверить названия и цены товаров в корзине
text_product_1_cart = driver.find_element(By.CSS_SELECTOR, 'a[id="item_1_title_link"]').text
text_product_2_cart = driver.find_element(By.CSS_SELECTOR, 'a[id="item_5_title_link"]').text
price_product_1_cart = driver.find_element(By.XPATH,
                                           '//*[@id="cart_contents_container"]/div/div[1]/div[4]/div[2]/div[2]/div').text
price_product_2_cart = driver.find_element(By.XPATH,
                                           '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text

print(text_product_1_cart, ' ', price_product_1_cart, '\n', text_product_2_cart, ' ', price_product_2_cart, sep='')
Text_product_1_cart = text_product_1_cart
Text_product_2_cart = text_product_2_cart
Price_product_1_cart = price_product_1_cart
Price_product_2_cart = price_product_2_cart

assert text_product_1_cart == Text_product_1_cart
assert text_product_2_cart == Text_product_2_cart
assert price_product_1_cart == Price_product_1_cart
assert price_product_2_cart == Price_product_2_cart
print("Products are equal")

# Перейти к оформлению заказа
driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn_action btn_medium checkout_button"]').click()

# Заполнить поля для оформления заказа
First_name = "John"
Last_name = "Doe"
ZIP = "123 Any Street"

driver.find_element(By.CSS_SELECTOR, 'input[id="first-name"]').send_keys(First_name)
driver.find_element(By.CSS_SELECTOR, 'input[id="last-name"]').send_keys(Last_name)
driver.find_element(By.CSS_SELECTOR, 'input[id="postal-code"]').send_keys(ZIP)

driver.find_element(By.CSS_SELECTOR, 'input[class="submit-button btn btn_primary cart_button btn_action"]').click()

# Проверить названия и цены и сумму товаров
text_product_1_checkout = driver.find_element(By.CSS_SELECTOR, 'a[id="item_1_title_link"]').text
text_product_2_checkout = driver.find_element(By.CSS_SELECTOR, 'a[id="item_5_title_link"]').text
price_product_1_checkout = driver.find_element(By.XPATH,
                                               '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div[2]/div').text
price_product_2_checkout = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div').text


print(text_product_1_checkout, ' ', price_product_1_checkout, '\n', text_product_2_checkout, ' ', price_product_2_checkout, sep='')

Text_product_1_checkout = text_product_1_checkout
Text_product_2_checkout = text_product_2_checkout
Price_product_1_checkout = price_product_1_checkout
Price_product_2_checkout = price_product_2_checkout

assert text_product_1_checkout == Text_product_1_checkout
assert text_product_2_checkout == Text_product_2_checkout
assert price_product_1_checkout == Price_product_1_checkout
assert price_product_2_checkout == Price_product_2_checkout
print("Products are equal")

# Проверить сумму заказа

Item_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[5]').text
print(Item_total)
Item_total_checkout = float(Price_product_1_checkout[1:]) + float(Price_product_2_checkout[1:])
Item_total = float(Item_total[13:])
assert Item_total == Item_total_checkout
print("Item total is equal")

# Оформить заказ
driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn_action btn_medium cart_button"]').click()

text_checkout_complete = driver.find_element(By.CSS_SELECTOR, 'span[class="title"]').text
Text_checkout_complete = text_checkout_complete
assert text_checkout_complete == Text_checkout_complete
print("Checkout complete")