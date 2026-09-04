from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators
from selenium.webdriver.common.by import By

# Вход через кнопку «Войти в аккаунт» на главной странице.
def login_account(wait, login, password):
    
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_FROM_HOME)).click()
    wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
    wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_SUBMIT)).click()
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))

 # Заполнение полей Email/Пароль и клик по кнопке «Войти». Без клика по «Войти в аккаунт».
def open_login_form(wait, login, password):
   
    wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
    wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password)
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_SUBMIT)).click()

# Открывает главную страницу и доходит до формы регистрации.
def open_registration_form(wait):
        
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_FROM_HOME)).click()
    wait.until(EC.element_to_be_clickable(PageLocators.REGISTER_LINK)).click()
    wait.until(EC.visibility_of_element_located(PageLocators.HEADER_REGISTRATION))

# Проверяет, активна ли вкладка по наличию класса tab_tab_type_current__.
def is_tab_active(wait, locator):
    el = wait.until(EC.presence_of_element_located(locator))
    return "tab_tab_type_current__" in el.get_attribute("class")

# Проверяет, виден ли элемент (есть в DOM и отображается).
def is_heading_visible(driver, locator):
    elements = driver.find_elements(*locator)
    if not elements:
        return False
    return elements[0].is_displayed()