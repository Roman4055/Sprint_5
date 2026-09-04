from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from helpers import login_account, is_heading_visible 
import time


class TestDesignerNavigation:

    def test_buns_sauces(self, wait, driver, base_url, test_user_credentials_fixed_email):
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)
        login_account(wait, login, password)

        wait.until(EC.element_to_be_clickable(PageLocators.TAB_SAUCES)).click()
        time.sleep(2)

        wait.until(lambda d: is_heading_visible(d, PageLocators.HEADING_SAUCES))
        assert is_heading_visible(driver, PageLocators.HEADING_SAUCES), "Заголовок 'Соусы' не появился"

    def test_sauces_fillings(self, wait, driver, base_url, test_user_credentials_fixed_email):
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)
        login_account(wait, login, password)

        wait.until(EC.element_to_be_clickable(PageLocators.TAB_FILLINGS)).click()
        time.sleep(2)

        wait.until(lambda d: is_heading_visible(d, PageLocators.HEADING_FILLINGS))
        assert is_heading_visible(driver, PageLocators.HEADING_FILLINGS), "Заголовок 'Начинки' не появился"

    def test_fillings_buns(self, wait, driver, base_url, test_user_credentials_fixed_email):
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)
        login_account(wait, login, password)

        wait.until(EC.element_to_be_clickable(PageLocators.TAB_FILLINGS)).click()
        time.sleep(1)

        wait.until(EC.element_to_be_clickable(PageLocators.TAB_BUNS)).click()
        time.sleep(2)

        wait.until(lambda d: is_heading_visible(d, PageLocators.HEADING_BUNS))
        assert is_heading_visible(driver, PageLocators.HEADING_BUNS), "Заголовок 'Булки' не появился"
