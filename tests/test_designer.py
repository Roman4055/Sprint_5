from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PageLocators 

#   TAB_BUNS       - Вкладка "Булки"
#   TAB_SAUCES     - Вкладка "Соусы"
#   TAB_FILLINGS   - Вкладка "Начинки"

# вход по кнопке «Войти в аккаунт»
def login_account(wait, login, password):
    # Клик по кнопке "Войти в аккаунт"
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_FROM_HOME)).click()
    #ввод данных
    wait.until(EC.element_to_be_clickable(PageLocators.EMAIL_INPUT)).send_keys(login)
    wait.until(EC.element_to_be_clickable(PageLocators.PASSWORD_INPUT)).send_keys(password)

    #Клик по кнопке "Войти" после ввода логина и пароля
    wait.until(EC.element_to_be_clickable(PageLocators.LOGIN_SUBMIT)).click()

    # Ждём, пока на экране появится кнопка "Оформить заказ"
    wait.until(EC.visibility_of_element_located(PageLocators.BUTTON_PLACE_AN_ORDER))
    
# Хелпер для проверки, активна ли конкретная вкладка (твой «вариант 3»)
def is_tab_active(wait, locator):
    el = wait.until(EC.presence_of_element_located(locator))
    return "tab_tab_type_current__" in el.get_attribute("class")


#Тест перехода по вкладкам конструктора в Соусы
def test_desinger_tab_navigation_buns_sauces(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")
    login_account(wait, login, password)

    # Клик по вкладке «Соусы»
    wait.until(EC.element_to_be_clickable(PageLocators.TAB_SAUCES)).click()

    # Ждём, пока у элемента появится класс активности (это и есть настоящая проверка)
    wait.until(
        lambda d: "tab_tab_type_current__" in d.find_element(*PageLocators.TAB_SAUCES).get_attribute("class")
    )

    # Теперь можно смело делать assert — мы уже точно знаем, что класс есть
    assert is_tab_active(wait, PageLocators.TAB_SAUCES)

#Тест перехода по вкладкам конструктора в Начинки
def test_desinger_tab_navigation_sauces_fillings(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")
    login_account(wait, login, password)

    # Клик по вкладке «Начинки»
    wait.until(EC.element_to_be_clickable(PageLocators.TAB_FILLINGS)).click()

    # Ждём, пока у элемента появится класс активности (это и есть настоящая проверка)
    wait.until(
        lambda d: "tab_tab_type_current__" in d.find_element(*PageLocators.TAB_FILLINGS).get_attribute("class")
    )

    # Теперь можно смело делать assert — мы уже точно знаем, что класс есть
    assert is_tab_active(wait, PageLocators.TAB_FILLINGS)

#Тест перехода по вкладкам конструктора в Булки
def test_desinger_tab_navigation_fillings_buns(wait, driver, test_user_credentials_fixed_email):
    _, login, password = test_user_credentials_fixed_email
    driver.get("https://stellarburgers.education-services.ru/")
    login_account(wait, login, password)

    # Клик по вкладке «Начинки» (исходная)
    wait.until(EC.element_to_be_clickable(PageLocators.TAB_FILLINGS)).click()

    # Клик по вкладке «Булки» (целевая)
    wait.until(EC.element_to_be_clickable(PageLocators.TAB_BUNS)).click()

    # Ждём, пока у элемента появится класс активности (это и есть настоящая проверка)
    wait.until(
        lambda d: "tab_tab_type_current__" in d.find_element(*PageLocators.TAB_BUNS).get_attribute("class")
    )

    # Теперь можно смело делать assert — мы уже точно знаем, что класс есть
    assert is_tab_active(wait, PageLocators.TAB_BUNS)