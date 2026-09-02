from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PageLocators 
from tests.helpers import open_login_form

class TestLoginLogout:

    # вход по кнопке «Войти в аккаунт»
    def test_login_via_login_button(self, wait, driver, base_url, test_user_credentials_fixed_email):
        
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)

        # Клик по кнопке "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_FROM_HOME)).click()

        #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
        open_login_form(wait, login, password)

        # Основная проверка: кнопка "Оформить заказ" появилась — вход выполнен
        btn_order = wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))
        assert btn_order.is_displayed()

    # вход через кнопку «Личный кабинет»
    def test_login_via_personal_cabinet_button(self, wait, driver, base_url, test_user_credentials_fixed_email):
        
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)

        #Клик по кнопке "Личный кабинет"
        driver.find_element(*PageLocators.BUTTON_PERSONAL_ACCOUNT).click()

        #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
        open_login_form(wait, login, password)

        # Основная проверка
        btn_order = wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))
        assert btn_order.is_displayed()

    # вход через кнопку в форме регистрации
    def test_login_via_registration_form_link(self, wait, driver, base_url, test_user_credentials_fixed_email):
        
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)

        #Клик по кнопке "Войти в аккаунт"
        driver.find_element(*PageLocators.LOGIN_FROM_HOME).click()
        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(*PageLocators.REGISTER_LINK).click()
        # Клик по кнопке Войти
        driver.find_element(*PageLocators.BUTTON_LOGIN_REGISTRATION_FORM).click()

        #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
        open_login_form(wait, login, password)

        # Основная проверка
        btn_order = wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))
        assert btn_order.is_displayed()

    # вход через кнопку в форме восстановления пароля
    def test_login_via_password_recovery_form(self, wait, driver, base_url, test_user_credentials_fixed_email):
        
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)

        #Клик по кнопке "Войти в аккаунт"
        driver.find_element(*PageLocators.LOGIN_FROM_HOME).click()
        # Клик по кнопке "Зарегистрироваться"
        driver.find_element(*PageLocators.BUTTON_PASSWORD_RECOVERY).click()
        # Клик по кнопке Войти
        driver.find_element(*PageLocators.BUTTON_LOGIN_PASSWORD_RECOVERY_FORM).click()

        #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
        open_login_form(wait, login, password)

        # Основная проверка
        btn_order = wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))
        assert btn_order.is_displayed(), "После входа через форму восстановления пароля должна отобразиться кнопка «Оформить заказ»"

    # выход по кнопке «Выйти» в личном кабинете.
    def test_logout_via_logout_button(self, wait, driver, base_url, test_user_credentials_fixed_email):
        
        _, login, password = test_user_credentials_fixed_email
        driver.get(base_url)

        # Клик по кнопке "Войти в аккаунт"
        wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_FROM_HOME)).click()

        #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
        open_login_form(wait, login, password)

        # Ждём, пока на экране появится кнопка "Оформить заказ" 
        wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))

        # Ждём, пока на экране появится кнопка "Лчный кабинет" и нажимаем
        wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_AUTH_PERSONAL_CABINET)).click()

        # Ждём, пока на экране появится кнопка "Выход" и нажимаем
        wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_LOGOUT)).click()

        # Основная проверка: после выхода должна появиться кнопка "Войти" (форма входа)
        login_submit = wait.until(EC.visibility_of_element_located(PageLocators.LOGIN_SUBMIT))
        assert login_submit.is_displayed()
