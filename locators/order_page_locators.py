from selenium.webdriver.common.by import By


class LocatorsOrderPage:
    name_field = By.XPATH, '//input[@placeholder="* Имя"]'  # Поле "Имя"
    surname_field = By.XPATH, './/input[@placeholder="* Фамилия"]'  # Поле "Фамилия"
    address_field = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'  # Поле "Адрес"
    metro_field = By.XPATH, './/input[@placeholder="* Станция метро"]'  # Поле "Станция метро"
    phone_field = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'  # Поле "Телефон"
    next_button = By.XPATH, './/button[text()="Далее"]'  # Кнопка "Далее"
    scooter_logo = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'  # Лого "Самокат"
    yandex_logo = By.CLASS_NAME, 'Header_LogoYandex__3TSOI'  # Лого "Яндекс"
    metro_sokolniki = By.XPATH, './/div[text()="Сокольники"]'  # Метро "Сокольники" из списка
    delivery_time = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'  # Поле "Когда привезти самокат"
    rent_period = By.XPATH, '//div[text()="* Срок аренды"]'  # Поле "Срок аренды"
    rent_period_list_3days = By.XPATH, '//div[@class="Dropdown-option" and text()="трое суток"]'
    order_button = By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]'  # Кнопка "Заказать"
    confirm_order = By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Да"]'  # Кнопка "Да" в окне подтверждения заказа
    order_placed = By.XPATH, '//div[text()="Заказ оформлен"]'

