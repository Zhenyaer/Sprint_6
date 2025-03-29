from selenium.webdriver.common.by import By


class LocatorsMainPage:
   question_chapter = By.ID, 'accordion__heading-'  # Заготовка локатора важного вопроса без номера элемента
   order_button_bottom = By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]'
   # Кнопка "Заказать" внизу страницы
   order_button_top = By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]'  # Кнопка "Заказать"
                                                                                                # вверху страницы
   response_chapter = By.ID, 'accordion__panel-'  # Заготовка локатора ответа на вопрос без номера элемента
   button_cookie = By.ID, 'rcc-confirm-button'
