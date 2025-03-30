import allure
from locators.order_page_locators import LocatorsOrderPage
from locators.dzen_page_locators import LocatorsDzenPage
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Клик по логотипу "Самокат"')
    def click_scooter_logo(self):
        return self.click_on_element(LocatorsOrderPage.scooter_logo)

    @allure.step('Клик по логотипу "Яндекс"')
    def click_yandex_logo(self):
        return self.click_on_element(LocatorsOrderPage.yandex_logo)

    @allure.step('Переход на новую страницу')
    def switch_and_load_dzen(self):
        self.switch_new_page()
        return self.find_element(LocatorsDzenPage.dzen_logo)

    @allure.step('Заполнение поля "Имя"')
    def input_name(self, name):
        return self.fill_field(LocatorsOrderPage.name_field, name)

    @allure.step('Заполнение поля "Фамилия"')
    def input_surname(self, surname):
        return self.fill_field(LocatorsOrderPage.surname_field, surname)

    @allure.step('Заполнение поля "Адрес"')
    def input_address(self, address):
        return self.fill_field(LocatorsOrderPage.address_field, address)

    @allure.step('Заполнение поля "Телефон"')
    def input_phone(self, phone):
        return self.fill_field(LocatorsOrderPage.phone_field, phone)

    @allure.step('Заполнение поля "Метро"')
    def input_metro(self, metro):
        return self.fill_field(LocatorsOrderPage.metro_field, metro)

    @allure.step('Клик по метро из списка')
    def click_on_metro_list(self):
        return self.click_on_element(LocatorsOrderPage.metro_sokolniki)

    @allure.step('Клик по кнопке "Далее" в форме "Для кого самокат"')
    def click_next_button(self):
        return self.click_on_element(LocatorsOrderPage.next_button)

    @allure.step('Заполнение поля "Когда привезти самокат"')
    def input_delivery_time(self, delivery_time):
        return self.fill_field(LocatorsOrderPage.delivery_time, delivery_time)

    @allure.step('Заполнение поля "Срок аренды"')
    def fill_rent_period(self):
        self.click_on_element(LocatorsOrderPage.rent_period)
        self.click_on_element(LocatorsOrderPage.rent_period_list_3days)

    @allure.step('Клик по кнопке "Заказать" в форме "Про аренду"')
    def click_order_button(self):
        return self.click_on_element(LocatorsOrderPage.order_button)

    @allure.step('Клик по кнопке "Да" в окне подтверждения заказа')
    def click_confirm_order(self):
        return self.click_on_element(LocatorsOrderPage.confirm_order)

    @allure.step('Получение подтверждения оформления заказа')
    def check_order_placed(self):
        return self.get_text_element(LocatorsOrderPage.order_placed)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_profile_form(self, name, surname, address, metro, phone):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.input_metro(metro)
        self.click_on_metro_list()
        self.input_phone(phone)

    @allure.step('Заполнение формы "Про аренду"')
    def fill_rent_form(self, delivery_time):
        self.fill_rent_period()
        return self.input_delivery_time(delivery_time)
