from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.result_field = (By.CSS_SELECTOR, ".screen")
        
        self.buttons = {
            "7": (By.XPATH, "//span[contains(@class, 'btn') and text()='7']"),
            "8": (By.XPATH, "//span[contains(@class, 'btn') and text()='8']"),
            "+": (By.XPATH, "//span[contains(@class, 'btn') and text()='+']"),
            "=": (By.XPATH, "//span[contains(@class, 'btn') and text()='=']"),
        }
    
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, delay_seconds):
        """Устанавливает задержку вычислений"""
        delay_input = self.driver.find_element(*self.delay_field)
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
    
    def click_button(self, button):
        """Нажимает кнопку калькулятора"""
        button_locator = self.buttons[button]
        self.driver.find_element(*button_locator).click()
    
    def wait_for_result(self, expected_result, timeout=50):
        """Ждет пока результат не станет равен expected_result"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*self.result_field).text == expected_result
        )
        print(f"✅ Результат {expected_result} отобразился!")
