from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data.urls import Url
import locators.base_page_locators as BP
import allure

class BasePage:

    def __init__(self,driver):
        self.driver = driver
    
    def element_click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def fill_input(self, locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).send_keys(text)

    def scroll_to_page_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_element_text(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text
    
    def element_is_displayed(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).is_displayed()
    
    def element_text_matches(self, locator, text):
        return self.get_element_text(locator) == text
    
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    @allure.step("Проверить, что открылась страница Дзен")
    def current_url_matches_dzen(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(Url.DZEN_PAGE_URL))
        return self.driver.current_url == Url.DZEN_PAGE_URL

    @allure.step("Нажать на логотип Яндекс")
    def yandex_logo_click(self):
        self.element_click(BP.yandex_logo)

    @allure.step("Нажать на логотипа Самоката")
    def scooter_logo_click(self):
        self.element_click(BP.scooter_logo)

    @allure.step("Проверить, что открылась главная страница Самоката")
    def current_url_matches_main_page(self):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(Url.MAIN_PAGE_URL))
        return self.driver.current_url == Url.MAIN_PAGE_URL
