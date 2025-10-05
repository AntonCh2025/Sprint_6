from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.data import Orders

import pytest
import allure

class TestOrderPage:

    @allure.title("Проверка заказа самоката. Точка входа: {description}")
    @pytest.mark.parametrize('button, description, order', Orders.orders)
    def test_order_succesfull_order(self, button, description, order, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.accept_cookie_click()
        main_page.order_button_click(button)

        order_page = OrderPage(browser)
        order_page.fill_order_data(order)
        assert order_page.is_order_success()
