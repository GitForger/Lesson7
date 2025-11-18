from selenium import webdriver
from selenium.webdriver.common.by import By
from lesson_7_shop_login import LoginPage
from lesson_7_shop_ppage import ProductsPage
from lesson_7_shop_cart import CartPage
from lesson_7_shop_check import CheckoutPage

def test_sauce_demo_checkout():
    driver = webdriver.Chrome()
    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
        
    products_page = ProductsPage(driver)
    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt") 
    products_page.add_product_to_cart("Sauce Labs Onesie")
        
    cart_page = products_page.go_to_cart()
    checkout_page = cart_page.click_checkout()

    checkout_page.fill_checkout_form("Иван", "Петров", "123456")
        
    total = checkout_page.get_total_amount()
    assert total == "58.29", f"Ожидалась сумма 58.29, но получили {total}"
    driver.save_screenshot("Shop_result.png")
    print("✅ Тест пройден! Итоговая сумма: $58.29")
        
    driver.quit()

if __name__ == "__main__":
    test_sauce_demo_checkout()

