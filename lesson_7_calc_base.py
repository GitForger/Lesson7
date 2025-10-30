from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        self.button_locator = "//span[contains(@class, 'btn') and text()='{}']"
    
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, delay_seconds):
        delay_input = self.driver.find_element(*self.delay_field)
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
    
    def click_button(self, button):
        self.driver.find_element(By.XPATH, self.button_locator.format(button)).click()
    
    def wait_for_result(self, expected_result, timeout=50):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*self.result_field).text == expected_result
        )
