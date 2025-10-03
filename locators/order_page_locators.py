from selenium.webdriver.common.by import By

# Для кого самокат
name = [By.XPATH,'//*[@placeholder="* Имя"]']
surname = [By.XPATH,'//*[@placeholder="* Фамилия"]']
address = [By.XPATH,'//*[contains(@placeholder, "Адрес")]']
metro_station = [By.XPATH,'//*[contains(@placeholder, "метро")]']
telephone = [By.XPATH,'//*[contains(@placeholder, "Телефон")]']
next_button = [By.XPATH,'//button[text()="Далее"]']

#Про аренду
deliver_date = [By.XPATH, '//*[contains(@placeholder, "Когда")]']
rent_time = [By.XPATH, '//*[contains(text(), "Срок аренды")]']
color_black = [By.XPATH, '//*[@id="black"]']
color_gray = [By.XPATH, '//*[@id="grey"]']
comment = [By.XPATH, '//*[contains(@placeholder, "Комментарий")]']
back_button = [By.XPATH, '//button[text()="Назад"]']
rent_button = [By.XPATH, '//div[contains(@class,"Order_Buttons")]/button[text()="Заказать"]']

#Подтверждение
yes_button = [By.XPATH, '//div[contains(@class,"Order_Buttons")]/button[text()="Да"]']
no_button = [By.XPATH, '//button[text()="Нет"]']

#Заказ оформлен
form_success = [By.XPATH, '//div[contains(text(),"Заказ оформлен")]']
show_status_button = [By.XPATH, '//button[contains(text(),"статус")]']
