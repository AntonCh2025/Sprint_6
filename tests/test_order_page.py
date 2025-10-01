from selenium import webdriver
import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

from data.data import orders


class TestOrderPage:

    @allure.title("Проверка заказа самоката")
    @pytest.mark.parametrize('order', orders)
    def test_order_succesfull_order(self, order, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.accept_cookie_click()
        main_page.order_button_click(order['button'])

        order_page = OrderPage(browser)
        order_page.fill_order_data(order)
        assert order_page.is_order_success()

    @allure.title("Проверка перехода на главную страницу при клике на логотип самоката")    
    def test_scooter_logo_click_start_page_opened(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.order_top_button_click()
        main_page.scooter_logo_click()
        url = main_page.get_current_url()
        assert url == main_page.url
