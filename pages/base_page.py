import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента по локатору')
    def find_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).click()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))

    @allure.step('Получение текст элемента')
    def get_text_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    # Форматирование локатора
    @staticmethod
    def format_locators(locator, question_id):
        locator_format = (locator[0], locator[1] + str(question_id))
        return locator_format

    @allure.step('Заполнение поля')
    def fill_field(self, locator, text):
        return self.driver.find_element(*locator).send_keys(text)

    @allure.step('Переход на открывшуюся страницу')
    def switch_new_page(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])
