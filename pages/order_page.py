from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

import allure

import locators.order_page_locators as OP


class OrderPage:
    url = 'https://qa-scooter.praktikum-services.ru/order'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def input_name(self, name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OP.name))
        self.driver.find_element(*OP.name).send_keys(name)

    def input_surname(self, surname):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OP.surname))
        self.driver.find_element(*OP.surname).send_keys(surname)

    def input_address(self, address):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OP.address))
        self.driver.find_element(*OP.address).send_keys(address)

    def station_click(self, station):
        xpath = f'//div[@class="select-search__select"]/descendant::*[text()="{station}"]'
        locator = [By.XPATH, xpath]
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def select_metro_station(self, station):
        self.driver.find_element(*OP.metro_station).click()
        self.station_click(station)

    def input_phone_number(self, number):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OP.telephone))
        self.driver.find_element(*OP.telephone).send_keys(number)

    def next_button_click(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OP.next_button))
        self.driver.find_element(*OP.next_button).click()

    def input_delivery_date(self, date):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OP.deliver_date))
        self.driver.find_element(*OP.deliver_date).send_keys(date)
        self.driver.find_element(*OP.deliver_date).send_keys(Keys.RETURN)

    def time_option_click(self, option):
        locator = [By.XPATH, f'//div[@class="Dropdown-menu"]/descendant::*[text()="{option}"]']
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def select_rent_time(self, rent_time):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OP.rent_time))
        self.driver.find_element(*OP.rent_time).click()
        self.time_option_click(rent_time)

    def select_gray_color(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OP.color_gray))
        self.driver.find_element(*OP.color_gray).click()

    def select_black_color(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OP.color_black))
        self.driver.find_element(*OP.color_black).click()

    def select_scooter_color(self, color):
        if color == 'черный':
            self.select_black_color()
        else:
            self.select_gray_color()

    def input_comment(self, comment):
        self.driver.find_element(*OP.comment).send_keys(comment)

    def order_button_click(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OP.rent_button))
        self.driver.find_element(*OP.rent_button).click()

    def confirm_order(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(OP.yes_button))
        self.driver.find_element(*OP.yes_button).click()

    @allure.step("Проверить, что заказ успешно оформлен")
    def is_order_success(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OP.form_success))
        text = self.driver.find_element(*OP.form_success).text
        return "Заказ оформлен" in text

    @allure.step("Оформить заказ")
    def fill_order_data(self, order_data):
        self.input_name(order_data['name'])
        self.input_surname(order_data['surname'])
        self.input_address(order_data['address'])
        self.select_metro_station(order_data['metro'])
        self.input_phone_number(order_data['phone'])
        self.next_button_click()
        self.input_delivery_date(order_data['delivery_date'])
        self.select_rent_time(order_data['rent_time'])
        self.select_scooter_color(order_data['color'])
        self.input_comment(order_data['comment'])
        self.order_button_click()
        self.confirm_order()
