from selenium.webdriver.common.by import By
import locators.main_page_locators as MP


class Questions:

    questions = [
        {
            "question": "Сколько это стоит? И как оплатить?",
            "answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
            "question_locator": [By.XPATH, '//div[contains(text(),"Сколько это стоит")]'],
            "answer_locator": [By.XPATH, '//p[contains(text(),"400 рублей")]']

        },
        {
            "question": "Хочу сразу несколько самокатов! Так можно?",
            "answer": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто "
                    "сделать несколько заказов — один за другим.",
            "question_locator": [By.XPATH, '//div[contains(text(),"несколько самокатов")]'],
            "answer_locator": [By.XPATH, '//p[contains(text(),"заказ — один")]']
        },
        {
            "question": "Как рассчитывается время аренды?",
            "answer": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени "
                    "аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в "
                    "20:30, суточная аренда закончится 9 мая в 20:30.",
            "question_locator": [By.XPATH, '//div[contains(text(),"время аренды?")]'],
            "answer_locator": [By.XPATH, '//p[contains(text(),"Отсчёт времени")]']
        },
        {
            "question": "Можно ли заказать самокат прямо на сегодня?",
            "answer": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
            "question_locator": [By.XPATH, '//div[contains(text(),"прямо на сегодня?")]'],
            "answer_locator": [By.XPATH, '//p[contains(text(),"станем расторопнее.")]']
        },
        {
            "question": "Можно ли продлить заказ или вернуть самокат раньше?",
            "answer": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
            "question_locator": [By.XPATH, '//div[contains(text(),"самокат раньше?")]'],
            "answer_locator": [By.XPATH, '//p[contains(text(),"1010.")]']
        },
        {
            "question": "Вы привозите зарядку вместе с самокатом?",
            "answer": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете "
                    "кататься без передышек и во сне. Зарядка не понадобится.",
            "question_locator": [By.XPATH, '//div[contains(text(),"привозите зарядку")]'],
            "answer_locator": [By.XPATH, '//p[contains(text(),"полной зарядкой")]']
        },
        {
            "question": "Можно ли отменить заказ?",
            "answer": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
            "question_locator": [By.XPATH, '//div[contains(text(),"отменить заказ?")]'],
            "answer_locator": [By.XPATH, '//p[contains(text(),"Штрафа не будет")]']
        },
        {
            "question": "Я жизу за МКАДом, привезёте?",
            "answer": "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
            "question_locator": [By.XPATH, '//div[contains(text(),"за МКАДом")]'],
            "answer_locator": [By.XPATH, '//p[contains(text(),"Всем самокатов!")]']
        }
    ]


class Orders:
    first_order = {
        'name': 'Летун',
        'surname': 'Бесстрашный',
        'address': 'Тот свет',
        'metro': 'Черкизовская',
        'phone': '84955550123',
        'delivery_date': '31.10.2025',
        'rent_time': 'трое суток',
        'color': 'черный',
        'comment': 'Пешеходы достали мешаться',
        'button': MP.order_top_button
    }

    second_order = {
        'name': 'Мяо',
        'surname': 'Ван',
        'address': 'Пекин',
        'metro': 'Динамо',
        'phone': '84955550124',
        'delivery_date': '30.10.2025',
        'rent_time': 'двое суток',
        'color': 'серый',
        'comment': 'Миска риса Мяо счастливый',
        'button': MP.order_bottom_button
    }

    orders = [first_order, second_order]
