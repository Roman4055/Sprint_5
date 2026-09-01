from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PageLocators 

#Функция заполнения формы входа
def open_login_form(wait, login, password):
    #Заполнение полей "Email" и "Пароль"
    wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
    wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password)

    #Клик по кнопке "Войти" после ввода логина и пароля
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_SUBMIT)).click()

# вход по кнопке «Войти в аккаунт»
def test_login_via_login_button(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")

    # Клик по кнопке "Войти в аккаунт"
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_FROM_HOME)).click()

    #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
    open_login_form(wait, login, password)

    # Ждём, пока на экране появится кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))

# вход через кнопку «Личный кабинет»
def test_login_via_personal_cabinet_button(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")

    #Клик по кнопке "Личный кабинет"
    driver.find_element(*PageLocators.BUTTON_PERSONAL_ACCOUNT).click()

    #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
    open_login_form(wait, login, password)

    # Ждём, пока на экране появится кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))

# вход через кнопку в форме регистрации
def test_login_via_registration_form_link(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")

    #Клик по кнопке "Войти в аккаунт"
    driver.find_element(*PageLocators.LOGIN_FROM_HOME).click()
    # Клик по кнопке "Зарегистрироваться"
    driver.find_element(*PageLocators.REGISTER_LINK).click()
    # Клик по кнопке Войти
    driver.find_element(*PageLocators.BUTTON_LOGIN_REGISTRATION_FORM).click()

    #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
    open_login_form(wait, login, password)

    # Ждём, пока на экране появится кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))

# вход через кнопку в форме восстановления пароля
def test_login_via_password_recovery_form(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")

    #Клик по кнопке "Войти в аккаунт"
    driver.find_element(*PageLocators.LOGIN_FROM_HOME).click()
    # Клик по кнопке "Зарегистрироваться"
    driver.find_element(*PageLocators.BUTTON_PASSWORD_RECOVERY).click()
    # Клик по кнопке Войти
    driver.find_element(*PageLocators.BUTTON_LOGIN_PASSWORD_RECOVERY_FORM).click()

    #Заполнение полей "Email" и "Пароль, клик по кнопке "Войти"
    open_login_form(wait, login, password)

    # Ждём, пока на экране появится кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))

# выход по кнопке «Выйти» в личном кабинете.
def test_logout_via_logout_button(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")

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

    # Ждём, пока на экране появится кнопка "Оформить заказ" 
    wait.until(EC.visibility_of_element_located(PageLocators.LOGIN_SUBMIT))