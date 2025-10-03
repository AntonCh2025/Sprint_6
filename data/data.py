import locators.main_page_locators as MP
import locators.base_page_locators as BP


class Questions:

    questions = [
        {
            "question": "Сколько это стоит? И как оплатить?",
            "answer": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
            "question_locator": MP.question1_locator,
            "answer_locator": MP.answer1_locator
        },
        {
            "question": "Хочу сразу несколько самокатов! Так можно?",
            "answer": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто "
                    "сделать несколько заказов — один за другим.",
            "question_locator": MP.question2_locator,
            "answer_locator": MP.answer2_locator
        },
        {
            "question": "Как рассчитывается время аренды?",
            "answer": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени "
                    "аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в "
                    "20:30, суточная аренда закончится 9 мая в 20:30.",
            "question_locator": MP.question3_locator,
            "answer_locator": MP.answer3_locator
        },
        {
            "question": "Можно ли заказать самокат прямо на сегодня?",
            "answer": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
            "question_locator": MP.question4_locator,
            "answer_locator": MP.answer4_locator
        },
        {
            "question": "Можно ли продлить заказ или вернуть самокат раньше?",
            "answer": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
            "question_locator": MP.question5_locator,
            "answer_locator": MP.answer5_locator
        },
        {
            "question": "Вы привозите зарядку вместе с самокатом?",
            "answer": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете "
                    "кататься без передышек и во сне. Зарядка не понадобится.",
            "question_locator": MP.question6_locator,
            "answer_locator": MP.answer6_locator
        },
        {
            "question": "Можно ли отменить заказ?",
            "answer": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
            "question_locator": MP.question7_locator,
            "answer_locator": MP.answer7_locator
        },
        {
            "question": "Я жизу за МКАДом, привезёте?",
            "answer": "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
            "question_locator": MP.question8_locator,
            "answer_locator": MP.answer8_locator
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
        'button': BP.order_top_button
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
