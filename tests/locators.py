# locators.py
from selenium.webdriver.common.by import By

class PageLocators:
    # --- Страница входа / главная ---
    LOGIN_FROM_HOME = (By.XPATH, "/html/body/div/div/main/section[2]/div/button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")      # Ссылка «Зарегистрироваться»
    

    # --- Форма регистрации ---
    HEADER_REGISTRATION = (By.XPATH,'.//h2[text()="Регистрация"]') # Заголовок  «Регистрация»
    NAME_INPUT = (By.XPATH, './/label[normalize-space()="Имя"]/following-sibling::input')  # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, './/label[normalize-space()="Email"]/following-sibling::input')  # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')  # Поле «Пароль» (кириллица в name)
    REGISTER_BUTTON = (By.XPATH, './/button[normalize-space()="Зарегистрироваться"]')  # Кнопка «Зарегистрироваться»

    # --- Элементы результата ---
    LOGIN_LINK_AFTER_REG = (By.XPATH,".//h2[normalize-space()='Вход']")  # Ссылка «Вход», появляется при успехе
    ERROR_MESSAGE = (By.XPATH, "//*[@id='root']/div/main/div/p")  # Сообщение об ошибке валидации
    NOT_VAL_PAS_MESSAGE = (By.XPATH, './/p[normalize-space()="Некорректный пароль"]')# Сообщение об ошибке короткий пароль

    # --- Локаторы для тестов входа в аккаунт ---
    LOGIN_SUBMIT = (By.XPATH, ".//*[@id='root']/div/main/div/form/button")# Кнопка "Войти" видна в форме входа
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//*[@id='root']/div/header/nav/a/p[text()= 'Личный Кабинет']") # Кнопка "Личный кабинет" на стартовой странице
    BUTTON_PLACE_AN_ORDER = (By.XPATH, ".//*[@id='root']/div/main/section[2]/div/button[text()='Оформить заказ']") # Кнопка "Оформить заказ" при залогинено пользователе
    BUTTON_LOGIN_REGISTRATION_FORM = (By.XPATH, ".//p[text()='Уже зарегистрированы?']/a") #Кнопка "войти" в форме  регистрации
    BUTTON_LOGIN_PASSWORD_RECOVERY_FORM = (By.XPATH, ".//p[text()='Вспомнили пароль?']/a") #Кнопка "войти" в форме  востановления пароля
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, ".//a[text()= 'Восстановить пароль']")

    # --- Локаторы для выхода из аккаунта ---
    BUTTON_AUTH_PERSONAL_CABINET = (By.XPATH, "//*[@id='root']/div/header/nav/a/p[text()='Личный Кабинет']") # Кнопка "Личный кабинет" для авторизованного пользователя
    BUTTON_LOGOUT = (By.XPATH, "//*[@id='root']/div/main/div/nav/ul/li[3]/button[text()='Выход']") # Кнопка "Выход"

    # --- Локаторы для тестов переходов ---
    BUTTON_DESIGNER = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[1]/a/p[text()='Конструктор']") # Кнопка Конструктор
    BUTTON_ORDER_FEED = (By.XPATH, "//*[@id='root']/div/header/nav/ul/li[2]/a/p[text()='Лента Заказов']") # Кнопка Лента Заказов
    LOGO = (By.XPATH, "//*[@id='root']/div/header/nav/div/a") #Логотип

    TAB_BUNS = (By.XPATH, "//div[contains(@class,'tab_tab__') and .//span[normalize-space()='Булки']]") # Вкладка «Булки»
    TAB_SAUCES = (By.XPATH, "//div[contains(@class,'tab_tab__') and .//span[normalize-space()='Соусы']]") # Вкладка «Соусы»
    TAB_FILLINGS = (By.XPATH, "//div[contains(@class,'tab_tab__') and .//span[normalize-space()='Начинки']]") # Вкладка «Начинки»

    NAME_PROFILE_EDITOR = (By.XPATH, "//*[@id='root']/div/main/div/div/div/ul/li[1]/div/div") #Поле имя в редакторе провиля

