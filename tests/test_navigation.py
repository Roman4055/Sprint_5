from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PageLocators 

# вход по кнопке «Войти в аккаунт»
def login_accaunt(wait, login, password):
    # Клик по кнопке "Войти в аккаунт"
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_FROM_HOME)).click()
    #ввод данных
    wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
    wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password)

    #Клик по кнопке "Войти" после ввода логина и пароля
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_SUBMIT)).click()

    # Ждём, пока на экране появится кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))

#Переход по клику на «Личный кабинет»
def test_navigate_to_personal_cabinet_after_login(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")
    login_accaunt(wait, login, password)

    # Ждём, пока на экране появится кнопка "Лчный кабинет" и нажимаем
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_AUTH_PERSONAL_CABINET)).click()

    # Ждём, пока на экране появится поле "Имя" в редакторе профиля
    wait.until(EC.visibility_of_element_located(PageLocators.NAME_PROFILE_EDITOR))

#Переход из личного кабинета в конструктор 
def test_navigate_from_personal_cabinet_to_constructor(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")
    login_accaunt(wait, login, password)

    # Ждём, пока на экране появится кнопка "Лчный кабинет" и нажимаем
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_AUTH_PERSONAL_CABINET)).click()

    # Ждём, пока на экране появится кнопка "Конструктор" и нажимаем
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_DESIGNER)).click()

    # Ждём, пока на экране появится кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))

#переход по клику на логотип Stellar Burgers.
def test_navigation_via_constructor_link_and_logo(wait, driver, test_user_credentials_fixed_email): 
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")
    login_accaunt(wait, login, password)

    # Ждём, пока на экране появится кнопка "Лчный кабинет" и нажимаем
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_AUTH_PERSONAL_CABINET)).click()

    # Ждём, пока на экране появится кнопка "Конструктор" и нажимаем
    wait.until(EC.visibility_of_element_located(PageLocators.LOGO)).click()

    # Ждём, пока на экране появится кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))