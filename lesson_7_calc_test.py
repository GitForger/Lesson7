from selenium import webdriver
from lesson_7_calc_base import CalculatorPage

def test_calculator_with_delay():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)
    
    calculator.open()
    calculator.set_delay(45)
    
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    
    calculator.wait_for_result("15", timeout=50)
    
    driver.quit()

if __name__ == "__main__":
    test_calculator_with_delay()
