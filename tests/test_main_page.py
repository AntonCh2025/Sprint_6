from selenium import webdriver
import pytest
import allure
from pages.main_page import MainPage
from data.data import Questions


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверка ответов на вопросы")
    @pytest.mark.parametrize('question', Questions.questions)
    def test_question_answer_correct(self, question):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.question_click(question)
        assert main_page.answer_is_visible_and_correct(question)
    
    @allure.title("Проверка открытия Дзена при клике на логотип Яндекса")
    def test_yandex_logo_click_dzen_opened(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.yandex_logo_click()
        main_page.switch_to_new_tab()
        assert main_page.is_dzen_page()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        