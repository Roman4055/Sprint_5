from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PageLocators 

#Открывает главную страницу и доходит до формы регистрации
def open_registration_form(driver, wait):
    
    driver.get("https://stellarburgers.education-services.ru/")

    # Клик по кнопке "Войти в аккаунт"
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_FROM_HOME)).click()

    # Клик по ссылке "Зарегистрироваться"
    wait.until(EC.element_to_be_clickable(PageLocators.REGISTER_LINK)).click()

    # Ждём, пока форма регистрации появится на экране
    wait.until(EC.visibility_of_element_located(PageLocators.HEADER_REGISTRATION))

#Тест попытки регистрации с уже зарегистрированнм Email
def test_registration_with_valid_fixed_Email(wait, driver, test_user_credentials_fixed_email):
    name, login, password = test_user_credentials_fixed_email

    open_registration_form(driver, wait)

    #Заполнение всех полей ввода в форме регистрации
    wait.until(EC.element_to_be_clickable(PageLocators.NAME_INPUT)).send_keys(name)
    wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
    wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password)

    #Клик по кнопке "Зарегистрироваться"
    wait.until(EC.element_to_be_clickable(PageLocators.REGISTER_BUTTON)).click()

    #Ожидание сообщения о дублировании Email
    wait.until(EC.visibility_of_element_located(PageLocators.ERROR_MESSAGE))

#Тест попытки регистрации с "Уникальным" Email
def test_registration_with_valid_random_Email(wait, driver, test_user_credentials_random_email):
    name, login, password = test_user_credentials_random_email

    open_registration_form(driver, wait)
        
    #Заполнение всех полей ввода
    wait.until(EC.element_to_be_clickable(PageLocators.NAME_INPUT)).send_keys(name)
    wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
    wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password)

    #Клик по кнопке "Зарегистрироваться"
    wait.until(EC.element_to_be_clickable(PageLocators.REGISTER_BUTTON)).click()

    #Ожидание успешного логина
    wait.until(EC.visibility_of_element_located(PageLocators.LOGIN_LINK_AFTER_REG))

#Тест попытки регистрации с паролем меньше 6 символов
def test_registration_with_short_password(wait, driver, test_user_credentials_random_email):
    name, login, password = test_user_credentials_random_email

    open_registration_form(driver, wait)

    #Заполнение всех полей ввода
    wait.until(EC.element_to_be_clickable(PageLocators.NAME_INPUT)).send_keys(name)
    wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
    wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password[0:3])
    
    #Клик по кнопке "Зарегистрироваться"
    wait.until(EC.element_to_be_clickable(PageLocators.REGISTER_BUTTON)).click()

    wait.until(EC.visibility_of_element_located(PageLocators.NOT_VAL_PAS_MESSAGE))       
