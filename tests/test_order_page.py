import pytest
import allure
from src.config import URL
from pages.order_page import OrderPage
from pages.main_page import MainPage
from src.generate_data import generate_profile, generate_rent_date
from locators.main_page_locators import LocatorsMainPage


class TestsOrderPage:

    @allure.title('Создание заказа')
    @pytest.mark.parametrize('order_button', [LocatorsMainPage.order_button_top, LocatorsMainPage.order_button_bottom])
    def test_create_order(self, driver, order_button):
        main_page = MainPage(driver)
        driver.get(f'{URL.url_main_page}')
        main_page.click_order(order_button)
        order_page = OrderPage(driver)
        order_page.fill_profile_form(
            name=generate_profile()['name'],
            surname=generate_profile()['surname'],
            address=generate_profile()['address'],
            metro=generate_profile()['metro'],
            phone=generate_profile()['phone']
        )
        order_page.click_next_button()
        order_page.fill_rent_form(generate_rent_date())
        order_page.click_order_button()
        order_page.click_confirm_order()
        assert 'Заказ оформлен' in order_page.check_order_placed()

    @allure.title('Проверка перехода на главную страницу при клике по лого "Самокат"')
    def test_click_scooter_logo(self, driver):
        order_page = OrderPage(driver)
        driver.get(f'{URL.url_order_page}')
        order_page.click_scooter_logo()
        assert driver.current_url == f'{URL.url_main_page}'

    @allure.title('Проверка перехода на страницу дзена при клике по лого "Яндекс"')
    def test_click_yandex_logo(self, driver):
        order_page = OrderPage(driver)
        driver.get(f'{URL.url_order_page}')
        order_page.click_yandex_logo()
        order_page.switch_and_load_dzen()
        assert driver.current_url == f'{URL.url_dzen}'
