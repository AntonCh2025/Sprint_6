from selenium import webdriver
import pytest
import allure
from pages.main_page import MainPage
from data.data import Questions


class TestMainPage:

    @allure.title("Проверка ответов на вопросы")
    @pytest.mark.parametrize('question', Questions.questions)
    def test_question_answer_correct(self, question, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.question_click(question)
        assert main_page.answer_is_visible_and_correct(question)
           