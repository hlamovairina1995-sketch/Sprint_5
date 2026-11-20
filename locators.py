
from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")  # «Конструктор» в шапке
    LOGO = (By.XPATH, "//header//a[.//*[name()='svg']]")  # Логотип Stellar Burgers
    ACCOUNT_LINK = (By.CSS_SELECTOR, "header a[href='/account']")  # «Личный кабинет» в шапке


class HomeLocators:
    TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")  # Заголовок конструктора
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")  # Вход с главной страницы
    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")  # Кнопка заказа после авторизации


class LoginLocators:
    TITLE = (By.XPATH, "//h2[normalize-space()='Вход']")  # Заголовок формы входа
    EMAIL_INPUT = (By.XPATH, "//form//label[normalize-space()='Email']/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.CSS_SELECTOR, "form input[type='password']")  # Поле Пароль
    SUBMIT_BUTTON = (By.XPATH, "//form//button[normalize-space()='Войти']")  # Кнопка «Войти»
    REGISTER_LINK = (By.CSS_SELECTOR, "main a[href='/register']")  # Ссылка к регистрации
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "main a[href='/forgot-password']")  # Ссылка к восстановлению пароля


class RegistrationLocators:
    TITLE = (By.XPATH, "//h2[normalize-space()='Регистрация']")  # Заголовок регистрации
    NAME_INPUT = (By.XPATH, "//form//label[normalize-space()='Имя']/following-sibling::input")  # Поле «Имя»
    EMAIL_INPUT = (By.XPATH, "//form//label[normalize-space()='Email']/following-sibling::input")  # Поле Email
    PASSWORD_INPUT = (By.CSS_SELECTOR, "form input[type='password']")  # Поле пароля (без повторного ввода)
    SUBMIT_BUTTON = (By.XPATH, "//form//button[normalize-space()='Зарегистрироваться']")  # Кнопка регистрации
    LOGIN_LINK = (By.CSS_SELECTOR, "main a[href='/login']")  # Ссылка «Войти» под регистрацией
    PASSWORD_ERROR = (By.XPATH, "//p[normalize-space()='Некорректный пароль']")  # Ошибка при коротком пароле


class RecoveryLocators:
    TITLE = (By.XPATH, "//h2[normalize-space()='Восстановление пароля']")  # Заголовок восстановления
    LOGIN_LINK = (By.CSS_SELECTOR, "main a[href='/login']")  # Ссылка «Войти» под восстановлением


class AccountLocators:
    PROFILE_LINK = (By.CSS_SELECTOR, "a[href='/account/profile']")  # Пункт «Профиль» в личном кабинете
    ORDER_HISTORY_LINK = (By.CSS_SELECTOR, "a[href='/account/order-history']")  # Пункт «История заказов»
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")  # Кнопка выхода (на сайте текст «Выход»)


class ConstructorLocators:
    BUNS_TAB = (By.XPATH, "//span[normalize-space()='Булки']/parent::div")  # Вкладка «Булки»
    SAUCES_TAB = (By.XPATH, "//span[normalize-space()='Соусы']/parent::div")  # Вкладка «Соусы»
    FILLINGS_TAB = (By.XPATH, "//span[normalize-space()='Начинки']/parent::div")  # Вкладка «Начинки»
    BUNS_ACTIVE = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span[normalize-space()='Булки']/..")  # Активная вкладка «Булки»
    SAUCES_ACTIVE = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span[normalize-space()='Соусы']/..")  # Активная вкладка «Соусы»
    FILLINGS_ACTIVE = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span[normalize-space()='Начинки']/..")  # Активная вкладка «Начинки»