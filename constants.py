from selenium.webdriver.common.by import By


class Locators:
    REGISTRATION_BUTTON = (By.XPATH, "//button[contains(., 'Зарегистрироваться')]") #кнопка Регистрации
    INPUT_NAME = (By.XPATH, "//label[text()='Имя']/../input") #ввод имени
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/../input") #ввод электронной почты
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/../input") #ввод пароля
    ERROR_VALIDATION = (By.XPATH, "//p[contains(@class, 'input__error text_type_main-default')]") #ошибка валидации
    BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Булки')]") #кнопка Булки
    SAUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Соусы')]") #кнопка Соусы
    FILLINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Начинки')]") #кнопка Начинки
    MAIN_PAGE_LOG_IN_BUTTON = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]") #Вход на главной странице
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']") #кнопка Войти
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") #кнопка Оформить заказ
    ACCOUNT_BUTTON = (By.XPATH, "//p[contains(., 'Личный Кабинет')]") #кнопка Личный кабинет
    ENTER_FROM_REGISTRATION_PAGE_BUTTON_FORGOT_PASSWORD = (By.XPATH, "//a[contains(., 'Войти')]") #кнопка Войти со страницы регистрации, когда забыт пароль
    PROFILE_BUTTON = (By.XPATH, "//a[contains(., 'Профиль')]") #профиль в Личном кабинете
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(., 'Конструктор')]") #кнопка Конструктор на главной
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]") #логотип сайта
    MAKE_BURGER_TEXT = (By.XPATH, "//h1[contains(., 'Соберите бургер')]") #"Соберите бургер" - текст на главной странице
    EXIT_BUTTON = (By.XPATH, "//button[contains(., 'Выход')]") #кнопка "Выйти" со страницы аккаунта

class Urls:
    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"
    REGISTRATION_PAGE = "https://stellarburgers.nomoreparties.site/register"
    FORGOT_PASSWORD_PAGE = "https://stellarburgers.nomoreparties.site/forgot-password"

class Data:
    LOGIN = "tatyanakhaneeva17258@gmail.com"
    PASSWORD = "25081996"
    NAME = "name"
    REGISTRATION_EMAIL = "258@ya.ru"
    VALID_PASSWORD = "123456"
    SHORT_PASSWORD = "123"

class Errors:
    USER_ALREADY_EXIST = "Такой пользователь уже существует"
    WRONG_PASSWORD = "Некорректный пароль"