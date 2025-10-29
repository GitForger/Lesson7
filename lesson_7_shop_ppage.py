from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_7_shop_cart import CartPage

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
        
        self.add_to_cart_buttons = {
            "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
            "Sauce Labs Bolt T-Shirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
            "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie")
        }
    
    def add_product_to_cart(self, product_name):
        button_locator = self.add_to_cart_buttons[product_name]
        self.driver.find_element(*button_locator).click()
    
    def go_to_cart(self):
        self.driver.find_element(*self.shopping_cart).click()
        return CartPage(self.driver)