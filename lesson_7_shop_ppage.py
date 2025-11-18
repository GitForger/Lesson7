from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_7_shop_cart import CartPage

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        self.add_button_locator = "//div[text()='{}']/ancestor::div[@class='inventory_item']//button"
    
    def add_product_to_cart(self, product_name):
        self.driver.find_element(By.XPATH, self.add_button_locator.format(product_name)).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.shopping_cart).click()
        return CartPage(self.driver)
