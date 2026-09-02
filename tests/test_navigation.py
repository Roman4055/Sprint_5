from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PageLocators 
from tests.helpers import login_account

class TestsNavigation:

    #Переход по клику на «Личный кабинет»
    def test_navigate_to_personal_cabinet_after_login(self,  wait, driver, base_url, test_user_credentials_fixed_email):
        
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)
        login_account(wait, login, password)

        # Ждём, пока на экране появится кнопка "Лчный кабинет" и нажимаем
        wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_AUTH_PERSONAL_CABINET)).click()

        # Проверяем, что открылся редактор профиля (есть поле «Имя»)
        profile_editor = wait.until(EC.visibility_of_element_located(PageLocators.PROFILE_EDITOR))
        assert profile_editor.is_displayed()

    #Переход из личного кабинета в конструктор 
    def test_navigate_from_personal_cabinet_to_constructor(self, wait, driver, base_url, test_user_credentials_fixed_email):
        
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)
        login_account(wait, login, password)

        # Ждём, пока на экране появится кнопка "Лчный кабинет" и нажимаем(Исходная позиция)
        wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_AUTH_PERSONAL_CABINET)).click()

        # Ждём, пока на экране появится кнопка "Конструктор" и нажимаем(Переход в целевую позицию)
        wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_DESIGNER)).click()

        # Проверяем возврат в зону конструктора (кнопка «Оформить заказ»)
        btn_place_order = wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))
        assert btn_place_order.is_displayed()

    #переход по клику на логотип Stellar Burgers.
    def test_navigation_via_constructor_link_and_logo(self, wait, driver, base_url, test_user_credentials_fixed_email): 
        
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)
        login_account(wait, login, password)

        # Ждём, пока на экране появится кнопка "Лчный кабинет" и нажимаем
        wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_AUTH_PERSONAL_CABINET)).click()

    # Кликаем логотип
        wait.until(EC.visibility_of_element_located(PageLocators.LOGO)).click()

        # Проверяем, что вернулись в конструктор
        btn_place_order = wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))
        assert btn_place_order.is_displayed()