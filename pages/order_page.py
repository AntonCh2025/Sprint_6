from selenium.webdriver.common.keys import Keys

import locators.order_page_locators as OP
from data.urls import Url
from pages.base_page import BasePage
from helpers.locator_maker import LocatorMaker

import allure


class OrderPage(BasePage):

    @allure.step("Открыть страницу заказа самоката")
    def open(self):
        self.open_url(Url.ORDER_PAGE_URL)

    def input_name(self, name):
        self.fill_input(OP.name, name)

    def input_surname(self, surname):
        self.fill_input(OP.surname, surname)

    def input_address(self, address):
        self.fill_input(OP.address, address)

    def select_metro_station(self, station):
        self.element_click(OP.metro_station)
        self.element_click(LocatorMaker.metro_station(station))

    def input_phone_number(self, number):
        self.fill_input(OP.telephone, number)

    def next_element_click(self):
        self.element_click(OP.next_button)

    def input_delivery_date(self, date):
        self.fill_input(OP.deliver_date, date)
        self.fill_input(OP.deliver_date, Keys.RETURN)

    def select_rent_time(self, rent_time):
        self.element_click(OP.rent_time)
        self.element_click(LocatorMaker.time_option(rent_time))

    def select_gray_color(self):
        self.element_click(OP.color_gray)

    def select_black_color(self):
        self.element_click(OP.color_black)

    def select_scooter_color(self, color):
        if color == 'черный':
            self.select_black_color()
        else:
            self.select_gray_color()

    def input_comment(self, comment):
        self.fill_input(OP.comment, comment)

    def order_element_click(self):
        self.element_click(OP.rent_button)

    def confirm_order(self):
        self.element_click(OP.yes_button)

    @allure.step("Проверить, что заказ успешно оформлен")
    def is_order_success(self):
        text = self.get_element_text(OP.form_success)
        return "Заказ оформлен" in text

    @allure.step("Оформить заказ")
    def fill_order_data(self, order_data):
        self.input_name(order_data['name'])
        self.input_surname(order_data['surname'])
        self.input_address(order_data['address'])
        self.select_metro_station(order_data['metro'])
        self.input_phone_number(order_data['phone'])
        self.next_element_click()
        self.input_delivery_date(order_data['delivery_date'])
        self.select_rent_time(order_data['rent_time'])
        self.select_scooter_color(order_data['color'])
        self.input_comment(order_data['comment'])
        self.order_element_click()
        self.confirm_order()

    def show_order_status_click(self):
        self.element_click(OP.show_status_button)
