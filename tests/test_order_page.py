from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.data import Orders
from data.urls import Url

import pytest
import allure

class TestOrderPage:

    @allure.title("Проверка заказа самоката")
    @pytest.mark.parametrize('order', Orders.orders)
    def test_order_succesfull_order(self, order, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.accept_cookie_click()
        main_page.order_button_click(order['button'])

        order_page = OrderPage(browser)
        order_page.fill_order_data(order)
        assert order_page.is_order_success()
        order_page.show_order_status_click()

        main_page = MainPage(browser)
        main_page.scooter_logo_click()

        assert main_page.get_current_url() == Url.MAIN_PAGE_URL
        main_page.yandex_logo_click()
        main_page.switch_to_new_tab()
        assert main_page.current_url_matches_dzen()
