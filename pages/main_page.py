import allure
from locators.main_page_locators import LocatorsMainPage
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Скролл страницы до важного вопроса')
    def scroll_to_important_question(self, question_id):
        question_locator = self.format_locators(LocatorsMainPage.question_chapter, question_id)
        return self.scroll_to_element(question_locator)

    @allure.step('Клик по важному вопросу')
    def click_to_important_question(self, question_id):
        question_locator = self.format_locators(LocatorsMainPage.question_chapter, question_id)
        return self.click_on_element(question_locator)

    @allure.step('Получение ответа на важный вопрос')
    def get_response_to_important_question(self, question_id):
        response_locator = self.format_locators(LocatorsMainPage.response_chapter, question_id)
        return self.get_text_element(response_locator)

    @allure.step('Клик по кнопке "Заказать" на главной странице')
    def click_order(self, order_button):
        self.click_on_element(LocatorsMainPage.button_cookie)
        return self.click_on_element(order_button)
