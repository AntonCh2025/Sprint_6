from selenium.webdriver.common.by import By

order_bottom_button = [By.XPATH, '//div[contains(@class,"Home_RoadMap")]/descendant::button']
accept_cookie = [By.XPATH, '//button[contains(@class,"CookieButton")]']

question1_locator = [By.XPATH, '//div[contains(text(),"Сколько это стоит")]']
answer1_locator = [By.XPATH, '//p[contains(text(),"400 рублей")]']

question2_locator = [By.XPATH, '//div[contains(text(),"несколько самокатов")]']
answer2_locator = [By.XPATH, '//p[contains(text(),"заказ — один")]']

question3_locator = [By.XPATH, '//div[contains(text(),"время аренды?")]']
answer3_locator = [By.XPATH, '//p[contains(text(),"Отсчёт времени")]']

question4_locator = [By.XPATH, '//div[contains(text(),"прямо на сегодня?")]']
answer4_locator = [By.XPATH, '//p[contains(text(),"станем расторопнее.")]']

question5_locator = [By.XPATH, '//div[contains(text(),"самокат раньше?")]']
answer5_locator = [By.XPATH, '//p[contains(text(),"1010.")]']

question6_locator = [By.XPATH, '//div[contains(text(),"привозите зарядку")]']
answer6_locator = [By.XPATH, '//p[contains(text(),"полной зарядкой")]']

question7_locator = [By.XPATH, '//div[contains(text(),"отменить заказ?")]']
answer7_locator = [By.XPATH, '//p[contains(text(),"Штрафа не будет")]']

question8_locator = [By.XPATH, '//div[contains(text(),"за МКАДом")]']
answer8_locator = [By.XPATH, '//p[contains(text(),"Всем самокатов!")]']
