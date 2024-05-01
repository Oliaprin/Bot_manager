import telebot
from telebot import types
# Создаем словарь для хранения данных сессии
session_data = {}
session_data2 = {}
session_data3 = {}
# Указываем токен вашего бота
bot = telebot.TeleBot('7097889503:AAFANG8pKNaIJwVjAhx8meo7ippvSBL51PU')

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Товар")
    item2 = types.KeyboardButton("Услуга")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Привет! Я бот менеджер по подбору товаров и услуг. "
                                      "Давай начнем с небольшого опроса. Что вы ищете?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Товар')
def handle_product(message):
    ask_category(message)

@bot.message_handler(func=lambda message: message.text == 'Услуга')
def handle_service(message):
    ask_service(message)
def ask_service(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Грузоперевозки")
    item2 = types.KeyboardButton("Строительство")
    item3 = types.KeyboardButton("Деловые")
    item4 = types.KeyboardButton("Фото и видеосъемка")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "Хорошо, какой категории услугу вы ищете?", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['Грузоперевозки', 'Строительство', 'Деловые', 'Фото и видеосъемка'])
def handle_service_choice(message):
    # Сохраняем выбранную категорию в словаре session_data
    session_data[message.chat.id] = {'categoryr': message.text}
    ask_price_ranger(message)
def ask_price_ranger(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item2 = types.KeyboardButton("500-5000")
    item4 = types.KeyboardButton("5000-100000")
    markup.add( item2, item4)
    bot.send_message(message.chat.id, "В каком ценовом диапазоне вы ищете услугу?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ['500-5000', '5000-100000'])
def handle_price_ranger(message):
    # Получаем значение категории из словаря session_data
    if message.chat.id in session_data:
        categoryr = session_data[message.chat.id]['categoryr']
        price_ranger = message.text
        bot.send_message(message.chat.id, "Вот товар, который подходит под ваши параметры.")
        bot.send_message(message.chat.id, "Выберите услугу здесь:", reply_markup=generate_inline_markup1(categoryr, price_ranger))
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так. Пожалуйста, начните сначала.")
def generate_inline_markup1(categoryr, price_ranger):
    if categoryr == "Грузоперевозки":
        if price_ranger == "500-5000":
            url = "https://www.avito.ru/kaliningrad/predlozheniya_uslug/gruzoperevozki_do_35t._gruzchiki._pereezdy_3391711859"
        elif price_ranger == "5000-100000":
            url ="https://www.avito.ru/kaliningrad/predlozheniya_uslug/shalanda_dlinnomer_gruzoperevozki_3865556761"
    elif categoryr == "Строительство":
        if price_ranger == "500-5000":
            url = "https://www.avito.ru/kaliningrad/predlozheniya_uslug/drenazhlivnevkakanalizatsiya_vodoprovod_2048019844"
        elif price_ranger == "5000-100000":
            url ="https://www.avito.ru/kaliningrad/predlozheniya_uslug/stroitelstvo_domov_pod_klyuch_2385828885"
    elif categoryr == "Деловые":
        if price_ranger == "500-5000":
            url = "https://www.avito.ru/kaliningrad/predlozheniya_uslug/avariynyy_komissar_3741502676"
        elif price_ranger == "5000-100000":
            url ="https://www.avito.ru/kaliningrad/predlozheniya_uslug/bankrotstvo_g.kaliningrad_2664697381"
    elif categoryr == "Фото и видеосъемка":
        if price_ranger == "500-5000":
            url = "https://www.avito.ru/kaliningrad/predlozheniya_uslug/fotograf_2617233860"
        elif price_ranger == "5000-100000":
            url ="https://www.avito.ru/kaliningrad/predlozheniya_uslug/svadebnyy_fotograf_2783841522"
    markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Выбрать", url=url)
    markup.add(url_button)
    return markup

def ask_category(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Электроника")
    item2 = types.KeyboardButton("Дом и сад")
    item3 = types.KeyboardButton("Детские товары")
    item4 = types.KeyboardButton("Одежда,обувь и аксессуары")
    item5 = types.KeyboardButton("Аптека")
    item6 = types.KeyboardButton("Книги")
    item7 = types.KeyboardButton("Продукты питания")
    item9 = types.KeyboardButton("Мебель")
    item11 = types.KeyboardButton("Канцелярские товары")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item9, item11)
    bot.send_message(message.chat.id, "Хорошо, какой категории товар вы ищете?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Канцелярские товары')
def handle_Stationery(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рюкзаки, ранцы, сумки")
    item2 = types.KeyboardButton("Тетради, дневники, блокноты")
    item3 = types.KeyboardButton("Письменные принадлежности")
    item4 = types.KeyboardButton("Концелярские принадлежности")
    item5 = types.KeyboardButton("Творчество в школе")
    item6 = types.KeyboardButton("Рабочее место")
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, "Выберите тип товара:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)
@bot.message_handler(func=lambda message: message.text in ['Рюкзаки, ранцы, сумки', 'Тетради, дневники, блокноты', 'Письменные принадлежности', 'Концелярские принадлежности', 'Творчество в школе','Рабочее место'])
def handle_Stationery_type(message):
    # Сохраняем выбранную категорию в словаре session_data
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

@bot.message_handler(func=lambda message: message.text == 'Мебель')
def handle_furniture(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Мебель для хранения")
    item2 = types.KeyboardButton("Столы и сутлья")
    item3 = types.KeyboardButton("Мебель дял спальни")
    item4 = types.KeyboardButton("Мягкая мебель")
    item5 = types.KeyboardButton("Компьютерная мебель")
    item6 = types.KeyboardButton("Мебель для ванной")
    item7 = types.KeyboardButton("Мебель для кухни")
    item8 = types.KeyboardButton("Мебель для бизнеса")
    item9 = types.KeyboardButton("Садовая мебель")
    item10 = types.KeyboardButton("Детская мебель")
    item11 = types.KeyboardButton("Бескаркасная мебель")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11 )
    bot.send_message(message.chat.id, "Выберите тип товара:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)
@bot.message_handler(func=lambda message: message.text in ['Мебель для хранения', 'Столы и сутлья', 'Мебель дял спальни', 'Мягкая мебель', 'Компьютерная мебель','Мебель для ванной','Мебель для кухни' ,'Мебель дял бизнеса' ,'Садовая мебель' ,'Детская мебель' ,'Бескаркасная мебель'])
def handle_furniture_type(message):
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

@bot.message_handler(func=lambda message: message.text == 'Продукты питания')
def handle_products(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Макароны, крупы")
    item2 = types.KeyboardButton("Чай, кофе, какао")
    item3 = types.KeyboardButton("Выпечка и сладости")
    item4 = types.KeyboardButton("Соки, воды, напитки")
    item5 = types.KeyboardButton("Орехи, снеки")
    markup.add(item1, item2, item3, item4, item5 )
    bot.send_message(message.chat.id, "Выберите тип товара:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)
@bot.message_handler(func=lambda message: message.text in [ 'Макароны, крупы', 'Чай, кофе, какао', 'Выпечка и сладости', 'Соки, воды, напитки','Орехи, снеки'])
def handle_products_type(message):
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

@bot.message_handler(func=lambda message: message.text == 'Книги')
def handle_book(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Электронные книги")
    item2 = types.KeyboardButton("Художественная литература")
    item3 = types.KeyboardButton("Детям и родителям")
    item4 = types.KeyboardButton("Учебная литература")
    item5 = types.KeyboardButton("Букинистика")
    item6 = types.KeyboardButton("Научная литература")
    item7 = types.KeyboardButton("Саморазвитие")
    item8 = types.KeyboardButton("Психология")
    item9 = types.KeyboardButton("Исскуство и культура")
    item10 = types.KeyboardButton("Иностранная литература")
    item11 = types.KeyboardButton("Бизнес-литература")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)
    bot.send_message(message.chat.id, "Выберите тип товара:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)
@bot.message_handler(func=lambda message: message.text in ['Электронные книги', 'Художественная литература', 'Детям и родителям', 'Учебная литература', 'Букинистика','Научная литература','Саморазвитие' ,'Психология' ,'Исскуство и культура' ,'Иностранная литература' ,'Бизнес-литература'])
def handle_book_type(message):
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

@bot.message_handler(func=lambda message: message.text == 'Аптека')
def handle_pharmacy(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Лекарственные средства")
    item2 = types.KeyboardButton("Мед.техника")
    item3 = types.KeyboardButton("Сопртпит")
    item4 = types.KeyboardButton("Средство реабилитации")
    item5 = types.KeyboardButton("Оптика")
    item6 = types.KeyboardButton("Витамины")
    markup.add(item1, item2, item3, item4, item5, item6)
    bot.send_message(message.chat.id, "Выберите тип товара:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)
@bot.message_handler(func=lambda message: message.text in ['Лекарственные средства', 'Мед.техника', 'Сопртпит', 'Средство реабилитации', 'Оптика','Витамины'])
def handle_pharmacy_type(message):
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

@bot.message_handler(func=lambda message: message.text == 'Одежда,обувь и аксессуары')
def handle_clothes(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Худи")
    item2 = types.KeyboardButton("Куртки")
    item3 = types.KeyboardButton("Обувь")
    item4 = types.KeyboardButton("Нижнее белье")
    item5 = types.KeyboardButton("Футболки")
    item6 = types.KeyboardButton("Брюки")
    item7 = types.KeyboardButton("Часы")
    item8 = types.KeyboardButton("Джинсы")
    item9 = types.KeyboardButton("Головные уборы")
    item10 = types.KeyboardButton("Платья")
    item11 = types.KeyboardButton("Юбки")
    item12 = types.KeyboardButton("Рюкзаки")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12 )
    bot.send_message(message.chat.id, "Выберите тип товара:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)
@bot.message_handler(func=lambda message: message.text in ['Худи', 'Куртки', 'Обувь', 'Нижнее белье', 'Футболки','Брюки','Часы' ,'Джинсы' ,'Головные уборы' ,'Платья' ,'Юбки','Рюкзаки'])
def handle_clothes_type(message):
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

@bot.message_handler(func=lambda message: message.text == 'Детские товары')
def handle_Kids(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Игрушки и игры")
    item2 = types.KeyboardButton("Игры на улице")
    item3 = types.KeyboardButton("Детское творчество")
    item4 = types.KeyboardButton("Настольные игры")
    item5 = types.KeyboardButton("Для школы и обучения")
    item6 = types.KeyboardButton("Подгузники и гигиена")
    item7 = types.KeyboardButton("Детское питание")
    item8 = types.KeyboardButton("Коляски и автокресла")
    item9 = types.KeyboardButton("Детская команата")
    item10 = types.KeyboardButton("Товары для мам")
    item11 = types.KeyboardButton("Товары для кормления")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11 )
    bot.send_message(message.chat.id, "Выберите тип товара:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)
@bot.message_handler(func=lambda message: message.text in ['Игрушки и игры', 'Игры на улице', 'Детское творчество', 'Настольные игры', 'Для школы и обучения','Подгузники и гигиена','Детское питание' ,'Коляски и автокресла' ,'Детская команата' ,'Товары для мам' ,'Товары для кормления'])
def handle_kids_type(message):
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

@bot.message_handler(func=lambda message: message.text == 'Дом и сад')
def handle_home(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Посуда")
    item2 = types.KeyboardButton("Текстиль")
    item3 = types.KeyboardButton("Декор и интерьер")
    item4 = types.KeyboardButton("Хозяйственные товары")
    item5 = types.KeyboardButton("Хранения вещей")
    item6 = types.KeyboardButton("Аксессуары для ванной")
    item7 = types.KeyboardButton("Дача и сад")
    item8 = types.KeyboardButton("Цветы и растения")
    item9 = types.KeyboardButton("Товары для праздника")
    item10 = types.KeyboardButton("Товары для бани")
    item11 = types.KeyboardButton("Освещение")
    item12 = types.KeyboardButton("Религия и эзоторика")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12 )
    bot.send_message(message.chat.id, "Выберите тип товара:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)

@bot.message_handler(func=lambda message: message.text in ['Посуда', 'Текстиль', 'Декор и интерьер', 'Хозяйственные товары', 'Хранения вещей','Аксессуары для ванной','Дача и сад' ,'Цветы и растения' ,'Товары для праздника' ,'Товары для бани' ,'Освещение','Религия и эзоторика'])
def handle_home_type(message):
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

@bot.message_handler(func=lambda message: message.text == 'Электроника')
def handle_electronics(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Телефоны")
    item2 = types.KeyboardButton("Планшеты")
    item3 = types.KeyboardButton("Ноутбуки")
    item4 = types.KeyboardButton("Телевизоры")
    item5 = types.KeyboardButton("Компьютеры")
    item6 = types.KeyboardButton("Смарт-часы")
    item7 = types.KeyboardButton("Аксессуары для смартфонов")
    item8 = types.KeyboardButton("Наушники")
    item9 = types.KeyboardButton("Фото/Видеокамеры")
    item10 = types.KeyboardButton("Игры и консоли")
    item11 = types.KeyboardButton("Умный дом")
    item12 = types.KeyboardButton("Офисная техника")
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12 )
    bot.send_message(message.chat.id, "Выберите тип электроники:", reply_markup=markup)
    session_data2[message.chat.id] = {'category': message.text}
    print(session_data2)
@bot.message_handler(func=lambda message: message.text in ['Телефоны', 'Планшеты', 'Ноутбуки', 'Телевизоры', 'Компьютеры','Смарт-часы','Аксессуары для смартфонов' ,'Наушники' ,'Фото/Видеокамеры' ,'Игры и консоли' ,'Офисная техника','Умный дом'])
def handle_electronics_type(message):
    session_data3[message.chat.id] = {'product_name': message.text}
    print(session_data3)
    ask_price_range(message)

def ask_price_range(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("100-500")
    item2 = types.KeyboardButton("500-1000")
    item3 = types.KeyboardButton("1000-5000")
    item4 = types.KeyboardButton("5000-10000")
    item5 = types.KeyboardButton("10000-100000")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, "В каком ценовом диапазоне вы ищете товар?", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ['100-500', '500-1000', '1000-5000','5000-10000','10000-100000'])
def handle_price_range(message):
    if message.chat.id in session_data2:
        category = session_data2[message.chat.id]['category']
        product_name = session_data3[message.chat.id]['product_name']
        price_range = message.text
        bot.send_message(message.chat.id, "Вот товар, который подходит под ваши параметры.")
        bot.send_message(message.chat.id, "Выберите товар здесь:", reply_markup=generate_inline_markup(category, product_name, price_range))
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так. Пожалуйста, начните сначала.")
def generate_inline_markup(category, product_name, price_range):
    if category == "Электроника":
        if product_name == "Телефоны":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/bunar-smartfon-zaryadnoe-ustroystvo-16-1-tb-bezhevyy-1561782149/?asb2=8-qooqanozKGvxvJCGG1U65DmS4XMkkgo7oKtwbi-dK7HY4c8OO0YeN20Q1rGLi4&avtc=1&avte=2&avts=1714415660"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/smartfon-watch-tpu-nano-screen-protector-3pcs-2-tb-prozrachnyy-1561755058/?asb2=BXGsx8rSJ-A9tNXDFKxufNvrHQNCZrVj6w5k3Hd3BGbmJd3BqjPTOvrtwNPXQEL4c6vogfQO3L7Q-yE-RFIySA&avtc=1&avte=2&avts=1714415691"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/bq-smartfon-1853-life-siniy-932787811/?asb2=Qt-jXhnYVh2cpB1SDYSj8QhBF43dMu2lbjnNfcI4r4SKcKAJeHjScJSORyxnus2Xpa3gaeqX6eVNrJ0vgsBZ4w&avtc=1&avte=4&avts=1714415733"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/smartfon-ofitsialnyy-flagmanskiy-magazin-9-pro-7-3-dyuymovyy-hd-ekran-1541165233/?asb2=O1bHwTdUI6lEfaYbX4v8cKkyiapqnXOrx1yIfxHlPk_wK1livMtXXOZ0CUys4Dlb&avtc=1&avte=2&avts=1714415996"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/smartfon-hot-300-ultimate-edition-s-7-3-dyuymovym-ekranom-setyu-5g-vysokokachestvennym-1550018489/?asb2=dUIqf3pqXrLwE0Hm4tdwQVfgdbdNY4ZpYTyhEqd7YeAupNUQpVHyNMX-A5zsxQryJdBBojuqJkEBhMMhK-jHrA&avtc=1&avte=2&avts=1714416042"

        elif product_name == "Планшеты":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/inleife-detskiy-planshet-detskiy-planshet-razvivayushchiy-igrushki-ot-3-let-poet-pesni-1560051067/?asb2=_t-eGuMaZxLdcAKYiOlOp3vPcVDLZqwJe0F8hZIFnfVeUWq3dr4BZUTOk5WxsCy0&avtc=1&avte=2&avts=1714416264"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/detskiy-planshet-26132300707-guang-v8t2l3-2gb-belyy-1552840842/?asb2=0l4nHL2JFx0-m4SUcvQqRK77Vw34sq5miCoPUoWSSPvqOUo2oeyT8Krha8Isi5rH&avtc=1&avte=2&avts=1714416298"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/planshet-klaviatura-s-kozhanoy-obivkoy-podderzhivayushchaya-diagonal-do-10-dyuyma-dlya-1342082866/?asb2=olG1aGBTcVViHgAuBU7CaBzXYaVurkNUwPaiVX0C1i9EcHZNQI2ph8Opo7Pky4yC&avtc=1&avte=2&avts=1714416339"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/wxlys-planshet-planshet-11-pro-12-9-16-1024gb-android-13-wifi-dve-sim-karty-sd-karta-1487883839/?asb2=8wfy8odJYm9Flaa3JNJwKl48OSCtirqp_cZScLUzkC8tA9aFKuWQpWFULUsKGnWY&avtc=1&avte=2&avts=1714416367"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/planshet-xioami-pro11-12-gb-512-gb-akkumulyator-10000-mach-10-1-dyuymovyy-bolshoy-ekran-android-12-1561506751/?asb2=hZdbly7zKiPl0iZphplgvpyhZ5i_FYhy5N7TvBpzrYE4k0YzfRLADrABi-aigfzCmvG5tD8Rr664FSxMzGfI1w&avtc=1&avte=2&avts=1714416385"
        elif product_name == "Ноутбуки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/ozon-1089728908-noutbuk-goluboy-1541969366/?asb2=kj-acbKPoQSnf_0569NHI-MhghNFVeeNHqvb_SbH6ObkiYsJvLUKYEyQTbNDeUBz&avtc=1&avte=2&avts=1714416415"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/izmenilsya-tsvet-podsvetki-usb-igrovoy-noutbuk-1543801726/?asb2=ealpWd9KbVuY3NXH2KcZHjc8O3pV4nwzx3YRZbHdxtlVobz84GXT6abzi8RxmC8Y&avtc=1&avte=2&avts=1714416440"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/a-756737031796-noutbuk-cherno-seryy-1509247147/?asb2=Zs3r8VpAIWTfjnE4nKDq-0kK-ur_Bw3JhSbsAZPnFcOw0Cz2g1gLaubXPL-0U8u6&avtc=1&avte=2&avts=1714416455"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/pb-x11cc11cc-noutbuk-12-4-ram-12-gb-512-gb-zolotoy-bezhevyy-russkaya-raskladka-1541297757/?asb2=6oa3zzNNjF6pX3E_A1lvlbV2dJaUhqJXncVn6jUG3Ad-u2P_tUBxjUEb_jCyFCvu&avtc=1&avte=2&avts=1714416473"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/n11-cp-noutbuk-14-intel-celeron-n3350-ram-4-gb-ssd-intel-hd-graphics-windows-pro-serebristyy-1549680969/?asb2=-gIhHCaFwcHOKetxa4Q2t6rHUokdXgzDC9X_X3Sph_vP87AitqrItQApAOQ0KpB_llyYp7e538XiUziUfawOpg&avtc=1&avte=2&avts=1714416494"
        elif product_name == "Телевизоры":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/vstraivaemyy-televizor-7-chernyy-matovyy-1411033778/?asb2=ByNL0Ru9Yec_frIG6bDVmvmgHYcZr-OG2eZUY3i1vhywcjYcH6OxHbP5CHnchA2n-KM9c6SBJkcITW56xCjXWa6ydNah0GFyZPMJrjEaiVQ&avtc=1&avte=2&avts=1714416554"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/vstraivaemyy-televizor-7-chernyy-matovyy-1411033778/?asb2=ByNL0Ru9Yec_frIG6bDVmvmgHYcZr-OG2eZUY3i1vhywcjYcH6OxHbP5CHnchA2n-KM9c6SBJkcITW56xCjXWa6ydNah0GFyZPMJrjEaiVQ&avtc=1&avte=2&avts=1714416554"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/vstraivaemyy-televizor-7-chernyy-matovyy-1411033778/?asb2=ByNL0Ru9Yec_frIG6bDVmvmgHYcZr-OG2eZUY3i1vhywcjYcH6OxHbP5CHnchA2n-KM9c6SBJkcITW56xCjXWa6ydNah0GFyZPMJrjEaiVQ&avtc=1&avte=2&avts=1714416554"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/byrkisd-televizor-17-chernyy-1056246042/?asb2=PCCaLvS30pszRuQWpR5UZVF9Yy1ATLuvEmMNE_HknIJiaqPOWsXG57PjZvEI3Jbq&avtc=1&avte=2&avts=1714416608"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/eplutus-televizor-19-hd-chernyy-1549600400/?asb2=iQZsdXV6APTtZgOEb7LAJX9aDgsAC6cA3bCtp70spOqRBS_-djXBBlbaiy4-tGT1E94iCh54dXNx9fKFesPuxw&avtc=1&avte=2&avts=1714416624"
        elif product_name == "Компьютеры":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/usb-flesh-nakopitel-m001-64-mb-1542947118/?asb2=diuNKDpmo7U7Y46GgstDtnJELxvnLR7HEqtcdG_dXKr59nQWqc1ogVDl4HvR6kcmk9Nzi_3wICxXZvnMXASkOg&avtc=1&avte=2&avts=1714416660"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/kovrik-dlya-myshi-gold-geometry-300h250h2-mm-chernyy-943217511/?asb2=TOGcPQr1b_9_-4nljHH5c_yEnxCoQle_lJb7-odRfZwN3wZKQ00XNb6b220gJNppDf0JxIvIwtDI0r0-SmVb5g&avtc=1&avte=2&avts=1714416692"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kabelnaya-sborka-5d-fb-n-female-fme-female-5-metrov-1279489481/?asb2=I_SKxxxnuf6ZLR4xwZRw61SD8-NokPRUIDLcgYep6V71uv8XIPXWydQqsQeAyjI7-eRIjzHL4sM4H-MqKo1mVQ&avtc=1&avte=2&avts=1714416714"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/naushniki-provodnye-igrovye-s-mikrofonom-dlya-pk-kompyutera-telefona-iphone-podarok-493787587/?asb2=nZf-qaXcjS3JwPZ-e92yrjsnX2gXXABZbqap1FMtohoV_196XbI31ydkRgjg2dy1374jZzqsfyb2QhTj2F1XOQ&avtc=1&avte=2&avts=1714416732"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/hp-sistemnyy-blok-nastolnyy-kompyuter-compaq-pro-6300-microtower-intel-pentium-g630-2-7-ggts-ram-1430349182/?asb2=Ac6rB9_ORc86v4adCajW8NjfWAs9A4Blfk3gIsnYm8_MCHrkUVAL7Yx-wkYJuy5Rg01xpeUoZZJ-idJCqo83Rw&avtc=1&avte=2&avts=1714416753"
        elif product_name == "Смарт-часы":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/umnye-chasy-2512220000711-huin-i4i9u7-1532415030/?asb2=ovaFGml0e-hWBwfhEam8ZEPdV0bgCZuzNtYbKJu11-hbCtO0NADywXGRxkfEQRCw&avtc=1&avte=2&avts=1714416789"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/umnye-chasy-y68-fitnes-braslet-d20-pro-561256723/?asb2=w3qxeQWtZtiex3HWzInzXax3YaZBpwrClH3EPKxmwT4jwz5kXBR9C5s4cmGBxggFtpvfZuiG1FBU99OokOs9PA&avtc=1&avte=2&avts=1714416806"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/cmart-chasy-naruchnye-fitnes-braslet-dlya-telefona-smartfona-sporta-sportivnye-umnye-478630082/?asb2=U-Er5A0zh9VrftY7zzFZPCPlk2DFtIxJYdgsAosV-wfsF27xPkLWyQWVEpx01ocJCs225Ks1aAc_yP65gLQI4w&avtc=1&avte=4&avts=1714416818"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/umnye-chasy-2024-ru-gt4-series-edition-2-remeshka-obnovlennaya-versiya-46mm-chernyy-1555904924/?asb2=w23LSNKN0iCTUQgkNxw0oFWkDiaOYLnVkwyDbVljOZlpk56gjWXBoYULLVUiGgR9&avtc=1&avte=2&avts=1714416837"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/amazfit-umnye-chasy-smart-chasy-detskie-muzhskie-zhenskie-naruchnye-umnye-chasy-dlya-detey-1269773413/?asb2=xwuxPcgfgA9vdtgwf1lEEKmXfYVSxQFEN74SVXbni26o_yQjEOPmju3TgbWmpdtJ&avtc=1&avte=2&avts=1714416851"
            elif product_name == "Аксессуары для смартфонов":
                if price_range == "100-500":
                    url = "https://www.ozon.ru/product/tonkiy-silikonovyy-chehol-dlya-telefona-samsung-galaxy-a71-prozrachnyy-chehol-nakladka-na-220763451/?asb2=LySJZt5K5jE_kaiDXPK5WDrknyPi9xcAj3NFI2EmwjWsbnHnI34SROytZJq1dL73_zzXSNOH4-JbjuFMb034rA&avtc=1&avte=2&avts=1714416955"
                elif price_range == "500-1000":
                    url = "https://www.ozon.ru/product/akkumulyatornaya-batareya-cameronsino-dlya-telefonov-blackberry-9220-9320-curve-220525236/?asb2=crJGH7nZytcCzpb4KZBp6uNc1Li-GjAvbCX8M_ZiRyg4po5QcSu2JZ8wZsKXdyOPwHdnkqi9iQhkNZ2PPDUuHA&avtc=1&avte=4&avts=1714416923"
                elif price_range == "1000-5000":
                    url = "https://www.ozon.ru/product/chehol-na-iphone-14-pro-max-s-karmanom-dlya-kart-i-koltsom-935551772/?asb2=-Syx-D6iaig1mkzxQxWrtpAKSsJ4EDKm783CFf32bYnBf5Cq9DsQPlO107EjYVtEKy5tt8HhJm9q0NnAv-FJJg&avtc=1&avte=2&avts=1714416993"
                elif price_range == "5000-10000":
                    url = "https://www.ozon.ru/product/kreplenie-n-star-x-grip-dlya-bolshih-smartfonov-prisoska-na-steklo-korotkaya-mufta-60-mm-938426865/?asb2=CHc8aXcJkoisoGtObFmU-L6ZAQsrQvgsi3zxhj7bXOmbfuBQOGUaCbOaNtVRMpvCJ9QlcLYQFtFJc5O9znJxZQ&avtc=1&avte=2&avts=1714417014"
                elif price_range == "10000-100000":
                    url = "https://www.ozon.ru/product/stabilizator-dlya-smartfonov-zhiyun-smooth-q4-stedikam-dlya-kamery-telefona-1313919577/?asb2=g3Ca54InrkTM--PQOnAr25LCX1AftnbTt7E8lCyvnxynTxMUCIt2-Fgr4dub_kqM-DicnucJEADJSbC1azIjjg&avtc=1&avte=4&avts=1714417088"
            elif product_name == "Наушники":
                if price_range == "100-500":
                    url = "https://www.ozon.ru/product/vo-vtoryh-pylezashchitnyy-kolpachok-srednetonalnogo-rupora-16mm-16mm-1533237521/?asb2=Y8QxUlZqBDKmO1EwGrIquJggcDe3yLrX11H1mXxuKUZSWX0hP3TCmU-6wlNLwZd5-13ttiPa029C4gCMEHr1bQ&avtc=1&avte=2&avts=1714417155"
                elif price_range == "500-1000":
                    url = "https://www.ozon.ru/product/1x-smennyy-kabel-dlya-100aap-100abn-s-mikrofonnym-kabelem-chernyy-1473521539/?asb2=yPYXgApwp_Fbv7CBvZCa9iNHIeRadpVzKOdd3eqKeCxIidefO26pYRptFm4Zqx6Hy2GL1aBf2s0PWve7zxB3ew&avtc=1&avte=2&avts=1714417201"
                elif price_range == "1000-5000":
                    url = "https://www.ozon.ru/product/vetrozashchita-dlya-petlichnogo-mikrofona-profi-2-2sht-1549414908/?asb2=vbAi3bXYuhKQPNx6eeNmxiT84OZzQPvQ6Xb7fw7jjaAA-WuaIgk9zdlJbrYBN9js_13q0HNTp2PCoycmtKBPsg&avtc=1&avte=2&avts=1714417216"
                elif price_range == "5000-10000":
                    url = "https://www.ozon.ru/product/naushniki-provodnye-igrovye-s-mikrofonom-dlya-pk-kompyutera-telefona-iphone-podarok-493787587/?asb2=aXyq_rXvnp1c4pbjnLpJjZ2xr0PreQ-Anl051yDjtm-bhWqyahR00iVlK034dA1pi9cZ1DENEC6I4zk8oRuV1A&avtc=1&avte=2&avts=1714417230"
                elif price_range == "10000-100000":
                    url = "https://www.ozon.ru/product/garnitura-epos-sennheiser-sc-635-dlya-kontaktnyh-tsentrov-nakladnye-provodnye-chernyy-1000642-1498613596/?asb2=jJOwNmRTf50T0hjjuHLPt8jccZi3oZnXlJOy3VEXPH3OzYFJAMo13koQWU6AgsQ3dheLKPDUxtSQ2c1YhRLPTg&avtc=1&avte=2&avts=1714417245"
            elif product_name == "Фото/Видеокамеры":
                if price_range == "100-500":
                    url = "https://www.ozon.ru/product/zashchitnaya-plenka-dlya-kamery-virbelite-matovaya-976826569/?asb2=KlcSpCtKXw_KDtYMcM_eRHw0YfeCwDok5IQXk2R2HlLs-qGjWZOktuDFZmZt0uwn&avtc=1&avte=2&avts=1714417271"
                elif price_range == "500-1000":
                    url = "https://www.ozon.ru/product/perehodnik-dofa-s-vintom-1-4-dlya-sjcam-i-xiaomi-yi-1561561757/?asb2=uJpbeukiaBiIkvH4Ple9OHWK7XYinHKcyW0UeG97m80LPY_8rHHmLvsToKvfKJ2DYYgeQCD5ax2ApejoZpsVcA&avtc=1&avte=2&avts=1714417284"
                elif price_range == "1000-5000":
                    url = "https://www.ozon.ru/product/akkumulyator-telesin-dlya-gopro-hero-5-6-7-8-1282998177/?asb2=U9vjj8VAJrI9F_ItMAtdD7-ahRdgIY1H3IWn33tdbnc-AZJ_ko7pnQHCz86aKtjDg_AK3WLhbjDRBmVq3TQIpQ&avtc=1&avte=2&avts=1714417300"
                elif price_range == "5000-10000":
                    url = "https://www.ozon.ru/product/fotoboks-dlya-predmetnoy-semki-i-manikyura-30-sm-s-led-podsvetkoy-6-tsvetov-fotofonov-1558879216/?asb2=paAyvAS_rJZ-wJ4znJvn0UsNpnVznY5GJNWMpfPxt35FLZWsKW31Y_eh1WrWjP2tZdqA-HyV-JipL5S4P-j7Zg&avtc=1&avte=2&avts=1714417317"
                elif price_range == "10000-100000":
                    url = "https://www.ozon.ru/product/vspyshka-yongnuo-yn565ex-iii-ttl-speedlite-dlya-canon-1417738107/?asb2=_lVI68XzwIJkZOU81SB1ClqB6ggybPvNJXZN1FipJ5shNMIbVL7thT_9dROeGvG_4DeOnChpiemAHaUIxpNU3w&avtc=1&avte=2&avts=1714417332"
            elif product_name == "Игры и консоли":
                if price_range == "100-500":
                    url = "https://www.ozon.ru/product/aksessuar-dlya-igrovoy-pristavki-igrovye-perchatki-s-kurinymi-paltsami-iz-uglerodnogo-volokna-1554859405/?asb2=lKlRj1jjkbSxykPlBOjW2iaovNKProdOnyM9yLb3RTJPrqmSYzkyV6vn9LenEPaB&avtc=1&avte=2&avts=1714417366"
                elif price_range == "500-1000":
                    url = "https://www.ozon.ru/product/kovrik-dlya-myshi-hellou-kitti-may-melodi-kuromi-igrovoy-80h30sm-bolshoy-kover-dlya-myshki-hello-1442917845/?asb2=ZjDzQjy29iE0bSMZ0pdopzNLUG_V5_oQjOqiyWHs_qmWF01yCbWng_yHYwhh4AedHsHaShdQnH5KU5EkXOnB4Q&avtc=1&avte=2&avts=1714417383"
                elif price_range == "1000-5000":
                    url = "https://www.ozon.ru/product/figurka-dota-2-baunti-hanter-dota-2-igrushka-bounty-hunter-1543501968/?asb2=ZANS2ds3PfOnZGEnVU7Z9ScA-p-rAWF8GiIBvCJpGawq7-dUAJIVADM6lFt1jWXD_m1gaFpLWyJs25Z7cCQxPw&avtc=1&avte=2&avts=1714417404"
                elif price_range == "5000-10000":
                    url = "https://www.ozon.ru/product/naushniki-provodnye-igrovye-s-mikrofonom-dlya-pk-kompyutera-telefona-iphone-podarok-493787587/?asb2=8rAq-lMVm2QNozuc59bllH16KpVtCTF_Z9naLKBUuqMB3KjJm5f5bsUba3GEhaFY4zgAiDj5FJe4clNacNcHPA&avtc=1&avte=2&avts=1714417426"
                elif price_range == "10000-100000":
                    url = "https://www.ozon.ru/product/korpus-1stplayer-steampunk-sp9-white-sp9-wh-1045595071/?asb2=c9FWlgywzUyKl0HBp4kWEbbnh04xrxBdyuhcdPtbon7piAtGmR9WnSb2uK5DbY63rJfmE6zeAw5dYsoZsGgPcw&avtc=1&avte=2&avts=1714417446"
            elif product_name == "Офисная техника":
                if price_range == "100-500":
                    url = "https://www.ozon.ru/product/kronshtey-potolochnyy-unv-tr-um06-e-in-1243054639/?asb2=Fq3tpjpC5dDmWwWyKHkYncVJ63MuXufJEVzjLMxSmZKSMxWaa3mtOsZLgpdF4yem&avtc=1&avte=2&avts=1714417491"
                elif price_range == "500-1000":
                    url = "https://www.ozon.ru/product/119rig208-zaglushka-g0401-1374615616/?asb2=HFE3BwsXEa3c0vlDD1yVuRSC9Ke21tGT5VeZsppg8d6yU_Cy3MuwrPHkCH1aoIaFeZ55BxKV31TwgeGKEtBgbw&avtc=1&avte=2&avts=1714417508"
                elif price_range == "1000-5000":
                    url = "https://www.ozon.ru/product/88001-0237-ustanovochnyy-krepezh-ats30-ats50-969553035/?asb2=30J6HncNV3VxASHePMLQJUrTbna8c1GTpZ7wLTkWB3jIHg3Lm4KxrduPynmjXiGfqhhk5Eyj0ZwZ_FnvlZD1pQ&avtc=1&avte=2&avts=1714417522"
                elif price_range == "5000-10000":
                    url = "https://www.ozon.ru/product/88001-0084-1-kozhuh-dvigatelya-bks-910248419/?asb2=k3lF_SQmITn56MVGkQDc__SV0fR1rrxQGzouEnw5L7k_4YIbPb0PJHftzL4U2yuw7mtpZDGjHUShklXd4dDLrQ&avtc=1&avte=2&avts=1714417535"
                elif price_range == "10000-100000":
                    url = "https://www.ozon.ru/product/ctv-im-hello-7-monitor-videodomofona-dlya-kvartiry-i-doma-chernyy-monitor-video-domofona-492508749/?asb2=YAw7dfGlQh1EbJbDyYWx_rAAapzvjtl-rWF75HEs0mB-8zIGcfmdFhWiGPhiNmHsw6QJs295JHbEkvdcSnA7rg&avtc=1&avte=2&avts=1714417552"
            elif product_name == "Умный дом":
                if price_range == "100-500":
                    url = "https://www.ozon.ru/product/bolt-shestigrannyy-m3-12-1280896809/?asb2=MxVTb18gmqaB-exU09e88Snm_J48MRrZZDPDE2lxWe6h6UH2d8r2Ni9NyeZ7qf-F&avtc=1&avte=2&avts=1714417593"
                elif price_range == "500-1000":
                    url = "https://www.ozon.ru/product/shkiv-zubchatyy-gt2-10-16-zubev-tridipro-634778191/?asb2=q1h2c3N9-RDxcfpTIXWPaH1QgkwXECCNc4vNP2yhrDrp6qEwSfA9LiaKnF0RIZ03fSrA4JHke2WfCaKq6Nn-Tg&avtc=1&avte=2&avts=1714417613"
                elif price_range == "1000-5000":
                    url = "https://www.ozon.ru/product/kartridzh-lazernyy-nv-print-nv-ce285a-dlya-hp-laserjet-p1102-p1102w-m1212nf-resurs-1600-str-1ed-1285958274/?asb2=W5qpqFpThSltWrnGDSrpxg9vFkAHlXXOl46aBQl87tpDfLWkOJY10751SQNMBnSdP8mB6yL_Ay4F8dM3T0K5qQ&avtc=1&avte=2&avts=1714417627"
                elif price_range == "5000-10000":
                    url = "https://www.ozon.ru/product/cactus-rashodnik-dlya-pechati-chernyy-black-1561331703/?asb2=eSZ-r7VesTc1U8bDkXxrZxbEXy-bdmCCrRIOPpdCjQDZLaZSVOMjsnW8Wi554bI3L_44eSzDXuA9wpJuBVQvIQ&avtc=1&avte=2&avts=1714417644"
                elif price_range == "10000-100000":
                    url = "https://www.ozon.ru/product/14-monitor-portativnyy-chernyy-utsenennyy-tovar-1481002043/?asb2=ga3tSF1XasHiwTHehozvr8kePt5N5vgydMtrHkAQSHOyI-6CPGQCP3oeX-ezLszUHCXPLxsmm36oYuTlkksb0w&avtc=1&avte=2&avts=1714417660"
    elif category == "Дом и сад":
        if product_name == "Посуда":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/grippery-ziplok-50x70-mm-40-mikron-100-shtuk-pakety-s-zamkom-zip-lock-prozrachnyy-dlya-zamorozki-845415177/?asb2=LyCYbMC8Tj4Tlu83ECqYvA4sqMLOKMnMRlCn-fWsEW6VlmA2L_7v0DzPe_464VdernlkTu5rBMpWIV07cjmQhg&avtc=1&avte=2&avts=1714417877"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/ogranichitel-hoda-abraziva-tsprof-6mm-s-pruzhinoy-erp-992986474/?asb2=jP3TtWmeCXIy3g1Nz1NpEu06KVAK4WQe74AeXPMY_iCdhNDVEYIfL3YHSwcrLl4g&avtc=1&avte=2&avts=1714417855"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kozha-dlya-polirovki-tsprof-na-blanke-469803065/?asb2=ap7656-06fQGYvuV81ecUu4MRrTzX0C4MjQtnc0NT7jlmMqUiQyAfnZAndwRvG6UDHuLHaYXeuWHgvhBWd9VTw&avtc=1&avte=2&avts=1714417897"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/vintazhnyy-podstakannik-latnyy-melhior-z-d-pluton-sssr-1970-e-1561559873/?asb2=0GgbLZrNGrRLolZSSYdd23qnAfrEBsCzfCV8JeOBke5O1VbZGa5sAiPb5vOzNMS_ZKnAG31oC5tXK5EgmRC-Og&avtc=1&avte=2&avts=1714417912"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/nabor-stolovoy-posudy-iz-25-predm-kolichestvo-person-6-1509995616/?asb2=lDggUQ3_EZTntHmL3vkq_wkYC9KK81unbuqcSE51hPQvctdRlhsz9Fgv8OropCV2mn2-RS_eXNnzHdHYAlZg9w&avtc=1&avte=2&avts=1714417930"
        elif product_name == "Текстиль":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/namatrasnik-nepromokaemyy-v-detskuyu-krovatku-stretch-jersy-60h120-sm-531778046/?advert=UrgGuXOaYsXqiN8Jp-xhPBz7VJz33LZIX4ukuch3foCl2ZckFP3_JgmsgMk-FL-CL7zUHby8mvvCyWuWxcfT-bQybVi0BzNSNjp65ONWGNuA2oG17Nw4rFKG3ZD_5SosfF0v0zG_ajvGH10dplvM2vEHMnuQdN-J4GBkrCikL2qDw_RlQO22Prqa7CdRyei2Cyksy-913jI56SEDvLQR1PlLkhCgeDX8wm-6I_Fzi-u3JztrPjZB497pVoE&avtc=1&avte=2&avts=1714417969"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/namatrasnik-160h200-nepromokaemyy-s-bortom-i-rezinkoy-po-krugu-nepromokaemaya-prostynya-752967971/?advert=z-I32NLSu4QE2uHod4Z1wl-uPmGlelse7UyCcbPh8wqFcuDVyqgqLWXu9k-4xrRYwm2JgmEz4X0faFkQyruwuYyLwKebI7daYdcs7R112at3ps3ZEIpVrfFMMO2JlZA0cPrAbUhCI2wjFrImeDJNbXAn-KbbMbO5ZE6ezSVofdppkQdg_UPcEXG__BXBD6D5inGxqduUT1oFknzZlBU_W-fdVCr9V_40JCdAJCDkm4dsF5K1hXMAW2eH0Wy-oq1AVU1S2L9Q&avtc=1&avte=2&avts=1714417985"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/namatrasnik-140h200-steganyy-s-bortom-bambuk-belyy-zashchitnyy-chehol-na-matras-topper-752967129/?advert=SbTE6JLRkHomciRoMDpMEwilwkoWMA62JMNDR1AOpd2l7G8NHAbfgV0AtD44V5wjkc3CKxa4Q12Bz7RT2abYocK3Md4-z-DYh34dtcm3OwrCFXuLF4KxatSwH5xn_oSNX4MbY8ZHL5HQVa6atCJeyVwhIWKkquXYj9OurY4ki0jIrGIhPzDC0J3Tnwe-El6oAXfh0J4-mitUE8qVLganvvK-FdnvpJji7kl-pVCOlppqDfxEQWSsEaz7SZdGwvf-7t2JLpEa&avtc=1&avte=2&avts=1714418016"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/infrakrasnoe-odeyalo-sauna-dlya-pohudeniya-s-effektom-obertyvaniya-s-dvumya-zonami-progreva-1341013502/?advert=IZLt-yK56KhhnnZY6lZ2LYoOJId_n32z2xqHelOUsl6jWAO1JB_nHvVv7x_4F-hWGZll33_-4B_WDjh5MVv-lEqR6mpjE1XZH0sM2WmRR3Q-ckcnN-zGi1U_xFZUl99Do2WViJWGQKSe0KwfnHtAd2oQS381F-lGHDw44aRJlvaeQFZX7UQJyfssHs9nE2BRvCrC1xA85yJPVIdx5L8JBTr8mKROb_xr9Nuqxq7-IqRYwIP_-dh312c&avtc=1&avte=2&avts=1714418033"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/postelnoe-bele-mariag-home-seryy-s-fioletovym-tensel-lyuks-300tc-evro-komplekt-pododeyalnik-200-220-259550128/?advert=s8wfJv31aNeAmMJ9i-VWIu_i6pZelnugdvmBm0IXqlG72NYKx6X_uJZfUFHU8IqRJeyvBAKE9Lh9dF8WugpgUOCibyM4YLcmNweH6dMIgONrEkztY9Q4iOAxxrAkmZJevX-iaNgp1fu5eDHRcVetujvJTTtraaBdSxFnyr5N26U9mf24o87cUqO2OEys9YPfOxp2grB8Bjg__bpCUYfM2nupruiZLlAnPz63ZniqwlEQa1Hk63y_uLh9&avtc=1&avte=2&avts=1714418052"
        elif product_name == "Декор и интерьер":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/poster-210h297mm-173017423/?asb2=OvBvcFDX0OHr8tHjHwrmsjZOB0UHScRU73dsxuwYBedKQLJpE1ZpkbrnsdV-cZ5DuPX9lKaqJUSAre2wEicWqg&avtc=1&avte=2&avts=1714418082"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/kartina-na-holste-art-ryzhaya-pushistaya-lisitsa-zhivotnye-22-32-sm-dlya-interera-v-komnatu-na-stenu-1544725018/?asb2=62QMRvO6jLwv_wZ2Y74ZSDRk8ouszw9CYaPtAa8VF9Op0qFA5sHD-ncSeDzkKmW5Fkolf47FMrHRGjWQxcdY4A&avtc=1&avte=2&avts=1714418100"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/anime-boks-genshin-impakt-yae-miko-podarochnyy-nabor-genshin-impact-1222740058/?asb2=Wmx4_Zgpafz3uOgToOPs-ssJrnkG1Nomwf1SFGNktRyR3eZZxQMKAnetXo6Kr5Bh8w8AFlLSIaAsdE3cBkYTTA&avtc=1&avte=2&avts=1714418115"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/tarelka-panno-tsvety-1561611880/?asb2=_1c_7fkcgEwTSe-p6Gqhc1rColmm-LxKtAOLxvhLu-OM_elFWaoMRp0UNKejH3EyOxPGJMtp2nciZi7-ISRRrA&avtc=1&avte=2&avts=1714418130"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/zhivopisnaya-interernaya-kartina-balerinki-holst-maslo-60-60sm-862813443/?asb2=mtQSh7HueFznBzudhy6YINQ1OPnVF17v7wyK4Y4S8ZJJx8PP_aW6gGeSPl5PF2Rlkf5NEs7OCsRPmQR3yUrJ-A&avtc=1&avte=2&avts=1714418145"
        elif product_name == "Хозяйственные товары":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/kryuchok-dlya-vannoy-2-kryuch-1525262861/?asb2=PE_VyVgLaKS4bVx-KTh0ol5Fq32rZuGocYDzU1CewMLN7KkTqpvIRxf0U9evpkO1PmTgJ7xFJ4ApCruyXihhcw&avtc=1&avte=2&avts=1714418177"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/perchatki-polietilenovye-odnorazovye-50-par-100-sht-v-individualnyh-paketah-kazhdaya-para-1171364087/?asb2=cmEZW8w3ivRzS1jyQNMdpaTSpa4LHTJ0Q3-xPlrRteHjV_iyY4J6V43P2lkgkAddU8wuvURc6FjD5NIZ-eVi9A&avtc=1&avte=2&avts=1714418377"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/derzhatel-dlya-vannoy-komnaty-1-sht-1543052466/?asb2=FZJ6QTXX98-FKSm83pegGiHtwJnC9iTOVyVsB1721S5Nmgu8I-6mHs0Xw12nXOs-dzdHPMZt5q6C-gUnchKL2g&avtc=1&avte=2&avts=1714418393"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/polka-dvuhyarusnaya-1162169065/?asb2=dFfAiJDYnTk6FOixNYTM43MEfuIYH1JLPWdww0_NFYOmdOEWudFmTlWU6HownqpTsuGYTQtBqP2lR20YYv6zNA&avtc=1&avte=2&avts=1714418407"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/polka-langberger-steklyannaya-pryamaya-40-sm-10951d-1392484393/?asb2=1JY9rzlPX35zwY7nM4UIA4upc79sbe_BcJGKRxno0TA7vc1l7n1rr2h_nnMaMwGZdtERc1-ULQHwOyotcVIY0w&avtc=1&avte=2&avts=1714418424"
        elif product_name == "Хранения вещей":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/mnogofunktsionalnyy-samokleyashchiysya-kryuchok-prochnyy-kryuchok-dlya-kuhni-vannoy-komnaty-net-1491573653/?asb2=K-2WbBOfiW9FcNTF7_le7wJl0oLyoO8QGMTNHnQvLzL8_pSnlv5IR84HuZCQC7XOdgRC1SVQUIdamC_3vKaDqg&avtc=1&avte=2&avts=1714418468"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/vakuumnyy-paket-dlya-hraneniya-veshchey-roza-60h80-sm-aromatizirovannyy-prozrachnyy-2-shtuki-984210372/?asb2=yoDdgzRRdgMthlivfO8ALiZSrvO4JuaMkdPo8l510GTKgqc3hqvJSYD79Ael9VTPPsRdkaVgNBmGQgUJyiX4dg&avtc=1&avte=2&avts=1714418488"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kofr-dlya-hraneniya-veshchey-sm-1534903024/?asb2=oXIl7rX4VIuoGcK4cdkO-ue8K3Ft523JE4HZXjbGe8ROh8MGbnwcOszBWd-bs2lHuBK8am4EdVpHaq0ZvOQBwA&avtc=1&avte=2&avts=1714418504"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/veshalka-kostyumnaya-iz-massiva-buka-na-kolesikah-mebelik-verona-lyuks-slonovaya-kost-948870176/?asb2=TIi7nz2piYOmYJdsoIDXNAY8qSKSUvMoGYoL4x-AVt9Bzn6n0FVkRbUp4Pe5SS0Nv-h0sTgMjqwCQUCos_jCJQ&avtc=1&avte=2&avts=1714418527"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/zip-pakety-50-h-70-sm-500-shtuk-kurerskiy-paket-zip-matovye-s-zastezhkoy-s-begunkom-839489035/?asb2=cTqxt6a22xyrlZk-AtNfsggP8lYfH3tzN4X4fFhoh3734FBVAgjjeflCnJA8GSgYHxo7JlRqfLshPB905iTbhw&avtc=1&avte=2&avts=1714418545"
        elif product_name == "Аксессуары для ванной":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/kryuchok-dlya-vannoy-4-pcs-kryuch-1562154627/?asb2=IOqaxATA0NXQpW8k5QBwuhdL-ih_zwJfiGyZauUw0FXSjS-LjU5Hk2c2S63y6yXHKX3nICw9UXyaq4CHinARyg&avtc=1&avte=2&avts=1714418616"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/dvoynaya-shtora-dlya-vannoy-komnaty-180-180-sm-poliester-peva-zanaveska-v-vannuyu-1073731811/?asb2=u6xtCpSkp0wmKxXGIyh3YgkRIutQy2N43fK2gZsToB2t5VcHjiIRRxd0SqLK9MZdKRg-1gwT9h5gMJUXGcNwKg&avtc=1&avte=2&avts=1714418633"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/derzhatel-dlya-vannoy-komnaty-1-sht-1543052466/?asb2=tQc__l29i3hLItmDkVO3wwMvT3okXIOzqMJzYbXJBjLEHTLGw9moOJBpX8jVbpD3lUYTeNS_fN1lpVJ4CVZyJg&avtc=1&avte=2&avts=1714418648"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/polka-dvuhyarusnaya-1162169065/?asb2=AGde1ndYRy3UO8w8mnFdyL_NrwBSSO2Zr_xSAraFxmwpwPuSDpRodRPg9GfTwVcxa2ztBxS66kQ4r-oOomTVGA&avtc=1&avte=2&avts=1714418662"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/polka-langberger-steklyannaya-pryamaya-40-sm-10951d-1392484393/?asb2=qgxc1i4t43q-M5SvA_rJKk3ItVXtuL6gE6SLhwxTMypmviFa0EyPEcYNvHAGv3exGPSXF9M43nA-jLX90MpRGw&avtc=1&avte=2&avts=1714418683"
        elif product_name == "Дача и сад":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/adapter-5305-gardena-05305-20-000-00-1555022936/?asb2=HxmkQleWrZ-GegpOwD40J0XXdN5_04BsvRy3fBuQaRU-OLGq6bpDWnupt48TBPY71CqeRd3cBnhIOtUF77bFvg&avtc=1&avte=2&avts=1714418717"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/vozduhoduvka-1441139089/?asb2=VUG8l7Mj0W12hTgFyCIyVMtOt_YWpDyB6bw0ngFCQEc-dbTS64fkkM_GjlWBYwxrlb66v1mgk7A-ilhbLqvCkQ&avtc=1&avte=2&avts=1714418732"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/nabor-podshipnikov-dlya-opornyh-rolikov-otkatnyh-vorot-6204-2rs-180204-8-sht-ntl-bearing-286948247/?asb2=Fwh_5jA-8Lern_6iBUO5u_aht6o0sOy2yQbcqsz4FkV1M03wq0_6T2XL_spvmR_5v7dgLjean-aHTpPPSrJaAA&avtc=1&avte=2&avts=1714418750"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/nabor-sadovyh-instrumentov-1545699632/?asb2=Rpibnz_TKi6x-t5IcZPtqF14qnTA0oPsO1cilb3HuoS0t4cd_WUxfjcmNzrxpjbzZt0TnbCuwufax0WthGxQoA&avtc=1&avte=2&avts=1714418795"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/umyvalnik-termmiks-s-evn-nerzhaveyushchaya-moyka-med-1079045026/?asb2=ypF_wIdscP6dCFWkxY6ALFMW5TTKn-mYeExCsQr0WTt6yQJ_9JXuyOW_eMlgQxdw5uXx9T3jGBOLOs1AT_Ml2Q&avtc=1&avte=2&avts=1714418811"
        elif product_name == "Цветы и растения":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/balmy-home-gorshok-dlya-tsvetov-7-sm-h-6-5-sm-100-l-1-sht-955834148/?asb2=gSu_QWhDh96uL3XNPqxJUEH0I0OTab_6EnkXizr424MtE5_WrI33L8EO450b_FHw&avtc=1&avte=2&avts=1714418875"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/kashpo-podvesnoe-15-sm-h-15-sm-1-sht-510996599/?asb2=42lZRBiSLcC1Gf2OjKIf8GQizKMWHkjKh5s0ES4Qvkj3uj7ZTaEXQlf0nKvVK095MwGDUPsL580qK04jjbVgEg&avtc=1&avte=2&avts=1714418904"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kashpo-ulichnoe-9h9sm-1532372905/?asb2=FuELphBGTU2AZ-mbmCWfybjWPCZUizo_BR-pw9V6VscnUE9bR6jxNpCh85hhZJe8&avtc=1&avte=2&avts=1714418934"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/orhideya-zhivaya-falenopsis-anna-beach-ot-son-ya-ne-tsvetushchie-podrostki-komnatnye-rasteniya-1219075432/?asb2=poQDk10UUwu7SFJWxhYu3X3vuQvYDPDb2fV3XmhbCCPo_axCFRTET8UzAmJ4Tffzda4qUOr6PrnPDPJAVYsyOA&avtc=1&avte=4&avts=1714418978"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/podstavka-dlya-tsvetov-i-kashpo-ilwi-int-w-pc-o-1-n-1-metall-891672508/?asb2=1zO5DhPNwZP_514xxQS9eRUh9t6204jZsi3YTYhCFifMj783iY0bgEYpC6BVjWDtf77epaXEk3dDonBioSg27A&avtc=1&avte=2&avts=1714418997"
        elif product_name == "Товары для праздника":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/vozdushnyy-shar-biryuzovyy-zayats-folgirovannyy-figura-80sm-prazdnichnyy-podarok-na-den-rozhdeniya-1228184575/?asb2=hXEQaX7FxcISc_Ixgo9kr5LgIZAv_mO7dOIq4o6b05Wrf6A_vEIpJKGqKaBvgUicAKpCREGmXxj-41_3MYhNKQ&avtc=1&avte=2&avts=1714419024"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/darite-schaste-paket-laminirovannyy-vertikalnyy-lyubvi-i-tepla-m-26h30h9-sm-2-shtuki-v-upakovke-1467810531/?asb2=g2qqdbTPdsMLG71iognH3bOWdVwadhIYp2F47nAZzXG_tFa8-MTpZIE7wy2yChV1tp1nF__h8UQJBX_8EURS0g&avtc=1&avte=2&avts=1714419041"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/svetyashchiysya-hellouinskiy-dvernoy-zvonok-1429572714/?asb2=gnRc8e5792EuwI-S96GVL51ZcXtF2B6aSUUq2lYGhq458O7-JskYy6sX7s-mhOv16cXK01Gmo7eZ8zckL8JBXw&avtc=1&avte=2&avts=1714419060"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/sverhsovremennye-maski-sayberpanka-dlya-muzhchin-i-zhenshchin-na-hellouin-i-parti-1545978000/?asb2=JdUKKChfQ0p8fCfmGY5YBbuJCp-UxwFPvvt-EsRs49HAxUEkYhmvQg-Uu2tYzKfxu46IR3pa8XQPGlcs_47PTg&avtc=1&avte=2&avts=1714419076"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/kostyum-karnavalnyy-1548258478/?asb2=tZBPzGrx3WkxSxoS1mGM_SBpQoeLOIJI3YsL8OI8SGvIZit43HveL7CFd3s0Wyev&avtc=1&avte=2&avts=1714419100"
        elif product_name == "Товары для бани":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/shapka-bannaya-zhenskaya-dlya-bani-i-sauny-bannyy-mir-koshka-voylok-belyy-858005615/?asb2=4zWGxPqRtHdfydexHO8qMntPvJlP37XX44YsGBr9Dd7v8ytRinF_1sDytyr0GuS8fyguUNBgX13s4dJKknsZZQ&avtc=1&avte=2&avts=1714419142"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/dobroparov-solyanoy-briket-kub-lipa-200-gramm-ex-2-shtuki-1394874455/?asb2=eYT-2tJjZC-ZLHpkNXVjqek2iDHRKHTXOElelw4bLjd1Mjt1wh8bDLif1QTljTIUY36aZruZmG5C183kG3U37g&avtc=1&avte=2&avts=1714419165"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/les-dzhut-nabor-dlya-bani-shapka-muzhskaya-zhenskaya-mochalka-rukavitsa-komplekt-dzhutovyy-1222005072/?asb2=8IODiTWSamglpW9jQ7Ku_qmQorJi74jZJbF_rZ9caeUyQC8HJBl_nL5-BpzNqA9KjAZenGDw5McgouXMyCjiOQ&avtc=1&avte=2&avts=1714419180"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/parogenerator-dlya-bochki-isparitel-dlya-sauny-i-bani-sr-1-kv-lj-1535253140/?asb2=SCAz5hljYqlN7qRCpC3t1hgnOkam2o29PiTM6j7h4-wKIBxxUgMFiumjqQw6iLSKXaPSCt0fO-qbpa8ywYslkA&avtc=1&avte=2&avts=1714419197"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/aromaterapevticheskiy-diffuzor-1434403901/?asb2=6RBoL1z-jSuNQOjP-2f1h_IaEfS-LQP_CahWwhFERotcG4uv6k-OeBp-AF2qJWaE&avtc=1&avte=2&avts=1714419211"
        elif product_name == "Освещение":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/feron-lampa-svetodiodnaya-led-6vt-e14-belyy-matovyy-shar-lb-1406-1536585484/?asb2=rOPKU8VXX1cAkf00tbYCCQNe6KxZ20GbIHU0xdNLT2CLdpc1bgGVKTTn83XpMIKk&avtc=1&avte=2&avts=1714419317"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/bra-crystal-lux-clt-017cw1r-bl-1154501401/?asb2=p-SOaq4zdjBXxVSOt6jsAvjmVgGmgCFIBdmtblqm7HKr7klivFwn-xncz6BjuYR8AMYL2xrMNWuD6QR5AZWA6g&avtc=1&avte=2&avts=1714419332"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/370388-spot-nt18-252-hrom-vstraivaemyy-svetilnik-gx5-3-50w-12v-damla-1544776747/?asb2=WMfRcFMpVQioTL36y30pdJRo1Lbsb_IotNC9vsGNsQtWBcfuJw7EgvjVQUn42X7IrNNZm4jRDj_995mKPwYPxg&avtc=1&avte=2&avts=1714419362"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/lyustra-potolochnaya-lumion-dallin-comfi-5639-6c-tsokol-patron-e14-6-40w-moshchnost-240-vt-220v-1525869373/?asb2=Ahp8IWZ4e-eRzk0jSLco5wYjacZeB3VrHGo5WCBq51y_C74ci04WFDexOCwrnFMCSdwEzjt2rBLQBxfbGLSP3A&avtc=1&avte=2&avts=1714419392"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/lyustra-potolochnaya-lumion-lara-ledio-6545-68cl-tsokol-patron-led-43w-moshchnost-43-vt-220v-1525868888/?asb2=tw7BuPYr3nivgLHIQMkCx2sRnpUaHNiy9xjWU5gs04WnLLvq_kOlV0mZ3O_OWLMDJDP2qSDF6qgz-yInvvkXdA&avtc=1&avte=2&avts=1714419490"
        elif product_name == "Религия и эзотерика":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/nabor-form-dlya-kulicha-domashnyaya-kuhnya-bumaga-d-9sm-4sht-1560890416/?asb2=MLpW8GRbpn3tfP36WqmW7XqFO26Gnap3eLSE0gflLilE2FFtaN5rwycByXwk_Wl2E_cmU2Y7AyneFcC9OA3TbQ&avtc=2&avte=1&avts=1714419538"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/nabor-pashalnyh-yaits-dekorirovannye-yaytsa-dekor-pashalnyy-6-sht-1518747976/?asb2=Q3PVG0Z-ui3AV-nhNg79S9cX5ljgq7E9G92fbPcPkQUBWx0YZLxDAdORT0qoMU7O&avtc=1&avte=2&avts=1714419553"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/pashalnyy-vertep-podvesnoy-kulon-ukrashenie-izyskannye-religioznye-zheleznye-1508363999/?asb2=hqOnuDjszx_nFiUdtegR7ilqLWJVpLUY1ASHF4fD3X8QvvJ_oVRA6Z45cCrIiJnz_hbTsJxUicTFX2G3geBGXg&avtc=1&avte=2&avts=1714419572"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/pashalnoe-ukrashenie-svetodiodnaya-girlyanda-dekor-pashalnyy-yaytsa-assorti-1-5-m-usb-rozetk-10-lamp-1537055183/?asb2=cY2-Z_ieVfH4pY7JzlqMq2myiLeJTx5x6GGpPODG_LlBkRtxiXekrOTF3BRQtPFUD5lSha6J-1jPLIj47Svtmg&avtc=1&avte=2&avts=1714419596"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/ikona-svyatoy-georgiy-pobedonosets-gal-12-064-ik-03-522317407/?asb2=R5al7AR_iNEZic4eQ6RWoSkyi0Hlqm6a3XVqTLwGndw4R-HZyHycKG6EgiZpoiOulKMc_a89TpW1Ljsj98fY-A&avtc=1&avte=2&avts=1714419644"
    elif category == "Детские товары":
        if product_name == "Игрушки и игры":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/squidopop-skvidopop-26-sm-igrushka-antistress-shchupaltsy-osminoga-prilipala-prisoska-igrushka-548640766/?asb2=1th_ewt-a5bW1WSL_UdSaci70qbhQUYZrWUUl8q3QZ9gelzM1bqmnEHT0uAHuVnJKtXetSJdGgcFAx5rQGbFqQ&avtc=1&avte=2&avts=1714429043"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/konstruktor-dlya-malchika-mashina-uaz-452-pozhar-v-bolnitse-gorod-masterov-121-detal-349451976/?asb2=xF7yT56R3M8_F31Z4Dlw7EA4mJJa58deNzEkMnGGZsf2IfftwQnSa36Ih9x_3BzAHDspRb4Ac6qzPvYAkSE0RQ&avtc=1&avte=2&avts=1714429064"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/razvivayushchiy-nabor-davay-uchitsya-i-igrat-po-metodike-montessori-1523325207/?asb2=50z6_cC6GK7E-KGDROaHfKmH80GFb8rBug7uiprAB_wE57_RySvLlDrCuhEBlk00bb0el03g9STNjWrkaU5w1w&avtc=1&avte=2&avts=1714429080"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/igrovoy-derevyannyy-nabor-umyvalnik-26-5-x-25-5-x-33-5-sm-1493172801/?asb2=9GmKAskUdFPuW4vQktywc9bhnfZ7zEO1RG0Z2SzYnVwSpGG2fZWYjUTUi8FaGyWekCG4JTrmgdlUAR64nzMhNw&avtc=1&avte=2&avts=1714429095"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/shopkins-nabor-igrushek-bolshoy-nabor-iz-ogranichennoy-serii-1501168603/?asb2=1D5ybrCWZiRQQ0U3G-DDY4QhOy1QoNDF19wYSU1WqEdBIyPUIBZBJf0CjUZ-kyL_&avtc=1&avte=2&avts=1714429112"
        elif product_name == "Игры на улице":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/ryra-myach-dlya-detey-1556814544/?asb2=JsON0NAfmx-HUYqkT0mBwJs7qlUe-MGfLf_CYCLyw51_EQ6yq62UzmQZYUlbrNixxfsKUKoQCzxBESarMtx65g&avtc=1&avte=2&avts=1714429139"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/formochki-polese-krab-2-morskaya-zvezda-2-rakushka-2-1054365493/?asb2=0wr2PjQ2M532n6kzLEvSxrOgzO7Lc39jZ5IP1Hh3r5iUJOdE9WmC2RLRjXHcVXwiPZYl_G_J-pYzm_vOxbhjnQ&avtc=1&avte=2&avts=1714429153"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/vodyanye-shariki-ot-7-do-8-mm-businy-bezopasnye-ekologicheski-chistye-gelevye-shariki-dlya-igrushki-1513182411/?asb2=vBxz1b7-R197hEn_TsdLHHpHskV8sCV11NFeOkfavMl-DNNdxqTD6bMvUI8bQzSL&avtc=1&avte=2&avts=1714429170"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/penni-bord-so-svetyashchimisya-kolesami-57-sm-zheltyy-1560886588/?asb2=hJWBPt3UWHQP9tddaJvTHni61BYH6PJ_TEKifop7b6gtIF8zqZjSrOBtlsrC4gc0PQgMut59nMMwBMMqQy2xBA&avtc=1&avte=2&avts=1714429187"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/basseyn-karkasnyy-metal-frame-305h76-1072185878/?asb2=4nenQVBFwh-BddEYzJLsAXn9ODKPc9SpXR9z7MH9F_JIopLW2_W2TfiVt1Ea4_jr73_WNXjC2rxTINd2mB-M6Q&avtc=1&avte=2&avts=1714429204"
        elif product_name == "Детское творчество":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/disney-bumaga-tsvetnaya-a4-21-29-7-sm-8-list-sht-611527661/?asb2=UAxQXQAC4MsCeew1L2N7hWINVZT11MlQv_bmKR7tfySDde_W4TaS8xf6lzyeVuTaiVisiawMGARz2v-zvgWFAQ&avtc=1&avte=2&avts=1714429227"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/albom-dlya-risovaniya-20-listov-a4-na-skrepke-bg-ekstremalnyy-ekonom-8-shtuk-v-upakovke-875053685/?asb2=BvdG_ofYbVk-i7V3jc3Q8TVtQkiIUwp5_13Hcqb9XBif3biZMdVHrSUQywPuKShTtscCT7Kowxo441au-Hfn1A&avtc=1&avte=2&avts=1714429243"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/schoolformat-albom-dlya-risovaniya-a4-nezemnoy-zashchitnik-vertolety-skrepka-melovannyy-karton-972401358/?asb2=LzdvxBE84vZxOHAY0EztXn1R6Pje0pl967nbdPK1yd04cLO7Ap8a1DGPw_KDVOih79-FibkJly2XWoZa2qC6LQ&avtc=1&avte=2&avts=1714429256"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/calligrata-karton-1459475586/?asb2=0fhwu2UNYZcdTF2C2YvbWCJvUqsRiTaBfCfv_AwppmSq_Us0oLnugk-NFvfSxvlXmBp6wEswUWozcHXT4owcOw&avtc=1&avte=2&avts=1714429273"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/nabor-kistey-dlya-risovaniya-derwent-48-sht-1476764503/?asb2=bRbYTvWo4khLza5In1N_wcaN8tmVme6WFhmsLNQvmW21TjP-WFo_K5xSZZNaNCz5&avtc=1&avte=2&avts=1714429285"
        elif product_name == "Настольные игры":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/nastolnaya-igra-dlya-detey-voobrazhay-ugaday-zhivotnoe-umnye-igry-154461850/?asb2=9cSlL0nb818lWJAHaGgpSu2Q5Jp87nmNnOr8twzKTjmnUNd8zVJC8SR25kf3PQy4iCKfOTEydxhn5KUNWn_cpA&avtc=1&avte=2&avts=1714429314"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/nastolnaya-igra-memo-obitateli-zemli-50-kartochek-221273622/?asb2=cq4XpW7-BvgRfBZupDf7QJe4_B4FEjMrYjEtbarrk12FcSGfUnPzQti_J_zqLkZdQsVo0vtHtqJ4NP6Lg8xdsg&avtc=1&avte=2&avts=1714429327"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/origami-nastolnaya-igra-ketmen-protiv-myshey-936297591/?asb2=JW3UJMUGbwctusAKQQ4mToKoxXCHOAPzF3CfKJmvX15P0bX-jQAIflsRBdSRWHrwlrP-3bpTrYRRK12ojeJWRg&avtc=1&avte=2&avts=1714429342"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/nastolnaya-igra-unmatched-jurassic-park-dr-sattler-vs-t-rex-na-angliyskom-yazyke-1543585001/?asb2=BglEeLeUiYLS283Vxdaqg7_U7ossKvrty8VuwnQyhxskZDcGNbdaaySKzrGkRZPJV1gy8ei9clxB2LnUIv8WDQ&avtc=1&avte=4&avts=1714429354"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/nastolnyy-futbol-chempionat-1396768846/?asb2=FLsL2wi6FKTFqnS-xWLqhCrVH-QfbC8vcoAOVCavCknd-xe8Fron8dR88AL4jirG3edG5cZ88ivE1V0PJvwgow&avtc=1&avte=2&avts=1714429373"
        elif product_name == "Для школы и обучения":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/lineyka-derevyannaya-15-sm-1266763761/?asb2=AdxzcCubzy4YWTt4d2Jw1M07YmI9hIeKbV6M4Gd9tRz3nVJoHM6kQPhzuEhU_k9bRRFNcQF7TsKYDIEJ7y2wh5Bqh7ZJgG3CwuOmcvQC5I5qjvBIWHbhOjbeUajyUaMK&avtc=1&avte=2&avts=1714429400"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/bg-tetrad-a5-14-8-21-sm-16-sht-listov-12-1162882388/?asb2=UlUdzSDd3oYCCVd2NgKaVxfb_XzAX0AMR3pJoIiWWOx5aMEvmzZjDOxhJwvOaq2v2DUCHR5Be720_J87wCzw8w&avtc=1&avte=2&avts=1714429414"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/markery-dlya-neyrografiki-1317502396/?asb2=J-i8rr-ALxyZdnn3M87KYemLdpWfeCW7gRoWomHzMzayzZdKmmjEZwXWPeUv28iD-vA3JqtV1sQRuZfpWUMNYA&avtc=1&avte=2&avts=1714429428"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/ryukzak-shkolnyy-genshin-impakt-genshin-impact-lang-1535293864/?asb2=BiVXEqMGINaXM6F8omn1TPcjBedayWi2-O5wBmTqIs6ar8FlsW2Fz-VRQU04EuFi5KmLhFyTN-B_lPki2XSSWw&avtc=1&avte=2&avts=1714429442"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/ranets-shkolnyy-1537009621/?asb2=Rq9jr55Q-sX97BelZ66LFTKZkTXLLmwr6SwikuELjRTvVjpYWaninhYV9843D6vo&avtc=1&avte=2&avts=1714429454"
        elif product_name == "Подгузники и гигиена":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/kukolka-studio-vatnye-palochki-105-sht-1100840060/?asb2=1qsmRg0i83EfeGsZFTvUv3TNA2vUbxXyAVLnYD4_zC1sE5YqBfckcR-gCb_5qF6It0k20X2Xy4s3vHaGk26EmvIP-qXvGCFOy1qPfVUSorhBAvEGx6TS0GJQbePvWHcy&avtc=1&avte=2&avts=1714429479"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/pelenka-nepromokaemaya-detskaya-mnogorazovaya-60h80-sm-1064482818/?asb2=gZ9dgzwkRpe_q2vmD322Mf-oIbIMUripUZPxtOKV1vfft5S4gOWRaT_I95ptoib_5NhFZ_eh9yWflG59VGDlhw&avtc=1&avte=2&avts=1714429493"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/sredstvo-dlya-kupaniya-1555921114/?asb2=WtGkYRVx0-Tk_BWm0NV8mQzeRJnbDFcviM0Ie71NmUGm8MGvP-b2n2KbjWLvoH9Pr8GKbXXsKscrt8bszxGgoQ&avtc=1&avte=2&avts=1714429507"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/igrushka-dlya-kupaniya-muzykalnyy-fontan-hape-868372073/?asb2=35nxvDS3VbK9FV-gW_PRZBx7F5BXm7fzDV_SfYX-6zraFNwr2D0OaR0JfA_rFwF9&avtc=1&avte=2&avts=1714429522"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/podarok-trusiki-pampers-premium-care-6-11-kg-razmer-3-2-sht-272089714/?asb2=ZCMmMz6XrfyzHArICKNw8CokCWBCiXDxRN9vOy44Nsswn00Zm8gkiBLLewg7zixh&avtc=1&avte=2&avts=1714429534"
        elif product_name == "Детское питание":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/babushkino-lukoshko-govyadina-pechen-pyure-s-8-mesyatsev-100-g-142625136/?asb2=brmNQty-Vuhfds2dZR5eZukjg0_5Wr-fXfNjZ46MfTqlaI_AlhYweyrrol13IphS&avtc=2&avte=1&avts=1714429569&ectx=1&miniapp=supermarket"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/pyure-fruktovoe-heinz-s-4-mesyatsev-nalivnoe-yablochko-90-g-x-12-308007142/?asb2=hpwM9lfL7YRjDteunvpYfHjEcf8AwFt3Wrt50MNj91G-acojiNP6oqVBVb2dHRirHuoOqNRuZqUnUVVltxiUqg&avtc=2&avte=1&avts=1714429581&ectx=1&miniapp=supermarket"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/pyure-babushkino-lukoshko-yabloko-grusha-tvorog-s-6-mesyatsev-90-gr-12-sht-1300412228/?asb2=no8ykvE8ITb3zXtXhfnnzGcMSy11vUHwJAUhbL7VKghnn79ckl1n9AMc3M8iwJNLrmATR3hnvjpf7zaLGFE4XQ&avtc=1&avte=2&avts=1714429595"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/resource-optimum-resurs-optimum-sbalansirovannoe-polnotsennoe-pitanie-s-aromatom-vanili-dlya-detey-s-798109351/?asb2=9j1m2DlkpdsXTWifRWEooYAWEDmnqdtIeRp7Ta4NABZVmLpmyqfRt7Lj9ie-o1ke&avtc=1&avte=2&avts=1714429605"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/nabor-iz-3-h-shtuk-smes-kabrita-2-gold-dlya-komfortnogo-pishchevareniya-6-12-mesyatsev-800-811078837/?asb2=DhYvyCAn4Ws6Md3PXIVYEuTtyx9oVQlOlmAdhH1LJI4z6YaAnOqPBv8ZGjsqG_b8&avtc=1&avte=2&avts=1714429617"
        elif product_name == "Коляски и автокресла":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/eg-moskitnaya-setka-trikotazhnaya-na-detskuyu-kolyasku-1-sht-140h90-sm-540024704/?asb2=ISOjzHEGLjCPh5ABOxqJC_LZL01r6cBVmsbQdWa-sldGLmMGKmDJUmPuypncbSjG&avtc=1&avte=2&avts=1714429639"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/okonnyy-zont-na-molnii-ot-dozhdya-dlya-avtomobilya-1537464838/?asb2=dQgbr-ry6BJ4uYXrlpm4D0lLFiOtShHDdlmf_V4cszzLB6owoI1Eo6LrRn3EwSSdJ1_nZMPzVV6KKb6Kk0an8w&avtc=1&avte=2&avts=1714429651"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/baby-essentials-podvesnaya-dorozhnaya-sumka-dlya-mamy-30smx20smx13sm-1561513944/?asb2=hmIYL2KI-eCGxE2uDuTUUeuKCdHH4kJF7BKibRhEW9fVPPTnrwpJsP-LRuTH8tx3sm1iCajhoixcg0AZBAN6xA&avtc=1&avte=2&avts=1714429661"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/skolzyashki-sanki-kolyaska-dlina-102-sm-shirina-48-sm-1378167258/?asb2=-Gzbs0mvx_KeKyyT4y41U3XcMEs_N0jI2IafQo07pvQsvNeDTv_J4LuAysVCtYlfukUyrG3OAFzmc7MkZdHyRg&avtc=1&avte=2&avts=1714429669"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/progulochnaya-kolyaska-indigo-maxima-svetlo-seryy-1363418914/?asb2=Pk4y9pr-EiTHIuLYilYNTcWb8UbXu156PNbhQ9Xc95-S4sm5Yxz02m8SCNebxUMcBp2LdbnpMzCH3p_qz_F8MA&avtc=1&avte=2&avts=1714429676"
        elif product_name == "Детская комната":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/prozrachnye-silikonovye-zashchitnye-ugolki-ot-stolknoveniy-dlya-rebenka-2sht-1518331645/?asb2=FfxMAv5B8n_C-zPal3FzsUcnJr1mAlVN1RNfDNBnPculaMJsFghl8MWug0O19dZEeWS-0xFowU0s8c_Zk5xeJQ&avtc=1&avte=2&avts=1714429698"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/korzina-dlya-hraneniya-igrushek-belya-odezhdy-bolshaya-s-ruchkami-50h40-sm-1397945691/?asb2=cKLSskx5ngWJ10SVqp_ALnJBqXnmY4c_dxVf6ErtQakCG6bpn_jV-rKuizJvRzyaNjOay3oRlfMWk8o7FmnXPA&avtc=1&avte=2&avts=1714429708"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/namatrasnik-nepromokaemyy-natyazhnoy-140h200h25-1269275453/?asb2=4GerCYkr5o-JnNVixc6WZ9GuHuy31zhzMEtPjAVnnh62hBzHzYFvxolGChHWg2S_Pntcqu3fzqLoNjBdoA6lsA&avtc=1&avte=2&avts=1714429717"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/sitreyd-detskiy-komplekt-postelnogo-belya-hlopok-1-5-spalnyy-1508500969/?asb2=1QHpZv6s6umDdXU1EaEoDloXrN0-xI4hunO0zGZSIjg0YBYhOAV4u1u_BvNGTZcx&avtc=1&avte=2&avts=1714429725"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/razvivayushchaya-igrushka-vtech-hodunki-dlya-malysha-1559763851/?asb2=ZjT9jBMExTZO1y-OtdAvP4A294apDC-vBrpNVzOAk1x282loZRzxEHcMl_GgZfgLBexLYfzKlh4gpasxFLlkkA&avtc=1&avte=2&avts=1714429735"
        elif product_name == "Товары для мам":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/mum-baby-prokladki-vpityvayushchie-dlya-byustgaltera-497905963/?asb2=MGSCsztgyR9lwDOmhpj3oem0BUn5JyeKuW0kNzOEUuFf54zR0LXI0WgAR2d9LcuV&avtc=1&avte=2&avts=1714429759"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/bandazh-dlya-beremennyh-euromama-budushchey-mame-do-i-posle-rodov-166306264/?asb2=APm7iSYeKNCv5qS6jFe34_4KWb_4weqpoDvST4m2DEpF31bhSmsBOm65osSy7MJHbhOXldLJmL9Xa9quFtRLog&avtc=1&avte=2&avts=1714429768"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/komplekt-belya-ripndip-1146248019/?asb2=HLla_3XeZ1lLW2Hqt933DJAhjGCR-OO4VNi5B2bJ9zZzpZ7rBU_Qbd0PkS0AkZeMDRyJjJr6JtCdlBxKfJYISA&avtc=1&avte=2&avts=1714429777"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/pharmedoc-podushka-dlya-beremennyh-i-kormyashchih-70x350-1494799084/?asb2=TBBsAFPjTrA51M1S1CDbvxsllEigln33mV1G1n75-ThfdA9vSHEc_Lb299jFdIxWxwX-v1gqpBtmDxqWqj-lfg&avtc=1&avte=2&avts=1714429785"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/purelan-37-gramm-purelan-dlya-soskov-medela-lanolinovyy-krem-balzam-dlya-gub-krem-dlya-ruk-1494823844/?asb2=8fksxd5I3JnWQITp67oYz-TLVKrp15yYkqO2B0UhUmbr30nBrAwj9xYCNltu6EBJFCNSpK16GUUWSD-usdl8qA&avtc=1&avte=2&avts=1714429793"
        elif product_name == "Товары для кормления":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/1-sht-shchetka-dlya-detskih-butylochek-s-dlinnoy-ruchkoy-myagkaya-gubka-shchetka-dlya-butylki-s-1473624793/?asb2=klW9M50QBFe9H6owSHmenlfvzcgghMbmyeo5xAN0fbLM41iIA-IldWvXPbOsdOMx8lOij4AVFkEj64-_arqYwg&avtc=1&avte=2&avts=1714429817"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/silikonovye-detskie-igrushki-dlya-prorezyvaniya-zubov-15smx5smx1sm-1561541939/?asb2=3IZNiFYcTemGq59Z0afGuiPVaLNMvn8w6Kzwo-899W5h6H37CgaNJfksxX3SCFPr9IevUyeqmWjmkLR9uMzsiQ&avtc=1&avte=2&avts=1714429826"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/molokootsos-elektricheskiy-besprovodnoy-bk-289-rozovyy-1418665329/?asb2=vnsfaa6LMzhI77XXiSYIo0QVyI8y0esttgk9E6rcpy2lmN7Tigt83G8CGPG9Z0ISRl9-KYfMHHX2mu2LYnv5RBEBK-w49X7msj_kl6nG7I_E3bbTPILzAmKDh3J2OqFc&avtc=1&avte=2&avts=1714429838"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/silikonovaya-tarelka-na-prisoske-bololo-baby-s-zashchitoy-ot-ozhogov-1520853843/?asb2=cxND7e7wdNrpUR_R9_mKHQ9eVxIQ3QEG7G7oC_6dFTp4lgY6tvBujnCj66Y9Jb54OnURPT5_f9osKdfsyGatpA&avtc=1&avte=2&avts=1714429848"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/stulchik-dlya-kormleniya-1507674520/?asb2=Wk9rCCS4lsUV3EonDMylQcC-mDYjoD0sr5IhyZU2HMHJ5D-Uw-3o5j18M-j0ld170PYRDizuJN4_uGNR4VnYnA&avtc=1&avte=2&avts=1714429858"
    elif category == "Одежда,обувь и аксессуары":
        if product_name == "Худи":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/hudi-1499971533/?asb2=un_dgxmpNDIclSirbTUWjjRhjy8YQ2vJc_NF22mZdZjCyLtpuR3wGY_Yl6E7PBkH0I3a8-ROUKqNrUrrAbnxdw&avtc=1&avte=2&avts=1714429918"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/hudi-jiyaoowr-893043938/?asb2=kQ-l7DXNqOaQcyO6dpRwk6JTCLjd5hv5drRgeshYxJtl-9jpiuBNXeocTZt1InoNCHMk7u-lV3VWqiE61YRSOA&avtc=1&avte=2&avts=1714429918"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/hudi-dreamshirts-studio-1542850664/?asb2=FxcdJt41B4BPPFbPNF7QNK4Q8Qds2sMCwx_DL-HzOt6tc2VX6GSUBNi9lwehhC3tdXtEBSP4oD7CwZt5DpCRBg&avtc=1&avte=2&avts=1714429952"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/hudi-snrg-1191457883/?asb2=6TJNKzZJG8BNyKuFEt796sij3tBJfxnghPyQGQfdvgiW1k2nnxbXxzNb7vEirs53eQfWR6E0IJhZtYGHQYcaxw&avtc=1&avte=2&avts=1714429966"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/hudi-alpha-industries-899110556/?asb2=Dt033nfZprimy855K91MCN9fmfxti6U9YroqVf6bDCTWPHFhGJ-ZyO-Bnaj3s6kPfzq79AXk-K5MPeVHaM9A4w&avtc=1&avte=1&avts=1714429990"
        elif product_name == "Куртки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/dozhdevik-rybalka-plashch-dozhdevik-na-lipuchke-s-kapyushonom-zelenyy-universalnyy-plashch-557530352/?asb2=hg8_dI3EjP7Ud8V-bBiqV1jdrwKgWQS0CSIuB72CWHD5ptbJApQozyNhIGo1S8Lo&avtc=1&avte=2&avts=1714430018"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/vetrovka-1488989031/?asb2=MeqFmxPDkq8yubI-MycUat3GZB51-GaqRv27b4Y_937wH_1ljVcLjTxbBE7bHePBLLI3ZQfDHk0gvl2Th8RyOg&avtc=1&avte=2&avts=1714430051/"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kurtka-968538101/?asb2=kV_CE2EH38gPG1Hu6Gs8T0x3cEgMstEwlvKkrGNtRUYJDY9KV8VHmLMZsH4Jr0Bja5ZCHWTARWUGItS_8q2xtA&avtc=1&avte=2&avts=1714430105"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/anorak-nike-1506737976/?asb2=R_sa984gX2GM3mwqBN4f_auawaBTAL0M_AYlMCFqIvfFub678OV3w6A4QaDJjoSXuTKpJzyovC742doBHkGiCQ&avtc=1&avte=2&avts=1714430127"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/kurtka-borman-642954143/?asb2=gchD28ptQE3jRZUU0DW-5edHmyHh7pCyjUDWBlCZnR0Y7RwjmLFPdyiQUD8MdqUW41c_mvQna-7xcK3bJ0Mh6A&avtc=1&avte=2&avts=1714430157"
        elif product_name == "Обувь":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/kedy-kolesnik-960416254/?asb2=LYBxguU6U9dIC64h2D-vlV2LRkUNgnDekyo19BYM6xqscBUNakdWjfhZru3ZAo09sHFTfm4PMSGh8C8BP93f3A&avtc=1&avte=2&avts=1714430248"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/kedy-forsa-823755675/?asb2=K9URs2ICKbndHaFm1eJi7WU4AeQ-iSqkvXEg2lzy1AQM4F3lk5WIGLmvfosp2trISLviPa-Dbsor1kkTu2muDQ&avtc=1&avte=2&avts=1714430266"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/krossovki-1538766475/?asb2=LXkW9Zy7rdSdB2Z1E8-CeBeDF9s4QVaPXt1zpeJZEVX3NkrXVJiMVSwLwn7tzfsSzhPv4OARymj9JZ7qtM4hjg&avtc=1&avte=2&avts=1714430281"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/krossovki-nike-harper-s-bazaar-zhurnal-1530222726/?asb2=b0S9M4LcuVXKb9soR91TT6TlGk9UykYNnwtwRa-MROpnMJ8XFfsgaYMODmTs2zhrVCJtNm47P14mKjnMzBcXqA&avtc=1&avte=2&avts=1714430291"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/krossovki-lacoste-1440321288/?asb2=SqREaXW1h_8THmgZTyyjAOXuDzPHm5MrpoKLQGtT5Zur7RgiqvMTq5YAbLUf_2gQirXVhKHKdtkuU63Xc-6scQ&avtc=1&avte=2&avts=1714430303"
        elif product_name == "Нижнее белье":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/komplekt-belya-enamora-1547961638/?asb2=GW2gVATBWtTGVXhJFqn80HQRtQyjZiiuBi8Df2EPbX8tMISIZ_bzkmN8xnjp9wjKvfpXdvczcQZh-6sSbjqhMg&avtc=1&avte=2&avts=1714430336"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/trusy-boksery-brify-veenice-nizhnee-bele-3-sht-1376969034/?advert=FxImlrExrjW5OY3V1ttYDetjhkMrxse1USfgJkMK3gyoBzxv2y8IrOdEUiHONyfR7DOhGnTFwRphA78jJ8Go6AHJdfXUAcu-uiR4k7kB7PSipxifQz0qTo-ccRUsiv-4S81pfbjZSYMdU2nE4sH1nJ5BepTwlWFXOdJKoWuj_USe4M-UrH-GtosNyo_0mWy9tbEqAgSv07xMu5jU3KUxV2dpaaH6fvvtiVzOxVc7J53Ui5j0VU9ejFs8U3YltCooVPnj_PWA1E4&avtc=1&avte=2&avts=1714430404"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/trusy-1-sht-883811909/?asb2=pghydQ6LYzradJ8YBoWbRcqXJNMIIv01p-70VCtUf54JYjVTlvJ3_R5i24XsejgVS9999cXnpjdoMlWdwJl-yg&avtc=1&avte=2&avts=1714430447"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/bodi-gingerelle-basic-slim-1-sht-1451704651/?asb2=kiYiT6hsRB9ZvKloIMDYnUyyZcfznFAsTsKxsbN8FEegF_oHF_71g3uZ5Ql1LmV2IwfWnAPFgn_jewBRB1vvRQ&avtc=1&avte=2&avts=1714430461"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/bodi-alo-yoga-1-sht-1539238938/?asb2=i8_z8ncw6xEA128MC4XasrAHV3kRHlJp00mfWDZOZno3PcCoH7tO2loiI_OjOFXvgtzhV0Z4RkVVrZ-npb-aZw&avtc=1&avte=2&avts=1714430475"
        elif product_name == "Футболки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/futbolka-misterbanana-538185661/?asb2=mJO9k6URt6030F8ZRpiWK-BXd_QPpHmb3KZtRtWQeA8oL52PtwDdYnq0j04a9J4yVYRlKPzz94AU7sQT5ssTqQ&avtc=1&avte=2&avts=1714430560"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/futbolka-845499684/?asb2=f_FQpxUU2OYYPKkeGAXECGLtGRpnw4p3GfDnHu30gn839t0GDhtNJV8ZI4TzHcn8mW6o6Z671MRvengQ7U8ZYQ&avtc=1&avte=2&avts=1714430575"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/futbolka-1547016434/?asb2=9DBqQ9yzDxn0eGI6a0lu5EF8Gv8YBkRCUC8wg1-Qg2Q-8FQ5kW1yuasERS-Yw8GLizenlEs7FlRIzt34cO214w&avtc=1&avte=2&avts=1714430586"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/futbolka-1290376963/?asb2=c1o6EoZteCYcspWLHSE77g-VXk-x7zBo4AMIDh2fzrw4nACtjolXYyXyva-TP-DfhIIKO-mq1-O2THss4AbksQ&avtc=1&avte=2&avts=1714430600"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/futbolka-1561685879/?asb2=6bq5AyJ9FIeHvYa87HK7V_nQp1cyL8LGoij05vbzdlmWGshq4KIY7eo6lmm24-MYboN7amvj6jEUCU61TgKEuw&avtc=1&avte=2&avts=1714430610"
        elif product_name == "Брюки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/bryuki-rti-tex-911109485/?asb2=91HSXVRho5Ze-ka1dS_60iFxF8zSjr2xZawfxign2GhxpofsC7dG3_yxigXLw91RAEp8_Um71w-xbNnLuyxnag&avtc=1&avte=2&avts=1714430630"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/bryuki-h-m-1147842695/?asb2=vLxsCaNdd8IHpzHS_k2VlbGFyucBuyUS569Hv7DonUyAmnkl6ZbAdnjMkU0iCiDIGhsYOvkcMX-7cMVbGPB9jw&avtc=1&avte=2&avts=1714430648"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/bryuki-1554618722/?asb2=E1pCrxxCM0d7TIUGwtAGoxbq_ULPlkGbqzkjQ21qkOpIux5qRAiqPFqqlGpTa9AJKvk4ajsRLx12-NsMt4lbgw&avtc=1&avte=2&avts=1714430658"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/bryuki-1522728599/?asb2=lsBlho7lvwlUjY-W6FLMeC5aSy4AR7R6gUkV_uTNuHOi9mPvmLc8Hdf_WABNcChB3DNg5nAD1fQ91Tv02-sAuQ&avtc=1&avte=2&avts=1714430670"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/bryuki-gardeur-1373423178/?asb2=eVrI4i_7setQu78qPgaa_GM_Yk6fc0QSeBL_ZZ2r9AekuEjoQWul5pttMyXI5lnFPSa4nHQ0YZpTB7jkvTO9Jg&avtc=1&avte=2&avts=1714430689"
        elif product_name == "Часы":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/remeshok-dlya-chasov-silikon-remeshok-dlya-chasov-893939939/?_bctx=CAYQrdJT&asb2=QqLh604vNYzMPXQMaULQkDSaw0_tf9oUqmKDHYFcRtnLZdsW3YLc_2ICr_FZYKPerwNxH_8MaSLBTsQhWxW7sg&avtc=1&avte=2&avts=1714430721"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/chasy-naruchnye-568930532/?_bctx=CAYQrdJT&asb2=rD3ACj08N7F9iWx8Sm7QMMkEkqpzs5knrS6y9FstlgaSox4WejbJscQvZ7xvCszAIlUzzWEAddLZcke7VD6rOg&avtc=1&avte=2&avts=1714430734"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/chasy-naruchnye-kvartsevye-1549327298/?_bctx=CAYQrdJT&asb2=pfEvp2UoT_44mze__20SfnCVsH6JCUFZMoqSFeIzXah7P3lMVjZJv30bDwpfBsih03hAvNMBO2Ndah9vMjlAgg&avtc=1&avte=2&avts=1714430743"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/lee-cooper-chasy-naruchnye-kvartsevye-1560417622/?_bctx=CAYQrdJT&asb2=pVvJhL6lZsN8Ppe3TCrqUcgHHwzQIhN_271mx-7j2gC8_zTZttqA34n-vD-hCyYc-tJNcEpZYDFYbx57zvvdsw&avtc=1&avte=2&avts=1714430753/"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/audemars-piguet-chasy-naruchnye-mehanicheskie-seriya-muzhskih-shveytsarskih-chasov-audemars-piguet-1496539476/?_bctx=CAYQrdJT&asb2=BnaSEgVZPoHxuuuCZk9LkZTa7PJmYfmxnhFzLmvapcmdQ7joEOKewBzyZIGdIwR07OHesazFRZYQH31uEifAcA&avtc=1&avte=2&avts=1714430765"
        elif product_name == "Джинсы":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/dzhinsy-i-love-mum-novaya-kollektsiya-1162705556/?asb2=bcGSINe0IA_CmUvM2AINK-vzOeIoOkV0BCHhZsDfdwk-Qa8DMuEdlzV4GkJ5FYhFhFHcNbh6BRe8nTl8IU-7v8LyR1qVOGQ9jyeEuRqPLmkOarQPMWn8ksWkmIJYCVlR&avtc=1&avte=2&avts=1714430780"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/dzhinsy-h-m-1072442424/?asb2=3sy_y9atmSesM21QHjKfkHqhLOJ1NKG8JxnjCgQ305hE5qIwaZfp1JKSnPeh2CYEWnt9MhnQBE_Tyg014p91dA&avtc=1&avte=2&avts=1714430793"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/dzhinsy-1550227689/?asb2=0PFTic7rTyiBc-iIIQnztA9j060CkEzPCCZKsh9irnof-R2lotX-eTt8Xe8UDEkv5-uulz05eHHpwsWXQ5pY2g&avtc=1&avte=2&avts=1714430811"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/dzhinsy-guess-hollywood-hollywood-straight-fit-852591194/?asb2=WVsnHurwSPoN_BJBI3caKAMXkccOeC1CKTYkRv7-gKIFF9EP70-uHRRoAivTQeiPB7OZMXZ85cn7E-OFa5QoRA&avtc=1&avte=2&avts=1714430824"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/dzhinsy-1512907019/?asb2=73i1YN9WLUXi2X5aBxMAeQUj3A0jPdNxy8UHN1-yvngtZwmVjGNjeh5glQ44Ss45jJwUbfTLXCGkN2WPQ5_F3Q&avtc=1&avte=2&avts=1714430840"
        elif product_name == "Головные уборы":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/kivar-sport-povyazka-na-golovu-sportivnaya-1352323356/?asb2=r9QOX9kze9sVlXFXGyvD6by1mRoG70zjrzSaPdzOLDQe7iD7LIRJ5cDgQETfdCsesSnN1etcCWZoIfupmbk6b94cMy8AWxfZDePYhsPYY1NJMs_mI5o-oFok04x-HWcf&avtc=1&avte=2&avts=1714430875"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/beysbolka-1431490063/?asb2=ZYujJ9Hh-PhUcmADT7DI_wHpU8uyWZwjchqpG52dQL6ar7_j5ctVR2oKZj08YDomCZxX-6Dsi6P3I5_MFy80knRkkV6ObxRwxpRQ4f-IUKo&avtc=1&avte=2&avts=1714430890"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/shapka-labbra-416893300/?asb2=018Z9XbzeiTcXAMY0aH-P3b1T0co8MXl_pX6o_v4K71Oaf6hPlOolhg_FtacwYPglF79CKt6Yzh87DxsGmAprA&avtc=1&avte=2&avts=1714430899"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/shlyapa-the-north-face-1554161903/?asb2=cU38cot6vCicWYzVPlTYRSUKB0PoMdH4pxyT9VjjPy2Fp7TdHuzBinEFoNESGXAC6G1MBJu2uSa2aHeenqOZug&avtc=1&avte=2&avts=1714430908"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/shlyapa-1530625491/?asb2=Tjbd0F_hhqS-L5RSlU5eNlZUCVF4mP-ApD6Qn-hSk9Ydh8WJqEiabxV3DR_uvMGEMUUgjUlvsJ5ozTteYgh1wg&avtc=1&avte=2&avts=1714430917"
        elif product_name == "Платья":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/plate-modis-utsenennyy-tovar-1356563349/?asb2=y0tGnfpYkHhZ6j7WxYwzLL-sgVWPDQzgA8aZ9OjSZnuM4VSGo9P0nuhsRWP3N4mbAQIhGJEdcxm87zmFLqRTtw&avtc=1&avte=2&avts=1714430946"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/plate-sinsay-1083379768/?asb2=bjUfvvUvTEcRDR9PVO_Fcr8ZYK1Uk2k1JUvjEvuhKkDOo5E0rwalqt-53lLoShbMD15jgg4a2QK4idDtndDuQg&avtc=1&avte=2&avts=1714430955"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/plate-aprel-1273209977/?asb2=weRKElzalWU5lielhVZPyeY1Z0B2f5sPPo97az6weTPLew5OW8S2E8penE2d499oBitrsh--rJjLCdRXpphiq54FXJj4ZajPGY0Es8smULa2q4drW7544Ppi_roVI-rT&avtc=1&avte=2&avts=1714430965"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/plate-1515969529/?asb2=1Y8705SbPVLFjWtpnG5w0FcOre4KGzCcZ2k7mwUNprllofCIOvPGHgV6JF1M1N_8WTvMPOBfaC8Z9FsUovW_Fw&avtc=1&avte=2&avts=1714430973"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/plate-1535796222/?asb2=-9onAiHeDQ6mqxycsOUWzf1_62Oqfj5SIqc55YL6W-i7MOu3NWc-RSzOck30RstglMjqRh2YE5ZcT4mZG1yFQw&avtc=1&avte=2&avts=1714430982"
        elif product_name == "Юбки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/podyubnik-ado-ves-mir-mody-611017158/?asb2=R7KVYIT_PLKx9vums527Zivzejm46JyCq927fZjbb7vEvvyQj3y8BNaD8pGD0v_KUzZq5G3eq_AnonaJqwijHgA62WAyQ-y6rA894YFHWckhXLJJeEs762SKpHcEwLcK&avtc=1&avte=2&avts=1714430999"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/yubka-1550289817/?asb2=4A16oYnq8HMvI3IeIOeLBmjvcqoxbneLdUfOfePq2VIRGiwjf-Byx0IuCwwDuVUwATB1Yvsb0QCX7PRX3jF-vA&avtc=1&avte=2&avts=1714431013"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/yubka-maxadorre-730006207/?asb2=DbIXzk5GTYCcGsMN68AkM2Qc70M2Sgid1oyfzI99YwPRM5QN7RV8Oe0fsvPbTQbssxISYRLJr3BuCSPdistlOQ&avtc=1&avte=2&avts=1714431022"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/yubka-pull-bear-1448610643/?asb2=gipTjoK8T9xIGAQSZsg2c6Mi170NwTPSifhjkIUHaar_9d56ByhhnHDhzxI7-MvrsOo8DQxJLZ4xdLJp5AWOnQ&avtc=1&avte=2&avts=1714431031"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/yubka-theone-by-svetlana-ermak-1415521338/?asb2=0Oq9yoYhL5RzqnbotKZxTdLmqV-runE8lrVZ4lvRqtQoAskEHj7B-i1RRXOqIAzYLX9-T0ghZl1iX5hr_D7rnw&avtc=1&avte=2&avts=1714431044"
        elif product_name == "Рюкзаки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/ryukzak-meshok-oriole-35h43-sm-tsvet-chernyy-dlya-shkoly-dlya-sada-dlya-progulok-dlya-smennoy-obuvi-701046286/?asb2=pDV0mj_X2WpZaV-uxBh4Qwq0cV1SO47S9Cg5qeTxSe631QiYp40f4ggRA5vBJKTD91n8_B6cPBMS_L05zVQ0WA&avtc=1&avte=2&avts=1714431062"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/ryukzak-muzhskoy-zhenskiy-gorodskoy-sportivnyy-shkolnyy-povsednevnyy-vodonepronitsaemyy-950514711/?asb2=n-iLYkhtiSLhC5rOH--OxlPtXAJ6qgDbyCbb8fIuwPjTmWUjBAwjJu9KomAlM16U51o6Dhh-R5UmkVFkg7q1mw&avtc=1&avte=2&avts=1714431074"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/habastore-ryukzak-897566586/?asb2=qsp_z_K3OA524dRCLyvNGCr3fWWjkqYkBJPnhMshcsT7bQMKAu-dBxMluRlhvNbi6HWxMioeopGp0v5En7UAtw&avtc=1&avte=2&avts=1714431086"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/nike-ryukzak-1552838620/?asb2=1JqEB8fD8VqljkdVt2iyI5YovebdPsmcQO9MClfIaSPIR8SL7oBdmsSV2DH3a6ZBiWMBPjy731ug9_zXSjIzoQ&avtc=1&avte=2&avts=1714431096"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/burberry-ryukzak-1560848115/?asb2=l09HCvKk9u1kB3uoFgfbYApGWrMF-OS2t30jqRE3SBEPBN-cF0fN4U4aY8xVVLqN5RsyyQhQ1zm8uYpdDGpxqg&avtc=1&avte=2&avts=1714431105"
    elif category == "Аптека":
        if product_name == "Лекарственные средства":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/nurofen-forte-400-mg-12-tabletok-146806420/?asb2=KbFngesNnOdCruI5nQc4uDh4gxFhkMPa6Im0HeDF4XU2uDFUOsn44QRimbKPTM9-AIkhUk38hHSErlfUK2U4Hw&avtc=1&avte=1&avts=1714431137"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/odekromon-tabletki-200mg-20sht-1409956481/?asb2=O6pDAfuzfTM_LLTpD_FQ1cTRoQOXRe_WYIulWvUlpWQC7Syh8QxsP9QF8RuYYZkyYwUdLvkPJdhLxH4WIlJEXw&avtc=1&avte=2&avts=1714431147"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/bepanten-krem-dlya-suhoy-kozhi-100-g-bayer-147251404/?asb2=e5HoqiqXbSYCbWess3C8r0d77u70yb1ABgy6Yqflq57gtGt8QrZ53IPe8i4KTrlMbvAAbVl1BOYA7RSGuW-b7g&avtc=1&avte=2&avts=1714431155"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/podagr-krem-maz-dlya-sustavov-i-svyazok-artoks-obezbolivayushchiy-1555167644/?asb2=YC5aCytW6KrIWIXxfC_816oUsy2sB-wl4-Mgyzt-Vd7qerEyFqcnK8sXVKDkTVL_Mwn9HMAzzMc7UeXSrY1jsw&avtc=1&avte=2&avts=1714431164"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/ripart-forte-sr-vo-dlya-zameshcheniya-sinovialnoy-zhidkosti-15-mg-ml-shprits-3ml-1-770350210/?asb2=4BqFr7M8tvBH6BP4ow7qGuNQh6Yaq5rFlq_kdCaZ5zcorYQqCYlhoAWq3FPt1rWW&avtc=1&avte=2&avts=1714431229"
        elif product_name == "Мед.техника":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/raspylitel-emkosti-dlya-lekarstv-dlya-ingalyatora-797936769/?asb2=hMBg-1khQcNx9HMbPZany7j7ZjHeHTLjxKfjFl8_4z6tsgtmILe6tQrVMWwcCetNEwEdAPcTZ9-BYEw_ezSk5g&avtc=1&avte=4&avts=1714431341"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/portativnyy-ruchnoy-raspylitel-mikrosetey-1504166170/?asb2=UFm0dLzB7w_mkFOv6FufyFKgpptE0SA5ROAMpyVRXSqBgdcUIQ3oHLgatxxMWwPEqPf9Khmhi1i0z-a65rGshg&avtc=1&avte=2&avts=1714431357"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/polimedel-plenka-chehol-bolshoy-dlya-plenki-1-sht-508542123/?asb2=9D79M3rF0POLRYGZfKP6ZcjvCJut0gFhu68DV5EcaIaoLpWueBiOlYtMLbn5spMvGhlQ56QXXABQ2y7rGKYuh5_ZSSgh3-7gq37zTlvyDq_EYdHbhblDH2xeMhkT0oRT&avtc=1&avte=2&avts=1714431365"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/shipy-mishina-elektrostaticheskie-s-bezinduktivnoy-katushkoy-dlya-vseh-tipov-generatora-sinusa-1087931828/?asb2=UUpJfDNnuAwBrpeb0K9q9bxzsGFmZ0SwZpuxGkuob1xTVZ4i3mYeLB7trAd9pf8XQ-8yZWTK8VuEjJaKS4WtUQ&avtc=1&avte=2&avts=1714431375"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/generator-sinusa-tgs-7a-s-dvumya-katushkami-mishina-odnochastotnaya-1-i-tor-1-714759440/?asb2=2q_c2nj4fMG1e1MHUuK6LvMtQRbhjJPW1OJ2kmgG2RCothqyLcPvmASuYm39PCndkviw0sbk5jdi0m_igw4EEA&avtc=1&avte=2&avts=1714431386"
        elif product_name == "Спортпит":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/proteinovoe-pechene-bez-sahara-e-baton-so-vkusom-shokolada-50-g-674723500/?asb2=iAKqlG4KHrQQX8nl3eSRnI7by63K7KETQ19bwKU73QtdOeb7QyPiD-mNiJZBoNYGNQLt2HXDCmVphY__7Zt54Q&avtc=1&avte=2&avts=1714431410"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/aminokisloty-prime-kraft-praym-kraft-bcaa-2-1-1-btsaa-chistyy-bez-vkusa-banka-150-gr-953972090/?asb2=yzQGX4VteKdjrRA8l_duIGV05O4O1WfAKL3MNf3JTxJOvSzeqHBVfK3jL0iuDhW3237wZpjDggJG3haIE_mJng&avtc=1&avte=2&avts=1714431427"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/izotonicheskiy-napitok-oshee-apelsin-6-sht-po-0-75-l-pet-1492262002/?asb2=AA9Bjd_7W_RGsnARFw0NmrrdAovAZCRP38bG_tqqJO5-lhXEvkMC3xDjtaDNdWLSp9eGXSnylOtoKawazv9ifQ&avtc=1&avte=2&avts=1714431437"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/geyner-dlya-nabora-massy-scitec-nutrition-jumbo-hardcore-3060-g-bananovyy-yogurt-939814013/?asb2=wY-m94mf0xfwMAurZwokTiC4mof8qaav8EQllw_GaWBwCkp1iGc2bxjyca6PLAjXw7X5uSZ-CA13RqySntUNnQ&avtc=1&avte=2&avts=1714431447"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/kazein-optimum-nutrition-100-casein-gold-standard-1812-1820-g-pechene-i-krem-913510524/?asb2=W4BaOeXmQ_K4PCwFReNE898YTr80h4BKkcXCu5v1yO-TGY3QhD0IWwSg_CSouCUr16reXMrDjnnlktLUVvgwcQ&avtc=1&avte=2&avts=1714431458"
        elif product_name == "Средство реабилитации":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/konteynery-dlya-biomateriala-60-ml-sterilnyy-bez-lozhki-1360192185/?asb2=E4A0_xuVttcBn-A65XSiinTN2ueeZzYncCj1bDhhoZzb2-ZTYAIOwq28MDLA0Y37GzHy47QMEw3pUdkK5WXi3w&avtc=1&avte=2&avts=1714431489"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/mochepriemnik-prikrovatnyy-apexmed-1000-ml-10-sht-540245483/?asb2=GydFIa4RmeFAF1mvzmtwKI_o4PABNxV6Ufqvi8_-MbjQmvdVdgdj5bBbzmjjtM5l&avtc=1&avte=2&avts=1714431500"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/byustgalter-ortopedicheskiy-posle-mastektomii-0091-valeriya-873714700/?asb2=6G1bPREA6xwAilz2knIaTl8AIqdpjufvwqX4vGk4Z118WDV2PZ3isL6RasO7xTXxp9u7xYt4-VnyQ6EnJB__Pg&avtc=1&avte=2&avts=1714431509"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/prostyni-meditsinskie-beajoy-soft-premium-v-rulone-70-200-rozovye-100-shtuk-1556871713/?asb2=HtUSmkGZgNCGc_kWEyUZ8djtCNaiQkmJ0QxGe4dZ_NbcWMDnf4tOfxZFzqCg2uz_99c7UGaENQUNWJXqNm3OwA&avtc=1&avte=2&avts=1714431519"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/kruglye-vrashchayushchiesya-diski-dlya-detey-sensornye-trenazhery-balansirovochnye-trenirovki-1551975187/?asb2=Fw6qvT1R1fom4id-tieNqPtLIsH3Ae0AU8qrZ8gIPcA_BvpZSaeCcFknvdAYSDRZ5EITVF9yItjd3_HxYChjYg&avtc=1&avte=2&avts=1714431530"
        elif product_name == "Оптика":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/salfetka-dlya-ochkov-tsv-goluboy-15-15-sm-784140573/?asb2=9RoxVA9E32LHzmyvRbjBzDmXRQLCjI7YY2BwpD1tNRENw8xjJzBk-P9WMV8og4x1JKu_C29PqDVARSFoIFYQ-g&avtc=1&avte=2&avts=1714431548"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/ochki-dlya-zreniya-zhenskie-3-ochki-dlya-zreniya-muzhskie-3-0-korrigiruyushchie-ochki-3-0-ochki-812542367/?asb2=g6AcO3waN9MAa_UzprGKYnxby_43qKWeJ0eSvVHX5OA5tiBQNQlH-Fp0JT88fQ-putewKFNehouOjhbQUEASfurX2K3ioQY0GQmm4MuePl6IKd40StIo2UBjlrdvctz6&avtc=1&avte=2&avts=1714431559"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/ochki-2-75-vysokogo-kachestva-v-elegantnoy-zolotoy-oprave-eyelook-d007c1-sispolzovaniem-tonkih-1-1407378001/?asb2=gYzFi-gVod-PilJWVR-UghwoX_8UsKdo44m5ztzLYqVL46kI03wMqK95ZWLpIjP4IhjT2TmXYWVPHLKmIvZqNg&avtc=1&avte=2&avts=1714431570"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/ochki-s-futlyarom-na-magnite-boccaccio-mod-0952-tsvet-6-s-flagmanskimi-linzami-cryol-1-56-hmc-1-798251242/?asb2=SZqknX27oPf6JOTROZd1HAyrizENfEhGy2YwwuodHWa4mcrjGpBt95Yu3m1JJLCE7SNWa1ShcaLwMCHI54sR8Q&avtc=1&avte=2&avts=1714431580"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/tsilindr-cyl-1-75-os-ax-20-sfera-sp-0-50-14-5-8-6-120-shtuk-4-pachki-po-30-linz-coopervision-myday-1167702257/?asb2=C5hKnkCWqyhrA6T6RjgXcrOaxAAohkYm9nKvcrWoPdJ0ORGyP-iT62ZMbqSAlxCeVKOVaiaDIeLIQ2HJAvO58w&avtc=1&avte=2&avts=1714431592"
        elif product_name == "Витамины":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/avs-helsi-fud-ledentsovaya-karamel-s-tsinkom-i-vitaminom-s-petushok-so-vkusom-klubniki-17-g-s-3h-676361495/?asb2=TJvMAxEIshHcDb0IYWTwmjjdcuhl38DJgoBdimgr9f-fqktgtJnC8yTcHGud1HLjY5DWAxttnGIh9qkxdcXxpw&avtc=1&avte=2&avts=1714431608"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/vitami-v12-9mkg-60-tabletok-1558822508/?asb2=j7UTjir1traE1jgv38_NODjZUUIUNVwL4sNphtiyRwQGlHbbGKFSZfAl7BewQHpf01IpTEWZUJZq8AiIwTEQbA&avtc=1&avte=2&avts=1714431627"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kompleks-vitaminov-dlya-zhenshchin-4fresh-health-koenzim-q10-s-alfa-lipoevoy-kislotoy-zhenskiy-1413339770/?asb2=M7jdeYQ5Wd3RiesHIjBy8HRrFaA3u5krGk2BJprB3modCJ0Fnxb7CaWBGgqvLfp_KYuzEt4eSV0DQnEOBCbvFQ&avtc=1&avte=2&avts=1714431635"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/probiotik-zhivoy-maksilin-939552978/?asb2=kjX_C3bbQk6XMxCtsSuZBngBg0IcT6t3yM8D9IN4PYAo8NA7BhPJeqEbhGrM5nLU&avtc=1&avte=4&avts=1714431644"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/bonotirk-60-peptidy-parashchitovidnoy-zhelezy-442902372/?asb2=jf0yARBIWkU7EUGUvi-Q7uzw1o_S3iwU4kGinG5He8ITUtVklPZrhr_aQHNoFqYx6d5hAU6XQDDNPsMy_WF_qA&avtc=1&avte=2&avts=1714431652"
    elif category == "Книги":
        if product_name == "Электронные книги":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/tvoya-vina-ron-mersedes-elektronnaya-kniga-910076041/?avtc=1&avte=2&avts=1714431693"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/himiya-10-klass-uglublennyy-uroven-popkov-vladimir-andreevich-puzakov-sergey-arkadevich-936175720/?asb2=j4ZUtPfWiALmFA_enPdiDwgURwV7RDElDTJsqQhXCvb6W5ScR-7Vq6YInU5uRr5VCfDhQDP3cuL6ry6-YlVgNQ&avtc=1&avte=2&avts=1714431720"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/gaydy-lvova-aleksandra-elektronnaya-kniga-1512233465/?asb2=NozXDwK-VsP6w0uPlQbhbj2E6wnkFhG1ev82hFcrajujsAPMQd8VjepmFL797x0ITo67Ok1UaWe1pG5H7jgDWw&avtc=1&avte=2&avts=1714431729"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/erfolgreich-mit-compliance-barbara-neiger-elektronnaya-kniga-912372390/?asb2=gNlDLX_WKzHsjSXXRFmdvn1-YKQCvUbuySJlZC6ghp6_7RMGFss1BoRqIpkz2V0r8NiKSZSSISEDx-DfLdzuhQ&avtc=1&avte=2&avts=1714431738"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/the-10-principles-of-food-industry-sustainability-baldwin-cheryl-j-elektronnaya-kniga-986351100/?asb2=PhSdhvTjLNnPd0y_JEQ-CFuji2yVVWLGUDDDTIEoj5f47dxhidV9VAZ7RN1E-ZqnnnlzAK0rWMiYeXL7VKuKMQ&avtc=1&avte=2&avts=1714431746"
        elif product_name == "Художественная литература":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/igra-prestolov-kardholder-gerby-domov-v-forme-knizhki-215h65-mm-216088892/?asb2=IDwh-F4YUQzU5JIW1b1VAqvp4YSeqMFI6Pe3UAZmHNb_JYvzNkXhyH5_fyc5pe0tyQOVgy0OFId3FW9oVJLrCQ&avtc=1&avte=2&avts=1714431776"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/leto-ne-vechno-1514554155/?asb2=4PckwDO6hAsgI0Sznz9Co_nNzMVe3VFUMuYhq9BQtsGXqLEYAxfug795kUX7MneNmmJkWSeIkmBPAMoXQFx9jw&avtc=1&avte=2&avts=1714431784"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kriminalnyy-talant-rodionov-stanislav-vasilevich-1456676674/?asb2=CyLq-H6flF1Kc7gp76Y-7ypegqqu4Q7seCzLqBQJkYdi2UFLGTXRl2dJH72PXK5tPkhjiQIe23UF48RUoY7Ekg&avtc=1&avte=2&avts=1714431794"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/monarhi-1558885719/?asb2=MhX_uGiKhMJXA52Kk2tltw92RTawcS5MuVEBQcojxobyfBhaeFVvX2r8qBeAE3vt8IFN5uk2ELgNPRSrSurKFA&avtc=1&avte=2&avts=1714431803"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/grokaem-algoritmy-iskusctvennogo-intellekta-harbans-rishal-1558981307/?asb2=M6-ED8Gg_SwoVpzQdW-1OW-9_l5Ev0JTGxjpQ4GJj1NKo0LIcoAreuJkXi7qiaAyEiGZkBIalvYHXdk4XkAyug&avtc=1&avte=2&avts=1714431812"
        elif product_name == "Детям и родителям":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/nabor-novogodnih-raskrasok-v-gostya-u-deda-moroza-491640903/?asb2=Cb5QcwFdasMV3VA6zP6bORmVf0uDY1dGrbeVAqEBm6jdTjBjxlBm-Vpppu2ktCEygtWIjDc7AoN91-wR5zrMoQ&avtc=1&avte=2&avts=1714431836"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/hudozhestvennaya-literatura-dlya-detey-komplekt-iz-3-knig-1-zolotoe-serdtse-2-gorod-schastya-3-1152185535/?asb2=ZpSwZ3pCncYMySBMp37I9klq4LVZiuNzf4z5y_VbupDfMmHtPuWI1eboVRCkeP0HdJIh6VuqbcnhAQ3ypgQUMY0q90CDKSkzNuqa9s7sAWMJkEOrX3Xtvj2lA1T9JYMu&avtc=1&avte=2&avts=1714431844"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/raskraska-igrushki-1523014650/?asb2=L_ftVl01CQCeSQhYN8Fw4M5ZC3t1jUwyyXgQjS88cMmOuI3ANEk31DUon5WlgpuKB5w8QkLB6hEmOBXBtv6gdA&avtc=1&avte=2&avts=1714431857"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/mama-i-dochki-synochki-putevoditel-po-neskuchnomu-detstvu-1545235883/?asb2=CcZSIBXSljXE5bh5SuT9H0YoMHMH_lHKv5br46BKapOT0ytjm-XwsJ5UsrRhFT77dW_-sIdreD8Na1FXNobSTw&avtc=1&avte=2&avts=1714431865"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/dva-tramvaya-10-ekz-708231720/?asb2=Os2RrYcgAZ0nqueooyjJ88660dSbuKyqtV4hxgZybJJPoEecVfhljxHNwEt6BWNMxsQpTIuBNWwmsjCcb_bImg&avtc=1&avte=2&avts=1714431873"
        elif product_name == "Учебная литература":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/tihomirova-n-okruzhayushchiy-mir-1-klass-testy-ch-1-pleshakov-tihomirova-elena-mihaylovna-1294990997/?asb2=-Dfm-sKsdNrAEWfxa8OX0Tdc0a24SXnYmRzzOs18JP_ulo2cM-s0LZuLhkOZAeqQoCCXvtOi6mk25T14mO2nvA&avtc=1&avte=2&avts=1714431898"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/teoriya-veroyatnostey-920970538/?asb2=rL44SFB8JOPxJsInuMEU3xtr_7MOhl3oecHDkVWrKY3qt61kAx6TIyRTgjKCFnWq&avtc=1&avte=2&avts=1714431909"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/introductory-chinese-listening-comprehension-audio-1307123862/?asb2=xN_ylJQVtk6EnN6rQPe2T2jIBkTIn6IoUJyehqQCDWDri_Uw2YVqn6YznoSe80CnA4PclDs1mcxdDbsmBZfMBg&avtc=1&avte=2&avts=1714431917"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/geografiya-zemlya-i-lyudi-7-klass-uchebnik-dlya-obshcheobrazovatelnyh-organizatsiy-v-treh-chastyah-1546385663/?asb2=j3xI_DCVWyuFtzGKsSufnTx4iyNYt41DYnZzJ20QFdGhkNc5BubBDCJG-vrjlRExp6u404cDq-b-CQUl5Vze_A&avtc=1&avte=2&avts=1714431926"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/how-to-teach-writing-harmer-jeremy-kniga-na-angliyskom-harmer-jeremy-1458585607/?asb2=umEkzSb_E06VPbLFXPSJn0RhzOfM_6YI_Y5WRtvBl9MVCDH6AZ5MpElH0tcHdhrBCRI0Dump8TMhbxJtoRlKHQ&avtc=1&avte=2&avts=1714431937"
        elif product_name == "Букинистика":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/parol-na-tot-svet-braun-karter-448639305/?asb2=V29Td0jFOrgk1awM6_rEceOsJgTN4e3K8nWikFSasnIZN4Z2SoSYA_kl3A1VXGLJd25bik743Y8H6OsVCFAsyA&avtc=1&avte=2&avts=1714431978"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/devid-gemmel-velikoe-zaklyatie-gemmel-devid-1462726763/?asb2=mvhY9YFRVmSjO0H-eeWHbqu3HAzR-3KXcbVoD24LyaRhyufdHSMy6fXRFh5CJVK3yDMVCYWE2U0gTCM1nuNvkg&avtc=1&avte=2&avts=1714431989"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/shahmatnaya-strategiya-polnyy-kurs-kalinichenko-nikolay-mihaylovich-1547928436/?asb2=h1rZKt_fcegY3sPOUcoRXAbShJ1ecsTmmKNAg5Xp6-K3bpUif9BP4u0j9Ap-6JBTJ2WnKKoYBDVuvvbnMknVUA&avtc=1&avte=2&avts=1714431998"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/r-fridman-parfyumeriya-i-kosmetika-pishcheprom-1968-1133693228/?asb2=VnvG4KLn4OD9uA_ASIzQVpdHkKl5cjh4E7JuGhPFKYcXMm1iSzNKJRYRDREYYpYPDqnGxQ7KbnQvsQ-09m3zQQ&avtc=1&avte=2&avts=1714432008"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/kuzner-bernard-rukovodstvo-po-srebrokuznechnomu-delu-1103377143/?asb2=izGtu7zXOhpjHaLKj2Uyl6Z-2jdMN6WFNqdTlWnuKfA6CSVeVqdKefTIpVvr_nb-IXR47q_f8W1wG9uE0vzG0Q&avtc=1&avte=2&avts=1714432015"
        elif product_name == "Научная литература":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/schitaem-i-reshaem-100-shagov-k-shkole-251014954/?asb2=I1ZjiPOt1UmR9nNk0k6iymXMcGM6VqoqbDKwkZG3GfHNCMgc4W_DDIHv-3G8OsRDtjfQC7dg9MugCyUjyiXCQw&avtc=1&avte=2&avts=1714432065"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/nauchnoe-tvorchestvo-metody-konstruirovaniya-novyh-idey-na-osnove-triz-mihaylov-valeriy-259684727/?asb2=hD4CKfWeietPiAjdQTiRlQbflzIngCbR03AG7IEKuIdCp99s9b5I_mlrOr9O3-FQeOR4ro8CK4Ga2ZcU48Hpwg&avtc=1&avte=2&avts=1714432073"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/psalmy-gimny-i-duhovnye-pesni-put-k-edinstvu-i-duhovnoy-zrelosti-1539225768/?asb2=MWIxlu2nXc6MNK8uAzrZe6YO5D5llkVjT3kr7WZP3xMfTeydvDHlDFWd-l_rlrDvtYjFA_dnhJSh0qCqtVC7ag&avtc=1&avte=2&avts=1714432083"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/rasteniya-ot-peshki-do-sekvoyi-1540629715/?asb2=nWnrr42ShGv3FTg6qwE6cwxi0rLOElVC1yLSo3jLirpVuP0fF2aILHtk6fCIe2JcIHQ-wgSVr6uqitn0No5cUA&avtc=1&avte=2&avts=1714432093"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/place-exclusion-and-mortgage-markets-aalbers-manuel-b-elektronnaya-kniga-936527517/?asb2=WI5qj-QQ-kwB6lDlbE84yQ_E00qWbkJodTU0JMu5u2Ei-OrieyhOpae6KvtQbIfAhE_GrTtrw1PPonR50iaTcw&avtc=1&avte=2&avts=1714432101"
        elif product_name == "Саморазвитие":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/lestnitsa-k-finansovoy-svobode-temchenko-maksim-elektronnaya-kniga-909664836/?asb2=09Nx-VHDg_YfdYaqtjAK-pFkhks9n83kjmkk3j0OIdusT9Wmw_vylWaOXdAV8aEB0_QHnUhMfI5GjcOIR4L2ig&avtc=1&avte=2&avts=1714432130"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/upravlenie-personalom-psihologicheskaya-otsenka-personala-2-e-izd-ispr-i-dop-uchebnoe-posobie-dlya-935334245/?asb2=f-BprQxRjjpOVmPaYIisnOYGt-WKsRST6IT1gU1SbHJEh4-p6tQo4Y72_dlAG_ts9LCXhCMyB5Yoaz0RyLuafw&avtc=1&avte=2&avts=1714432136"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kult-predkov-sila-nashey-krovi-o-chem-molchat-predki-sila-predkov-markova-nadezhda-1048283428/?asb2=s_zUosibSdFGbrTamNy2Tm6jp9YH38f5JMZBh4946EKCN8mq_p09e2wQy_HGI0j_LkEglfS2Czvtoix4X00I_A&avtc=1&avte=2&avts=1714432147"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/zakony-vliyaniya-kak-pobudit-lyudey-delat-to-chto-vam-nuzhno-vaynshenk-syuzan-1418930986/?asb2=yEuKRIIJZycEciF81rB9AqBjfvoKUvuRbm74MIIAcFWUL4ZohrMwRQK8wiBUgwtGCT6z_5pkSAfU7w8EQebh4g&avtc=1&avte=2&avts=1714432164"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/domostroy-drevnerusskaya-entsiklopediya-semeynoy-zhizni-1391160746/?asb2=DlE5XGdPX-v9alMdUKbKxiaFBubku2xyErg5ngM81W1owA5ybyWnf62UBMyLytk3JdRSnn1ONH_yP7e43OvwDA&avtc=1&avte=2&avts=1714432178"
        elif product_name == "Психология":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/pozabotsya-o-sebe-ch-2-universalnye-instrumenty-dlya-psihologicheskoy-samopomoshchi-dudin-vitaliy-909626754/?asb2=I5eHJyzr5FvrcASEtcQdWvzDNzRZmtAb7NyJyxGuUDNPuwsTyII4fmdbyrRpJE0REcHvdCccuj7-g-VEjy6msA&avtc=1&avte=2&avts=1714432208"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/biografii-fizicheskih-konstant-uvlekatelnye-rasskazy-ob-universalnyh-fizicheskih-380611511/?asb2=N2UbE4l-nPD1Be6eW8VOHOnfkO98sIKyVyjorDsNM3zid27OrdyGyU878kA0MPO6b_0wcUAarHmFktsgmV98_Q&avtc=1&avte=2&avts=1714432218"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/taktiki-disputa-kognitivno-povedencheskiy-podhod-1428427415/?asb2=BnKFlSo7LEUf2MFwuXuWoO9HOLbTzhTSai4eTqPKjK8JHaUNDV-f6-gky79Yi7q0mg1sTa30YAjZLZ9V6M__Iw&avtc=1&avte=2&avts=1714432228"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/cambridge-grammar-and-writing-skills-stage-1-learner-s-book-1552504364/?asb2=cwW-vGrPkYk0T8xLT8TvRzAANAuvXGUyhvp1YIsKfZK8az3AStSXGE0wMDxGPN3WQxJfA_i6G9PIEYNRynL1rA&avtc=1&avte=2&avts=1714432237"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/ivan-bunin-biograficheskiy-punktir-komplekt-iz-dvuh-tomov-1300195151/?asb2=hGXhiGPX-z5wzC-hZ3_udBvhER8TXOc7E9QpHHvRsqy_UF3bG3VN7PVLdbGL3Jmje9vrcmXaLbSEVDwi8avBaA&avtc=1&avte=2&avts=1714432249"
        elif product_name == "Искусство и культура":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/bolshaya-letnyaya-raskraska-saenko-irina-andreevna-elektronnaya-kniga-920661097/?asb2=Og4kWnUJmrxE_gbfHpcyS04I6TV-QF_y-pdKAQFIK0UU_Te9mOkyx4h80tVdwbU65-tdfh5gy0UOSZOrwg5sBA&avtc=1&avte=2&avts=1714432275"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/istoriya-drevnego-mira-nechaev-sergey-yurevich-1301507700/?asb2=1AB6ZDABTZIJjDXN1ru3WSocEcd1Va0pX_Zc1_lDfCflN6mr1CRliVYJHJSC5eO0quC7Fj3LkKC-_pjJCHKAog&avtc=1&avte=2&avts=1714432284"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/manga-osnovy-i-tehniki-dlya-nachinayushchih-m-pauell-805533951/?asb2=fdtjwmGpPzWNM49UKeFlPvPIoZk-6d7Opj6dKY199JR8SbHjYd8FRD4YzUxyvhlbHWo1pBKQpqARbapFgyeuqg&avtc=1&avte=2&avts=1714432291"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/istoriya-imperatorskih-armii-i-flota-yubileynoe-izdanie-komplekt-iz-2-knig-1553388657/?asb2=mEfuDqMjRKOXyan4BnmNKv6v8NuZxKcheifDjQrUNyskS0bqvX6RBfLDSiwqIVstH4GNmnOs0ICMEd_dQ3jg-g&avtc=1&avte=2&avts=1714432303"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/luka-dzhordano-vsemirnyy-muzey-1561915159/?asb2=-toWhuH0-Tem7PX4YUK1ovgPF81UIFtLsbBBcInW6vIjmDYFVE0ObAmdsg6PDoD0Mp7nluHZKAzAGDMHjXfhpg&avtc=1&avte=2&avts=1714432312"
        elif product_name == "Иностранная литература":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/qarqanta-v-pantaqrel-2-ci-kitab-rable-fransua-elektronnaya-audiokniga-917066492/?asb2=80nFhwcVCxorO4IZpxFc4cAS-giDD45bjrSQdV_7uINY9sOjQ8doDh7YEf1AmhEhdKgka4iZhBFD7R0Hu9dLMw&avtc=1&avte=2&avts=1714432333"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/sons-and-lovers-1314190649/?asb2=tj2wR2c4Fp6UHhUQeLAR4LMprbdbqBU6Tn7AZZXaizMlOXVLf4p0fd48-An6KBtFPfm9Qh6oCNRtKL3fAAsjew&avtc=1&avte=2&avts=1714432343"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/murder-in-mesopotamia-1239689217/?asb2=Wo6t49JMMDXU4vBigVHrCz49s9VRdfOzNi6SqYq40m-uqsa6G5HWYGPQx41fxbln6V1Fasf5IXU6F6HTHLDBAA&avtc=1&avte=2&avts=1714432351"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/greenfeast-spring-summer-slater-nigel-kniga-na-angliyskom-slater-nigel-1464317365/?asb2=tALWULRhHXefQKx_hfyMbHnlNU1xVKZHdXa0ovYcAZQ2YkrcLrkPyB7msG1vxczfoUqV7sVhOYNZqhMdRYXzcw&avtc=1&avte=2&avts=1714432359"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/the-10-principles-of-food-industry-sustainability-baldwin-cheryl-j-elektronnaya-kniga-986351100/?asb2=Ts5rCJIURtDJ01EmoYE6NM2SiBeTuj_leqHxkgQw3qKhpVFkRTZhF5GAJypsqvdudkd0uCdX5j-8P4tMsjjUyQ&avtc=1&avte=2&avts=1714432371"
        elif product_name == "Бизнес-литература":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/dnevnik-stoika-366-voprosov-k-sebe-holidey-rayan-hanselman-stiven-elektronnaya-kniga-935631796/?advert=yBPwlHUE7ZMM_1WL4LP3Avl84B6K1SuMrKDfLksCtbap3q4EoijSG5YfKqlUpB7oS1osVmqoeewvCV_wvv46Mm24yTxVLejHfwMx8vAZTuG2Kz7t_DzLs1783ByGHZa2TgxUZMkEDmoewtNdDO6ILoSXPycTjr1gJ7zG2Gp2wwciQDu5z22VuLm6S1kSLMAV5O7shSF0JPtPRylohDssYtLlmhg0fVQ3Ut576KbnlVBiH3tq9i-ygKO8y1xktLnEcEzD-Sju&avtc=1&avte=2&avts=1714432384"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/menedzhment-po-otraslyam-rabochaya-tetrad-dlya-studentov-obrazovatelnyh-uchrezhdeniy-1544163232/?asb2=obNtZor1el-Iq-zdh5UhPwjXEFBfTsmK7g0w26n4Ra--310opzQJFEh2n0_wYTGC2xMpXAOK5mTBH4nGI0Gsqg&avtc=1&avte=2&avts=1714432400"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/zhivi-kak-avtor-teoriya-i-praktika-storitellinga-dlya-sozdateley-kontenta-artem-starostin-1512094359/?asb2=j_7Bvx7YrbgGt7JHBrwmCiyTfLEyoJk0xXZI_r3e5mtICH5q07TAOulNHnHPR2q-lENUTViv17ecWWRWcefmyg&avtc=1&avte=2&avts=1714432413"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/ugrozy-ekonomicheskoy-bezopasnosti-i-ih-preduprezhdenie-uchebnoe-posobie-1539044786/?asb2=l9T3lwon4MJR8OY8c7maN8HOxhYWEZy7jL1FIq4Sfan-IDeDRAa7PuQu6_V8Btptyq2khsjQwXC-30TTmP-rUA&avtc=1&avte=2&avts=1714432426"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/servis-terminy-i-ponyatiya-slovar-1541888411/?asb2=yFZIHvR1q6GSeQRe1MUeidJQCs_zs4tOuCX32LsXW-M8MjncFvksrec80xv5MJX4dXENRrLSWjywXoGE6XWGxQ&avtc=1&avte=2&avts=1714432437"
    elif category == "Продукты питания":
        if product_name == "Макароны, крупы":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/bulgur-v-paketikah-dlya-varki-mistral-proparennyy-400-g-206384776/?asb2=kYpM0QOaIvNJb2YFOX16bEtNYQ3qt5-bguwzmQG3o0-BZryj8UGLJmYxDg7ZAKhN80vDOsA1Pq5KXocOYPv3bw&avtc=1&avte=2&avts=1714432998"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/mash-boby-mung-krupa-bobovaya-2kg-fasol-zelenaya-1001287308/?asb2=du_UWg-tuv-TqZzRPZKQZaTAgZya08AWVqqWEk1rWRXte0q03R88EHy8F-YJnQkV5mRNkVBo_53sRabuF84bGQ&avtc=1&avte=2&avts=1714433123"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/chechevitsa-arabskaya-natsional-krasnaya-450-g-6-sht-1480721998/?asb2=_Z5tLTrqN98OXXqmtZz8nUNscAoBTyN7Yn1tyv6sqX-MBkjjuGkWIblZMUmkigyelVRgms2wSGp8feDpCXZ6gF-kJXTqbhkdEuMJVPv1ZeXAaM8k2HttBz7TZ-fBGDp6&avtc=1&avte=2&avts=1714433134"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/makaronnye-izdeliya-3-glocken-gold-ei-landnudeln-fadennestchen-gnezda-komplekt-12-upakovok-po-500-g-696967592/?asb2=bwqVBHNrLTkH03QN-l6cuKXLgN7uyjdh3AmVKpeIBBmHbAGcLd9Nv6jTAMZo8oJl9nZXibgOw-aX_1hW98NEWg&avtc=1&avte=2&avts=1714433145"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/makaronnye-izdeliya-pietro-coricelli-spaghetti-500-g-1484463957/?asb2=Xbz3W_g52wBibUcj9zz51jpxEA5R62wjD5TdByGgcskxkEXUdsTy1UgzR4gKHaqOZomZZ24GW3Pz63aBugbziw&avtc=1&avte=2&avts=1714433159"
        elif product_name == "Чай, кофе, какао":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/chabrets-chay-30-gr-729127761/?asb2=i_1jmng3svUN4MeTaabDm6lBBwCFKZ5yYlqnrnMJ_gK2bTi_QA1wmwhNeMtaNHSQk2Yl2SKS5s8HhvEnbT61Vg&avtc=1&avte=2&avts=1714433190"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/kapuchino-klassicheskiy-santino-1-kg-851593056/?asb2=WuBZjonpfKS_CoFrIp0rjKQ5r0ElK69KHjXKcX8WU-LGe3QPtcXplfJgvqRdZ6hWczL2mT6fZEi6EVWcUPeeLQ&avtc=1&avte=2&avts=1714433198"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kofe-v-zernah-piazza-del-caffe-crema-vellutata-1000-gr-1124744735/?asb2=VZlcC0_Vl5vzqch5BWW7nfaHbFw0r_aXs2ei1s4chvlBM5hwqm2TbpJ3zjKNButrCiBBRgmtXrIaLUaDvmMR7Q&avtc=1&avte=4&avts=1714433205"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/yunnanskiy-chernyy-chay-dyan-hun-syao-hun-ta-byuti-krasnyy-chay-1000-g-1483112863/?asb2=VQTq773bLXbRRfFV0bmfVjPrWXgux4QV4bCMolSpOq0zKzc5EbP_VcLSqzqzdaddxfNekEWx7Gu_TL7U-0D2sA&avtc=1&avte=2&avts=1714433212"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/kofe-kimbo-integrity-bio-v-zernah-1-kg-komplekt-3-upakovki-po-1-kg-661353749/?asb2=Q-I11a-gVYQ2cWsDiwGhz4yq60lBSUGjNvMThg1wZXyAZB7UxluPFomaUFPi0fI-EHs6Wn3jC5szpDnh2c84AQ&avtc=1&avte=2&avts=1714433224"
        elif product_name == "Выпечка и сладости":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/konfety-shokoladnye-slavyanka-levushka-s-myagkoy-karamelyu-199-g-143932917/?asb2=oR9z7FzR4rWURAafapbPJK3sy9Bz3Kj2PjQsp9CAQLaQOb7Ll_s8hkBTtdhvAFmDRto6SFua_EUYMbkRfJqN_w&avtc=2&avte=1&avts=1714433243&ectx=1&miniapp=supermarket"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/marmelad-zhevatelnyy-gigantskiy-vinograd-damel-300-g-1054188898/?asb2=yknLl7H1aZASv3BmNdAQehiBVdTI_Apv15b4W44k8rYBb7gqpE-rrFBxsZKIjfVtrTMxum5ZHf9h0kB6kb0DxQ&avtc=1&avte=2&avts=1714433253"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/nabor-batonchikov-fruktovo-orehovyy-marakuyya-gretskiy-oreh-10-sht-po-50-g-1160111886/?asb2=IujHgasUb5in1oDlw43XCr0d-SYEXPTQm1ZmPxjd_3xXKW97hv1149YA0msiIUsawmUiS1jpRUYsFinzS-q-5w&avtc=1&avte=2&avts=1714433262"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/shokoladnoe-yaytso-zaini-smurfiki-s-syurprizom-blok-24sht-bez-glyutena-20g-24shtuki-1349975150/?asb2=iHKaDX34RYeHi1ljAoyTODv1qK0pkGh0GVnCMu8CokRuWsKrd0zV8sB_pv68NVAfJm9I5laRIV9edvyF0PaaEw&avtc=1&avte=2&avts=1714433273"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/shokoladnye-konfety-lindt-lindor-coconut-s-kokosovoy-nachinkoy-v-pakete-1-kg-germaniya-1506148157/?asb2=KO69ufnZPdXegg1_U1AYJcDlfBR7L1Unp_PseIBMr0qCF7GYDvbgEeldbPppIGDpm580swbP4nAAWDg0MNQaVQ&avtc=1&avte=2&avts=1714433287"
        elif product_name == "Соки, воды, напитки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/napitok-star-bar-bitter-grapefruit-silnogazirovannyy-1-l-sladkaya-gazirovannaya-voda-gazirovka-818097170/?asb2=xKHTB97wIbbEDLQ9An7RLF2K8lhfFmYn2E2T0kRlAjosrEJw2lbI3sWmbBdzM_pzSbJ-3WeAuvb0fW7A8Id0cw&avtc=2&avte=1&avts=1714433322"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/mineralnaya-voda-essentuki-17-1-0-l-6-sht-175806652/?asb2=fGxm5Ipqfr9vsRuThKyL4-c5LE-qSmug4YvaKQh0FVUKdDWnF_m93qV1hhjnGqsAxREnKnc82875c1xXth3HfQ&avtc=1&avte=4&avts=1714433336"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/napitok-ascania-grusha-0-5-l-6-sht-631137501/?asb2=v4URI0KNsYDrs36B9aa2fulli6mPxM9oBdPalR4jsbuzT2vcY2avPtUFUToE_0rJJWVRP65XbvzdC5UGN6N_nw&avtc=1&avte=1&avts=1714433345"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/energeticheskiy-napitok-red-bull-red-bull-zh-banka-0-355-l-24-shtuk-1284400842/?asb2=dXd6U4fwpzDfD49aCt4orlX9fz5FDMnIgO2-ECviXd0f3cNKTzkCLmACYaWGtjSwhR0ZOTJQAamoTph_LwtRBA&avtc=1&avte=2&avts=1714433354"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/energeticheskiy-napitok-red-bull-473-ml-h-48-sht-1231518125/?asb2=ZGXV91To7JGuUId8jMKgIXZjRNf-_hqP3A3t0OyVddqsHQq3ZT3W6OC2El4pAzRwIBFK6SCJCy8pGBCn1cGbjg&avtc=1&avte=2&avts=1714433364"
        elif product_name == "Орехи, снеки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/chipsy-fruktovye-yablokov-iz-kislo-sladkih-yablok-25-g-137511395/?asb2=RQ9hkGiD2EjyqeqPrRHrDHN19zfQ-gfW5DK3h7QTMRywd0gcp7h2AqEPNcrWXRTubem6-LKeF47aZJLP-tjNSw&avtc=2&avte=1&avts=1714433407&ectx=1&miniapp=supermarket"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/nut-zharenyy-solenyy-uzbekskiy-1-kg-1000-g-1008745866/?asb2=m2CZHs1nx4JbCDKbCdeJU_pznHtoEyobzVd1kS1MmKWFc0805r_7YcnY95WDaKlO5VGr3F2snDflc2I2rLuTXg&avtc=1&avte=2&avts=1714433416"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/kuraga-gornaya-2kg-1545332536/?asb2=BpDShf12k7aOqwGP8udkv1ThUPK30enY6Qx_6CjU7AB_IGDCrxC3nZraB1x-OnD80UzrXTlkPPKBlFHppwfpJw&avtc=1&avte=2&avts=1714433424"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/chipsy-pringls-ostryy-kartofel-110-gramm-pringles-110-g-upakovka-20sht-909816444/?asb2=7yRkp_yPnj1PubgWvsDDkWMtZL7_z5vqKapiidNPww1AwbKi0YKzI9jgkCqF9u7yKKduLQI0HqgronTphd1aDQ&avtc=1&avte=2&avts=1714433431"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/orehi-grand-master-kedrovye-600g-h-3sht-1496237232/?asb2=nLFpFCVtldYnB4ghBLPecIO4g9gR-thcfT22Qk0QNeQ6BuoO2oZpV8a_a4hxwT4rd7ticPIDYka1jRnEeBaqDw&avtc=1&avte=2&avts=1714433440"
    elif category == "Мебель":
        if product_name == "Мебель для хранения":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/torgovyy-dom-vishera-polka-nastennaya-uglovaya-25h25h1-6-sm-1-sht-616689135/?asb2=N1EhLaDv8YjrHRn2InSQ8nYDtpkN5v4LAUuLSIdDt1Fp13Cpx8tn0J0wEglCc3Wg6fMoUkta2MG-ES5skogL-Q&avtc=1&avte=2&avts=1714433616"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/detal-dlya-mebeli-ldsp-shchit-polka-16-mm-320-580-s-kromkoy-vishnya-1sht-bez-krepleniy-1505657956/?asb2=OVbwDYoaqYVnDHrBlztUDgtZWeKLKM-sEu38ZIw5lvzJgcpFIXTPZy8euuP7fUnQLLHs7uYrdC0BmDcsAGBYmg&avtc=1&avte=2&avts=1714433629"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/detal-dlya-mebeli-ldsp-shchit-polka-16-mm-440-820-s-kromkoy-dub-amberg-1sht-bez-krepleniy-1505665291/?asb2=wrTNrrwh_SAtxxhP2MSVcId_0MV_KEqRvIuJeiaOIso5TMiJi95cLBLo7eE6GO5Q8p7jmMTJ4iZgEi3h1033Hg&avtc=1&avte=2&avts=1714433639"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/tumba-hanna-chernaya-zheltaya-703913900/?asb2=MKWzV5Lhb1ZtXOXTJ-WdkMlblhwQAIgiFiog5wc0BnZTImgzuuw5vo24ykLiDjw92FLLpvTNrh6jQyv4L3xULA&avtc=1&avte=2&avts=1714433648"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/raspashnoy-shkaf-dlya-odezhdy-reymi-so-shtangoy-s-polkami-s-yashchikami-160h55h200-sm-belyy-1554881691/?asb=maKFVB5QMDMbbx%252BTltIjPVtyKCQoo%252BPSOLMtInyBOEY%253D&asb2=eM0wH4sbz2qG4objeditYD6lPK75THj45nTzZ1H6wNGRHiw93k3q6SBRih-oJdnuICTl3FfBLTRxRZrNl_VF-A&avtc=1&avte=2&avts=1714433660"
        elif product_name == "Столы и стулья":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/karkas-tabureta-stula-domside-kryshka-400-1-sht-813537289/?asb2=kIYSlKsmBk6lFnyF2QRIzvl93Qcar68-9BL9buigVk6kOLPgLissGzgk2k1Fc2Kq&avtc=1&avte=2&avts=1714433677"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/skladnoy-stul-1561447295/?asb2=KsD0nykSzBypA6IyUKWZX0BoEQ0ZZ9C1mc7rk1uZuzxuV6hCdq--qao1bNjusXAbccMXtCWGicNMdL5-vdNbkA&avtc=1&avte=2&avts=1714433689"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/taburet-kuhonnyy-sidene-106gra-grafitovyy-nozhki-podbirayutsya-otdelno-1562195386/?asb2=aOJL8BnEsNIA11Yw5mFisP9-Rr5ndfRymd1uUTExuzTOcAP_vwivzIBWeaSTasNLEakC-PwJT0frtolaFuxLoA&avtc=1&avte=2&avts=1714433708"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/taburet-1-sht-1561709814/?asb2=P6fUAXqjhwju2hIS7ySKtqujrrGNzAHucf6ASAH5lOuKR11dgWZzzLhXcWm5rTUZ0VkBRIIoiRzSfTiYROrGyQ&avtc=1&avte=2&avts=1714433722"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/stul-1-sht-1468924420/?asb2=edFYN4nB7IRSIwWjuoNgWmFI6mduTdFhELC9nLol_Zq36gVG-ihPwuLSAlINlcQuXtSWOlnhW5SgkoJ2e3do_Q&avtc=1&avte=2&avts=1714433732"
        elif product_name == "Мебель для спальни":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/zerkalnye-vstavki-dlya-stenovyh-paneley-izgolove-dlya-krovati-tsvet-zolotoy-2-60-sm-komplekt-2-sht-1200789509/?asb2=1N-SzF_vGly2ma0nFlPEX3Ljbc9QdADjGEGiE9-4UME9JzpydbGQQWZS4LL3w14M&avtc=1&avte=2&avts=1714433757"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/namatrasnik-dimaks-akvastop-90x200x18-992233257/?asb2=DCANJbM50-BTsFFOLak9oykWIexNlky4yPSAZ4SYXWfSHMh6m7iuF7QLEnhMvzI5&avtc=1&avte=2&avts=1714433780"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/matras-matras-70h200h5sm-bespruzhinnyy-70h200-sm-1077858349/?asb2=U31qRkcjJ0CSVmsga4p8s8_oOgOgkCKVL2oiOa_Dc6MW9x88xw896rF_tC_LSeko&avtc=1&avte=2&avts=1714433788"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/matras-ikea-ikea-asvang-bespruzhinnyy-80h200-sm-688758656/?asb2=FWTeMzDGe4stJnkYHfU5IbyCW1AgAxeJrOYPZMpJDzv_Pas7vUjK1DNvxpBgRW16GHtObbDl_oQ_LRFh2HRnVQ&avtc=1&avte=2&avts=1714433795"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/matras-kumir-nezavisimye-pruzhiny-70h190-sm-1523180414/?asb2=gOgZICRSkPWO4-YrnQWrKEIvK-krByl2uzMKvCf1iF8qLWri0LSxMP0RlXrLpp5bFeJvXAMgVihwykFj5wBqeA&avtc=1&avte=2&avts=1714433803"
        elif product_name == "Мягкая мебель":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/podpyatnik-voylochnyy-d-40-mm-11-sht-tsvet-korichnevyy-958572984/?asb2=sDD-NNksIeRhvUJ-lhNFu7DlVmhF5mSa6H9XklJYpgjgjtvfhd_LzHtFSklvp78f&avtc=1&avte=2&avts=1714433824"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/puf-skladnoy-s-otdeleniem-dlya-hraneniya-volshebnaya-strana-puff-kot-30-30-30-sm-820041290/?asb2=9aSwUQD0aFEOT-eLieMp3kP3CblJJlUKxSHNYPKz33PjfvHMzQ8lM1wolY8ct3OPGG5OLBB-bsSzR5NNJT5E6Q&avtc=1&avte=2&avts=1714433835"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/komplekt-myagkoy-mebeli-1557861622/?asb2=0K3HhpAotVdWb3v4i9RP2kkUzR8PpB79b2ATZWpGXyCVIkBxNlZuxtUDddFg-hlzkXuwzk3f-c1rZfnGk-aI3A&avtc=1&avte=2&avts=1714433843"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/banketka-bn-17ks-ekokozha-iskusstvennaya-kozha-50h30h49-sm-651533315/?asb2=PYzYuDQoOupLydmmgmnnOejT4lb08h5Q6u17_biebsyb9GZtnCw_a6FUCW10oh3EmulJ70gqBgE-RcZl76eJtg&avtc=1&avte=2&avts=1714433851"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/kreslo-kachalka-60h96-5h100-sm-1481458980/?asb2=XFfVb1bJg98700MzSC9pcAN9kcQ5YSF-8P2o2CYNriqPjO32e773dcb7T1vzkTnhttvbh3kvlw9LlOUwZ5C27Q&avtc=1&avte=2&avts=1714433859"
        elif product_name == "Компьютерная мебель":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/zamok-lock-138-cr-pryamougolnyy-hrom-d19x22-889648052/?asb2=PTwuAeKm2cVH2bX4nfFZTe3npEsZyAqmrTv1HcDhg8yiHnMaFGLHEgYn26LpLa_9&avtc=1&avte=2&avts=1714433872"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/kreslov-podstavka-pod-nogi-detskaya-13h34-5h8-sm-1212770252/?asb2=Qsse6EXr-yTGxPPEZbE7JQF8hPVGvidPh3Vn8OWYdS0gr54FmTHyYURay5I8vBtsrj8BHRl3ZU6hDSm72m8qCQ&avtc=1&avte=2&avts=1714433880"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/stolik-podstavka-dlya-noutbuka-70h30h270-sm-1526233617/?asb2=qWha_zt8ECPdDaMYKwLWdp54rSXrKJpaTQZMlz_3OjmpqQ_gIgH9lAV0OSPoTokGG7PwQL33eGzgTHQpOYGF4A&avtc=1&avte=2&avts=1714433888"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/ofisnyy-stul-abs-plastik-iskusstvennaya-zamsha-belyy-i-seryy-1453403744/?asb2=vA-xBxRkvPQsD8ldGpgH6dr8JxxeK5XawxiIQC5dCelnZ7559ksuhfXxExNdSzXCnF_vi_ysUVJGGJ5mbxYT7A&avtc=1&avte=2&avts=1714433896"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/veysay-ofisnoe-kreslo-belaya-rama-i-chernaya-setka-nelzya-raskachivatsya-vpered-i-nazad-1480153578/?asb2=op44fHTyb4Q9XWvav74AAOz47OMRuRpGN820Daoe5yMAfinktMuafcetdKUf7yh5Wlupq-TTFcI2fnCWF_r8Ww&avtc=1&avte=2&avts=1714433904"
        elif product_name == "Мебель для ванной":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/generic-uglovoe-zerkalo-dlya-vannoy-1467414209/?asb2=u5ecE1kq6UOUZMqbWVhVaEqED-7PAdrIEmQenB-2-IZXZMkVoPhhDIKbCOfkNnDH&avtc=1&avte=2&avts=1714433925"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/polochka-dlya-masel-6-puzyrkov-24h11sm-lipa-dobroparov-1024870703/?asb2=G41DMtVi_lyV2AfHX73z8KyDr41K7tQXoqaFZ1bCkTTZJfm4LlMCmit6ZHXWoemN37yKUQ8RyKEsg4pZvqWhLg&avtc=1&avte=2&avts=1714433934"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/shkaf-navesnoy-dlya-vannoy-13h10h28-5-sm-universalnyy-1559449164/?asb2=hD85Ej2YJ6UxBNFJvjyfYzOKQ0WRfTQ54KL0deB5NCSvyuEbbXU_e2Za_ziFTdkdwqiHekm5p5vQmp2VFgVcug&avtc=1&avte=2&avts=1714433947"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/derossa-zerkalo-shkaf-shkaf-zerkalnyy-metida-60-60h14h68-5-sm-675761122/?asb2=fUd1eBxPjKQAJMEmYQwUwSwwBLtCba2cUGFwJVPPfCAGtw8tTdeL_dQOrOJd2lTfpA19LT7cklfgLpvNBlijOw&avtc=1&avte=2&avts=1714433955"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/tutsi-tumba-pod-rakovinu-55h30-4h85-sm-373564199/?asb2=hvR65BDszEWqyEYJRpR3yR6N-FYVC3AiRh53_ENMADLUfjVamHO_knSEfN0-6gYRAjJFxiQsKQ3QnUDY-a7tlA&avtc=1&avte=2&avts=1714433964"
        elif product_name == "Мебель для кухни":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/fasad-kuhonnyy-dlya-mebelnyh-moduley-140-h-296-iz-sosny-1518563779/?asb2=CsJzivRhI22BKofcpCfhYJav9xTYY0SYDoDPZHts0V7CKShdgB8IExDIXH2Q7D1J&avtc=1&avte=2&avts=1714433979"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/plintus-dlya-stoleshnitsy-120-sm-komplekt-zaglushek-tsvet-kanadskiy-dub-840055666/?asb2=SHGwvl2nwsB-8vNzCZcquDYurnfM4uWxnXSqHyo-JROt7OwmQh0EOmT6REJ6xtW9xHZcgGvJHAywzIOJbDNdYA&avtc=1&avte=2&avts=1714433988"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/stoleshnitsa-ldsp-900h450-16mm-tsvet-belyy-1553984440/?asb2=fNcQQenh0n-rl2oEkVSoOAq6q9vSOoxDfGuOelgeXRMpfixbgjOQrX6XBjpevn3J0eBc7NMyDORFqJ4FCDRnRg&avtc=1&avte=2&avts=1714433999"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/polka-dlya-kuhonnoy-mebeli-napolnaya-pryamaya-50h18h96-sm-1-sht-1493740465/?asb2=DZWfJ2MdqL0_sOpIaUB9t6VqDu4X_Gt4P6CpKpcbF3TqFKQPH7GmHLDLwo0ihSlDRfm7Zjx7K-UIYvuMQwQk3w&avtc=1&avte=2&avts=1714434006/"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/stoleshnitsa-iz-massiva-dereva-listvennitsa-srashchennaya-bez-suchkov-sort-av-1000-600-40-1251741888/?asb2=Elm0vuYzbvzmCEUHNQJjX579vU6Y46rg4d7h0rqyITtiVyIbul3_XSfw6CiTdyH7qoKuQtvnjUExrkLQVvvaLw&avtc=1&avte=2&avts=1714434013"
        elif product_name == "Мебель для бизнеса":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/zamok-vreznoy-allyur-602-a-107-vitrinnyy-140-mm-1485-1432593730/?asb2=TLqCpTtj4ikbHq-OpmojihgzKOMZTDgJ_afS7sFldNepj3MSALbb0huIpcOfo6i3&avtc=1&avte=2&avts=1714434027"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/plakat-maketa-stopy-i-lodyzhki-dlya-kabineta-pedikyura-i-podologa-v-formate-a1-84-h-60-sm-297585809/?asb2=tzrwQlN3LZMjRwUcfL36xS6EjBy2GmwnhHOR5lB-zjzGzmYqf8moSL3UM5nCTaIo&avtc=1&avte=2&avts=1714434035"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/flangerio-polka-proizvodstvennaya-25h25h25sm-1378407916/?asb2=nkatoVazrrBYAzH0zLlMQCxp-_3ZikaEiAzBK6ad3Jaj-xu8Zl1OUcXoQ7rYMIGxfTAIYrXip1nXr-q6JjpicQ&avtc=1&avte=2&avts=1714434044"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/kushetka-kosmetologa-cosmotec-kosmetik-180h60-belaya-utsenennyy-tovar-1039162583/?asb2=LyEPSbmkhSjgxMnABFD0K_qshiiGVLrwNp1MEalaKNh9iU-sVPkOYTI88HERagbtO_qMD6sDnlIZrtL3uON4Mw&avtc=1&avte=2&avts=1714434054"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/tehnologii-yuga-stol-proizvodstvennyy-120h60h87sm-1504377379/?asb2=SzCPmCe2qacJ3BqWLSxf-xbtfxhfPI60sXYMlP-aNRPNyURe98vhmH2G8yLJf0RrGpQT4Hx9JqFvggdzylY0kw&avtc=1&avte=2&avts=1714434064"
        elif product_name == "Садовая мебель":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/furnitura-dlya-sadovoy-mebeli-1458386500/?asb2=pJf11NM7Ex3_lYkxBM9eBgi2rzvaW1dOxEzfC6Bf8BVYPM7WnlRP-ZYeCyeCQ04I&avtc=1&avte=2&avts=1714434079"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/nueayms-furnitura-dlya-sadovoy-mebeli-1533174802/?asb2=PfU1qSTU06C1eTxELeLhWi3quuuGoV3hy75LOt8ypdoFOFZYOtcT79GBjV-ddjGdrfX4BBqJ9w4qql1nK_-BHQ&avtc=1&avte=2&avts=1714434088"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/nueayms-furnitura-dlya-sadovoy-mebeli-1533177126/?asb2=y3dC9GS0WF2Ua9DEsArROK59MzMw5qt-2xTfvp5QsWATzhKkHEkn4q6N80nHq93hxAN3Ez35h6PaLE722Kn4Aw&avtc=1&avte=2&avts=1714434097"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/sidene-dlya-kacheley-60h120sm-1552118917/?asb2=r6hFMEFGID4QI1JW2kRf4XkojNiQFQsZC1HWij2gXMZyxlxMl4T6gSLskbExkIU5_GImveyXlvAs9aTjaD60Uw&avtc=1&avte=2&avts=1714434105"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/sadovyy-stul-abs-plastik-metall-29h49-sm-1512927498/?asb2=N5Da6scSBmtT91l2T8fkRG6q0GoCEGcbHyq-gcbFgaIL_UmrWY3M1auDYrGsvd_6l6nBtSk-lRvO7S2F-5OiTg&avtc=1&avte=2&avts=1714434116"
        elif product_name == "Детская мебель":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/divan-yashchik-dlya-igrushek-1523936995/?asb2=FHr1vR4O4SQxDsQevSy3DFHA9EZTT-_5DY1B_AmGwMHIjuLmCEQ-VOR4SF5kHbXh&avtc=1&avte=2&avts=1714434134"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/divan-yashchik-dlya-igrushek-1535232938/?asb2=bhxGYJqaC1owcf8NiMRGCPFnLz6B63nB4Iw9qxvmgCG09d-5DPZDTSNjwc5_ETOMh22tFHB-R8I6PsX0lxH4Kg&avtc=1&avte=2&avts=1714434144"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/stulchik-podstavka-30h35h25sm-1516684330/?asb2=72ksvT4VJDeX8oZarf_eHqluj_HuxBOUgCgjgGajXs5EuPCCp2gtGq1HhNyl5wSjvCgQVLjTPy0qFKhlv-DPag&avtc=1&avte=2&avts=1714434151"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/yashchik-dlya-igrushek-dlina-30-5-sm-shirina-23-sm-vysota32-5-sm-sektsii-1-sht-1556582639/?asb2=ofm6VoPCaDPMDEGdYgi4yQ3xQV7tmyo9An465e0K76-uNWqR3vIJPMBCWx8DMeAfafIlkc9U8OrSWJ7zbS3y-Q&avtc=1&avte=2&avts=1714434160"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/komod-pelenalnyy-800-4-lilu-5-belyy-483422948/?asb2=lUaP5luIuZ4I9WdyVah6nm46ScXtIEhSSfB6cFQGMI6EhSlnOcD3sp2fSyXOk8vTdJN4412cRUbhYSIJMNTmNw&avtc=1&avte=4&avts=1714434171"
        elif product_name == "Бескаркасная мебель":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/napolnitel-dlya-kresla-meshka-polistirol-penoplast-30-l-1422661792/?asb2=BZADY-mMeCrDoO8V7Xz_pV9DqWBf_0Eb9kwdv1vTGxJSbcM9MJHNwuScTtNR83VZ&avtc=1&avte=2&avts=1714434189"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/chehol-dlya-kresla-meshka-puf-pufik-pod-nogi-pufon-korichnevyy-726269052/?asb2=CPSCcHw8TVyUgjxY-CAtr9ZWzGYKgqklYJTCvt7xdsF2elGbKBkQcyGHTIBUwQSMzwXs8kaS_5V05nMZETqz5g&avtc=1&avte=1&avts=1714434198"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/puffberi-komplekt-chehlov-dlya-kresla-meshka-pufik-oksford-razmer-l-260219533/?asb2=b7kzPBtufXxzIcaWEYHrcwbu1vlJV90rAr_J12CmyP7wKkQML9reNjHLmAEwb7KkDxrA7iHoPAoh5ktkqj2ifw&avtc=1&avte=4&avts=1714434207"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/kreslo-meshok-len-razmer-xxxxl-svetlo-rozovyy-1486057306/?asb2=gB5zs52gj4vRyHDwg5I8D6f5-k6aq6sVNSgYHGtBVhnzhmdpHCqVmzzIOG85vDw9nYKDv3HydWZrxcOLhp3mMA&avtc=1&avte=2&avts=1714434216"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/beskarkasnyy-puf-tkan-razmer-s-1500120824/?asb2=RymBOwMGb9tCtMpkamTi8XKEjIrO7bLuL5AFdJcHoii9SvA7tH02PwmY4EiKVR6EGQoYPzek65Q9bNiFJJwEgQ&avtc=1&avte=2&avts=1714434227"
    elif category == "Канцелярские товары":
        if product_name == "Рюкзаки, ранцы, сумки":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/sumka-meshok-dlya-obuvi-1343265896/?asb2=hWfSyHT7q5y3tOiCIrCHm1NPDPo939whMnT6rUIOoHy8AGkWl79ozhTpHtQ23CoMN_gjUUzuEQ6kABfrZYPv1g&avtc=1&avte=2&avts=1714434513"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/meshok-dlya-obuvi-otdel-na-shnurke-svetootrazhayushchaya-polosa-tsvet-biryuzovyy-1544477915/?asb2=RqJPHAfWic3x37PQoSALfPrKm77O2yfmAQZmJC7cjmODawm_VXonz6M_FYt7jKROPQBG7cCSsQ8vH3rqd3f_KQ&avtc=1&avte=2&avts=1714434523"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/ranets-shkolnyy-1544200215/?asb2=n7p9MK9pXqwWxfmjSidV8GzdJJklSTwQvfICmZ36xeWArsIeViRIi-SHPMjoPP7gWWVEkazAd69SyccRmza5jQ&avtc=1&avte=2&avts=1714434533"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/kuromi-kuromi-sumka-shkolnaya-svetlo-rozovyy-1535563833/?asb2=LSZHf6XFXHAMvldHPAQAcaZgBaMxuzvP_61zKp55GZI_c13qr8eiJ9-FpyZIbHKykxL6pbBvVTWt3fe6K1rAnQ&avtc=1&avte=2&avts=1714434541"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/ryukzak-muzhskoy-hatsune-miku-ryukzak-zhenskiy-1537009836/?asb2=HAprOFIY_Lrq96RDT3QG4968sUJkdCzSETLZpIWcBuckDMeaEyjbpCYiO70ugNkm5oPsmQBGSCn8rApGhINaXw&avtc=1&avte=2&avts=1714434550"
        elif product_name == "Тетради, дневники, блокноты":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/tetrad-hatber-48l-a5f-liniya-na-skobe-oblozhka-iz-bumvinil-metallic-fioletovaya-799530010/?asb2=PzJ1IY9IjfcYyjDMwZvlL2gV0APmrTc1mOvgnvK4Gjz55AWo9ZVdZ5Sd11Hinh4-L00HTFp-QKDY5dBeqklGqA&avtc=1&avte=2&avts=1714434567"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/calligrata-dnevnik-dlya-muzykalnoy-shkoly-muzyka-abstraktsiya-integralnaya-gibkaya-oblozhka-1028416566/?asb2=FVQU9-vNbBUyYDTb0oovFiLOPiKQjblNWH3oOTiir8yBgjeoetbfD_whz9rKF8nfxaua66LGlbE4pcFCN8LbWQ&avtc=1&avte=2&avts=1714434589"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/artfox-bloknot-1552597618/?asb2=9wgU4ZEgmevlOQcxLjwC7ErElv8f-BVcXgOlVj1awdE5mDJiCBRU30WeniGhALyoR0wQHDzlu0dEMSThrsWZEA&avtc=1&avte=2&avts=1714434598"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/tetrad-puteshestvennika-zigzag-171493399/?asb2=N6HSHlwbOc4vjQ305YK0dY0ywZ7j6-HmblSe9mJV809KLyWMj8Qjq61_Nw1qcetgEn3qOR814xIxxSImDdrmig&avtc=1&avte=2&avts=1714434607"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/bloknot-a5-14-8-21-sm-listov-96-1413897398/?asb2=qjSi1RDC9qIQyF04I3IyBb78Q4e3YP4tLRnqKwX9jkn24Bb-9t5abskCihus6oKxwWdebHOPcpHk9IiXJ5FvOw&avtc=1&avte=2&avts=1714434615"
        elif product_name == "Письменные принадлежности":
            if price_range == "100-500":
                url = "https://example.com/catalog/board_games_100_500/"
            elif price_range == "500-1000":
                url = "https://example.com/catalog/board_games_500_1000/"
            elif price_range == "1000-5000":
                url = "https://example.com/catalog/board_games_1000_5000/"
            elif price_range == "5000-10000":
                url = "https://example.com/catalog/board_games_1000_5000/"
            elif price_range == "10000-100000":
                url = "https://example.com/catalog/board_games_1000_5000/"
        elif product_name == "Канцелярские принадлежности":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/ruchki-dlya-shkoly-gelevye-chernye-nabor-ruchek-dlya-oge-ege-i-vpr-12-shtuk-komplekt-dlya-ofisa-318672871/?asb=Ly%252Bo7KkNeDOaIwKnQxMWGh%252FLSHuhnRyqrzZe%252Bwcl8%252F%252BpEh234kEItaoaWeDeNmh1&asb2=4LHX_xh7T3GZcITRtejeA1nRiCBjfUMUlKE9De76eMGF47yiJUq6mFfTJfwf75sGV3PFqmJ-_TkqWFoU8HCq7C5qdcS6dt3rhlAYnUI2KIMQm_epDRykiUeZ2RZKVKuj3xLDX3nsGVduJfV8nCfT5BR9O99s3bPm9w5gbqrlHz43ZwJNTllwzgRQgNEHZKxd&avtc=1&avte=2&avts=1714434664"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/flomastery-nab-12tsvcarioca-joy-40614-1-sht-1363057715/?asb2=DpZsAWc3ufTCDVJgtJ3S7q-lTRqFhVtAysuM4m3lWkmgRXYoHHV4nQEcQVBoY6vMEMlPXEM0oucvzH8krAq4xw&avtc=1&avte=4&avts=1714434679"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/asmar-marker-24-sht-1545114908/?asb2=lf_JfyQFfZoKPU80EeBcQJZI2hLSUNvCJrNbzzSSHcquEZ4MjikJd8bbpMLOEbzY3Q-ohRQNvOGJ5oSreGIhmw&avtc=1&avte=2&avts=1714434688"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/parker-ruchka-tolshchina-linii-0-5-mm-tsvet-chernyy-1-sht-1535655879/?asb2=j5Lmdfxe7MNIaW3EX4q6ywIMFga9FmomKg206mBTXYTiVztEiolJHQhevwx4Uw8JapCkZKbNoAQDoPbVLVyWkQ&avtc=1&avte=2&avts=1714434700"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/nabor-gelevyh-ruchek-crown-hi-jell-0-35mm-3sht-60-up-hjr-500set-3-ep-547825384/?asb2=cQKHBnMULn77EE808c-4KVtz37vbMnMwIQOJAqMIkINI3L2Ym28EV-TRikk2l30esczI06AWmPJwpgL8F4cTPw&avtc=1&avte=2&avts=1714434709"
        elif product_name == "Творчество в школе":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/melki-tsvetnye-dlya-asfalta-multi-pulti-enot-v-avstralii-25sht-5tsv-plastikovoe-vedro-796460543/?advert=p5hsrVtg_JIVgJri6CTFR6ob0Rc4xaKImjzJMojaGGRQCygPOgoDRiggRv26SMJu11kdZrIrlPBqH_7osbkXO5XT_ZmWQ4di4gEfTGPalOCkbkWWQ1oTr31nhmMklb4hFHobj0JVz2VSI4MjveV1BVxo4jZRN3Ahy6_rnxTcGaDmPOQIrLAMCo03dB7LIuDmhkGybY3hGVyqw6VETeAx0iatRoleiM_gUgIZkKy2QLVvf02YBvyUpXGEC03EuYZulIBA&avtc=1&avte=2&avts=1714434732"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/skyf-albom-dlya-risovaniya-546467134/?asb2=fWjWHp7jjR8iVt_9x44xKJKVgnojw-nfkdMSG-MErNn1K4GYEhzVOpto0UAyw4ekU-A1iJPASR2T27GTMobBjw&avtc=1&avte=2&avts=1714434750"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/canson-bumaga-tsvetnaya-a4-21-29-7-sm-50-list-sht-1341187480/?asb2=iJ8hhLQVy7k_JEOarWmlfH1K7CnMoAXhA_ln8kAS5ubtVJH0scDmkkXHzOYwOey2j6JXvTvozSdk4xYXzNfnsg&avtc=1&avte=2&avts=1714434757"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/albom-dlya-akvareli-25-listov-30-40-na-skleyke-clairefontaine-fontaine-grain-fin-300g-m2-659303851/?asb2=hbTuM1uBgw4HRqbQ9PrkPA3pvLh3f69A22y2zIuF4y9Ivo-0pI6G3ngM4utZYnWV8QqURDcg7LfsMQjDeiCfWw&avtc=1&avte=2&avts=1714434764"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/akvarelnaya-kraska-schmincke-uroven-hudozhnika-12-tsvetov-v-korobke-12-20ml-1398834008/?asb2=fFZAfNRApKcP-BGIWSwBZC6l7GJAD96exp5GtPhlGa_gMGEEeb1VnC9jSEMACVeIuH8S9s9x9kTBLErJVWZ6EA&avtc=1&avte=2&avts=1714434773"
        elif product_name == "Рабочее место":
            if price_range == "100-500":
                url = "https://www.ozon.ru/product/podstavka-dlya-knig-i-uchebnikov-globus-metallicheskaya-chernaya-2g-07-01cher-530086621/?advert=aGrGtY28jsJ3IrnRJ-IL0B9WB0G28TjC39ldzkNJ1ZwhPubZlSAuCMLtmkg66LF4PolSRdX4PdGrKmPLR9plZY_llpwhidm9sqcnI3JdNMuXYIurP7JbQvwLeXYgKH5g2uDgFX0k_fyCPnZ7IU8Vppo2t_vB4U2WKH2lBpjKeSsgRg-clY35YFqHTU-R5c_iupe37_Uzk400jaU6ziONG-sqavstyd1xN9WmbZQWdrWH7Nujw-QeF2GbEGn9&avtc=1&avte=2&avts=1714434785"
            elif price_range == "500-1000":
                url = "https://www.ozon.ru/product/nabor-bukv-russkogo-alfavita-tsifry-i-znaki-409571995/?asb2=I_J7U8pruh2VfwBBv3jYhLIUPa-_CrbejDgqzICHD9uB79iCjA1dBlGzoemSkxZ7FlhNSxZsbjF38AMcFf7HlA&avtc=1&avte=2&avts=1714434801"
            elif price_range == "1000-5000":
                url = "https://www.ozon.ru/product/doska-probkovaya-dlya-zametok-i-foto-na-stenu-s-derevyannoy-ramkoy-1294900406/?asb2=PiYHur9nwSfpmfNjRdiniDqBheiqRRxeDLIcZBVy1XJtTTarLwC2--DrGkJa0oURsHt0dXsBXxSl5qobYiYusw&avtc=1&avte=2&avts=1714434810"
            elif price_range == "5000-10000":
                url = "https://www.ozon.ru/product/stakan-dlya-karandashey-delucci-zelenyy-mramor-h-102-mm-mbm-00009-1415920444/?asb2=02gQ-n8Kp4cj_FlbXjD2DQ52p7V68GrA1e2aMtCWaGXyomrU-xFaRLKQS84MyPWrPsQsnIivLdBgnyub1BEV9g&avtc=1&avte=2&avts=1714434820"
            elif price_range == "10000-100000":
                url = "https://www.ozon.ru/product/podstavka-dlya-korana-podstavka-dlya-knig-1534793996/?asb2=2VfWV-VFE7aNhb_FdvFcuCiO5AXxAs80WBW_QCAqNYoH3dube1Xl6a7kSCjxCnQdS10GwqGcsZot-CLB6CEAtA&avtc=1&avte=2&avts=1714434829"
    markup = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Выбрать", url=url)
    markup.add(url_button)
    return markup
bot.polling()