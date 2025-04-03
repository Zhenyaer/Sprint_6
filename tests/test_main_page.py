import pytest
import allure
from src.config import URL
from src.data import response_to_important_question
from pages.main_page import MainPage


class TestsMainPage:
    @allure.title('Проверка ответов на вопросы о важном')
    @pytest.mark.parametrize('question_id, expected_response', response_to_important_question.items())
    def test_response_to_important_question(self, driver, question_id, expected_response):
        main_page = MainPage(driver)
        driver.get(f'{URL.url_main_page}')
        main_page.scroll_to_important_question(question_id)
        main_page.click_to_important_question(question_id)
        assert main_page.get_response_to_important_question(question_id) == expected_response
