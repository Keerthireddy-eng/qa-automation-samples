from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_page_loads():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    assert "Login" in driver.title
    time.sleep(2)

    driver.quit()
