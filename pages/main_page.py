import locators.main_page_locators as MP
import locators.base_page_locators as BP
from data.urls import Url
from pages.base_page import BasePage

import allure

class MainPage(BasePage):

    @allure.step("Открыть стартовую страницу")
    def open(self):
        self.open_url(Url.MAIN_PAGE_URL)

    @allure.step("Нажать кнопку создания заказа")
    def order_button_click(self, button):
        self.element_click(button)

    @allure.step("Перейти на страницу оформления заказа")
    def order_top_button_click(self):
        self.element_click(BP.order_top_button)

    def order_bottom_button_click(self):
        self.element_click(MP.order_bottom_button)

    @allure.step("Нажать на вопрос")
    def question_click(self,question):
        self.scroll_to_page_bottom()
        self.element_click(question["question_locator"])

    def accept_cookie_click(self):
        self.element_click(MP.accept_cookie)

    @allure.step("Проверить, что ответ виден и корректен")
    def answer_is_visible_and_correct(self,question):
        answer_is_displayed = self.element_is_displayed(question["answer_locator"])
        answer_is_correct = self.element_text_matches(question["answer_locator"], question["answer"])
        return answer_is_displayed and answer_is_correct
    
    @allure.step("Проверить, что открыта стартовая страница")
    def is_start_page_open(self):
        return self.get_current_url() == Url.MAIN_PAGE_URL    

    @allure.step("Нажать на логотип Самоката")
    def scooter_logo_click(self):
        self.element_click(BP.scooter_logo)

    @allure.step("Нажать на логотип Яндекс")
    def yandex_logo_click(self):
        self.element_click(BP.yandex_logo)
