from selenium.webdriver.common.by import By

class PageLocators:
    # --- Страница входа / главная ---
    LOGIN_FROM_HOME = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")      # Ссылка «Зарегистрироваться»

    # --- Форма регистрации ---
    HEADER_REGISTRATION = (By.XPATH,'.//h2[normalize-space()="Регистрация"]') # Заголовок  «Регистрация»
    NAME_INPUT = (By.XPATH, './/label[normalize-space()="Имя"]/following-sibling::input')  # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, './/label[normalize-space()="Email"]/following-sibling::input')  # Поле «Email»
    PASSWORD_INPUT = (By.XPATH, '//input[@name="Пароль"]')  # Поле «Пароль» (кириллица в name)
    REGISTER_BUTTON = (By.XPATH, './/button[normalize-space()="Зарегистрироваться"]')  # Кнопка «Зарегистрироваться»

    # --- Элементы результата ---
    LOGIN_LINK_AFTER_REG = (By.XPATH,".//h2[text()='Вход']")  # Ссылка «Вход», появляется при успехе
    ERROR_MESSAGE = (By.XPATH, "//p[normalize-space() ='Такой пользователь уже существует']")  # Сообщение об ошибке валидации
    NOT_VAL_PAS_MESSAGE = (By.XPATH, './/p[normalize-space()="Некорректный пароль"]')# Сообщение об ошибке короткий пароль

    # --- Локаторы для тестов входа в аккаунт ---
    LOGIN_SUBMIT = (By.XPATH, ".//button[normalize-space()='Войти']")# Кнопка "Войти" видна в форме входа
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[normalize-space() = 'Личный Кабинет']") # Кнопка "Личный кабинет" на стартовой странице
    BUTTON_PLACE_AN_ORDER = (By.XPATH, ".//button[text() ='Оформить заказ']") # Кнопка "Оформить заказ" при залогинено пользователе
    BUTTON_LOGIN_REGISTRATION_FORM = (By.XPATH, ".//p[text()='Уже зарегистрированы?']/a") #Кнопка "войти" в форме  регистрации
    BUTTON_LOGIN_PASSWORD_RECOVERY_FORM = (By.XPATH, ".//p[text()='Вспомнили пароль?']/a") #Кнопка "войти" в форме  востановления пароля
    BUTTON_PASSWORD_RECOVERY = (By.XPATH, ".//a[normalize-space() = 'Восстановить пароль']")

    # --- Локаторы для выхода из аккаунта ---
    BUTTON_AUTH_PERSONAL_CABINET = (By.XPATH, ".//p[normalize-space() = 'Личный Кабинет']") # Кнопка "Личный кабинет" для авторизованного пользователя
    BUTTON_LOGOUT = (By.XPATH, ".//button[normalize-space() = 'Выход']") # Кнопка "Выход"

    # --- Локаторы для тестов переходов ---
    BUTTON_DESIGNER = (By.XPATH, "//p[normalize-space() = 'Конструктор']") # Кнопка Конструктор
    BUTTON_ORDER_FEED = (By.XPATH, "//p[normalize-space() = 'Лента Заказов']") # Кнопка Лента Заказов
    LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']") #Логотип

    PROFILE_EDITOR = (By.XPATH, "//p[normalize-space() = 'В этом разделе вы можете изменить свои персональные данные']") #Поле имя в редакторе провиля

    # --- Локаторы активных вкладок ---
    TAB_BUNS = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and text()='Булки']/..")
    TAB_SAUCES = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and text()='Соусы']/..")
    TAB_FILLINGS = (By.XPATH, "//span[contains(@class, 'text_type_main-default') and text()='Начинки']/..")

    # --- Заголовки секций (h2) для проверки переключения ---
    HEADING_BUNS = (By.XPATH, "//h2[text()='Булки']")
    HEADING_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    HEADING_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")
