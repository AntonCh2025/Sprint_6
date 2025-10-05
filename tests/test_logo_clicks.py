from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.urls import Url

import pytest
import allure

class TestLogoClicks:

    @allure.title("Проверка открытия главной страницы при нажатии на логотип Самоката")
    def test_scooter_logo_click_main_page_opened(self, browser):
        order_page = OrderPage(browser)
        order_page.open()
        order_page.scooter_logo_click()
        assert order_page.current_url_matches_main_page()

    @allure.title("Проверка открытия страницы Дзена при нажатии на логотип Яндекса")
    def test_yandex_logo_click_dzen_opened(self,browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.yandex_logo_click()
        main_page.switch_to_new_tab()
        assert main_page.current_url_matches_dzen()
