import pytest
from selenium import webdriver
from lesson_7_calc_base import CalculatorPage


def test_calculator_with_delay():
    driver = webdriver.Chrome()
    calculator = CalculatorPage(driver)
    
    calculator.open()
    calculator.set_delay(45)
    
    calculator.click_button("7")
    driver.save_screenshot("b7.png")
    calculator.click_button("+")
    driver.save_screenshot("b+.png")
    calculator.click_button("8")
    calculator.click_button("=")
    driver.save_screenshot("b=.png")
    
    calculator.wait_for_result("15")
    driver.save_screenshot("result.png")
    print("✅ Тест пройден!")
    
    driver.quit()

if __name__ == "__main__":
    test_calculator_with_delay()