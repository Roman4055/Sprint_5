from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PageLocators 
from tests.helpers import open_registration_form

class TestRegistration:

    #Тест попытки регистрации с "Уникальным" Email
    def test_registration_with_valid_random_Email(self, wait, driver, base_url, test_user_credentials_random_email):
        name, login, password = test_user_credentials_random_email
        driver.get(base_url)
        open_registration_form(wait)
            
        #Заполнение всех полей ввода
        wait.until(EC.element_to_be_clickable(PageLocators.NAME_INPUT)).send_keys(name)
        wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
        wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password)

        #Клик по кнопке "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(PageLocators.REGISTER_BUTTON)).click()

        # Основная проверка: после успешной регистрации должен появиться заголовок «Вход»
        login_header = wait.until(EC.visibility_of_element_located(PageLocators.LOGIN_LINK_AFTER_REG))
        assert login_header.is_displayed()

    #Тест попытки регистрации с паролем меньше 6 символов
    def test_registration_with_short_password(self, wait, driver, base_url, test_user_credentials_random_email):
        name, login, password = test_user_credentials_random_email
        driver.get(base_url)
        open_registration_form(wait)

        #Заполнение всех полей ввода
        wait.until(EC.element_to_be_clickable(PageLocators.NAME_INPUT)).send_keys(name)
        wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
        wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password[0:3])
        
        #Клик по кнопке "Зарегистрироваться"
        wait.until(EC.element_to_be_clickable(PageLocators.REGISTER_BUTTON)).click()

        # Основная проверка: должно отобразиться сообщение «Некорректный пароль»
        invalid_pass_msg = wait.until(EC.visibility_of_element_located(PageLocators.NOT_VAL_PAS_MESSAGE))
        assert invalid_pass_msg.is_displayed()
