from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import allure

import locators.main_page_locators as MP
from data.urls import Url


class MainPage:
    # url = 'https://qa-scooter.praktikum-services.ru/'

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть стартовую страницу")
    def open(self):
        self.driver.get(Url.MAIN_PAGE_URL)

    @allure.step("Нажать кнопку создания заказа")
    def order_button_click(self, button):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(button))
        self.driver.find_element(*button).click()

    @allure.step("Перейти на страницу оформления заказа")
    def order_top_button_click(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(MP.order_top_button))
        self.driver.find_element(*MP.order_top_button).click()

    def order_bottom_button_click(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(MP.order_bottom_button))
        self.driver.find_element(*MP.order_bottom_button).click()

    @allure.step("Нажать на вопрос")
    def question_click(self,question):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(question["question_locator"]))
        self.driver.find_element(*question["question_locator"]).click()

    def accept_cookie_click(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(MP.accept_cookie))
        self.driver.find_element(*MP.accept_cookie).click()

    @allure.step("Проверить, что ответ виден и корректен")
    def answer_is_visible_and_correct(self,question):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(question["answer_locator"]))

        answer = self.driver.find_element(*question["answer_locator"])
        answer_is_displayed = answer.is_displayed()
        answer_is_correct = (answer.text == question["answer"])
        return answer_is_displayed and answer_is_correct
    
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Проверить, что открыта стартовая страница")
    def is_start_page_open(self):
        return self.driver.current_url == Url.MAIN_PAGE_URL
    

    @allure.step("Нажать на логотип Самоката")
    def scooter_logo_click(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(MP.scooter_logo))
        self.driver.find_element(*MP.scooter_logo).click()

    @allure.step("Нажать на логотип Яндекс")
    def yandex_logo_click(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(MP.yandex_logo))
        self.driver.find_element(*MP.yandex_logo).click()

    @allure.step("Проверить, что открылась страница Дзен")
    def is_dzen_page(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))
        return self.get_current_url() == 'https://dzen.ru/?yredirect=true'

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
