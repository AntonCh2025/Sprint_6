from selenium.webdriver.common.by import By


class LocatorMaker:

    def metro_station(station):
        return [By.XPATH, f'//div[@class="select-search__select"]/descendant::*[text()="{station}"]']

    def time_option(option):
        return [By.XPATH, f'//div[@class="Dropdown-menu"]/descendant::*[text()="{option}"]']
