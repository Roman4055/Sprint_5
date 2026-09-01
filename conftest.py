import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 3)

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

#Для тестов регистрации написана фикстура с генерацией уникального Email, чтобы исключить обшибку дубликатов по Email
@pytest.fixture
def test_user_credentials_random_email():
    random_suffix = f"{random.randint(0, 999):03d}"
    name = "Roman"
    login = f"RomanBessolitsyn52{random_suffix}@yandex.ru"
    password = "123456"
    return name, login, password

#Для тестов регистрации написана фикстура с фиксированным Email, чтобы проверить обшибку дубликатов по Email
@pytest.fixture
def test_user_credentials_fixed_email():
    name = "Roman"
    login = "RomanBessolitsyn52123@yandex.ru"
    password = "123456"
    return name, login, password

