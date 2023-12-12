import telebot
from telebot import types
bot = telebot.TeleBot("6765900390:AAGIPTUf1d3UFhdZh_ahlzg4U80TPBq9eX8")

@bot.message_handler(commands=['start'])
def question(message):
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, "Привет! Выбери, что хочешь узнать:\n"
                                      "/vocab : Лексика по темам\n"
                                      "/grammar : Грамматика", reply_markup=markup_reply)
@bot.message_handler(commands=['vocab'])
def question(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    person_description = types.InlineKeyboardButton("Человек как живое существо", callback_data='answer_desc')
    society = types.InlineKeyboardButton("Человек и общество", callback_data='answer_society')
    nature = types.InlineKeyboardButton("Природа", callback_data='answer_nature')
    abstract = types.InlineKeyboardButton("Абстрактные понятия", callback_data='answer_abstract')
    numbers = types.InlineKeyboardButton("Числительные", callback_data='answer_numbers')

    markup.add(person_description, society, nature, abstract, numbers)
    bot.send_message(message.chat.id, "Выбери тему:", reply_markup=markup)

@bot.message_handler(commands=['grammar'])
def question1(message):
    markup = types.InlineKeyboardMarkup(row_width=2)

    phonetics = types.InlineKeyboardButton("Фонетика", callback_data='answer_phonetics')
    syntax = types.InlineKeyboardButton("Синтаксис", callback_data='answer_syntax')
    morphs = types.InlineKeyboardButton("Словообразование и морфемы", callback_data='answer_morphs')

    markup.add(phonetics,syntax, morphs)
    bot.send_message(message.chat.id, "Выбери тему:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def answer(callback):
    if callback.message:
        if callback.data == 'answer_desc':
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            age = types.KeyboardButton("Возраст")
            body = types.KeyboardButton("Части тела, внешность")
            health = types.KeyboardButton("Здоровье")
            food = types.KeyboardButton("Питание")
            house = types.KeyboardButton("Жилье")
            clothes = types.KeyboardButton("Одежда")
            emotions = types.KeyboardButton("Эмоции")
            character = types.KeyboardButton("Характер")

            markup_reply.add(age,body,health,food,house, clothes,emotions,character)
            bot.send_message(callback.message.chat.id, "Выбери подтему.", reply_markup=markup_reply)
        elif callback.data == "answer_society":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            family = types.KeyboardButton("Семья")
            relations = types.KeyboardButton("Отношения/связи")
            profession = types.KeyboardButton("Профессии")
            education = types.KeyboardButton("Образование")
            art = types.KeyboardButton("Искусство")
            rest = types.KeyboardButton("Отдых")
            travel = types.KeyboardButton("Путешествие")
            vehicle = types.KeyboardButton("Транспорт")

            markup_reply.add(family,relations,profession,education,art,rest,travel,vehicle)
            bot.send_message(callback.message.chat.id, "Выбери подтему.", reply_markup=markup_reply)
        elif callback.data == "answer_nature":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            climate = types.KeyboardButton("Климат")
            geography = types.KeyboardButton("География")
            animals = types.KeyboardButton("Животные")
            plants = types.KeyboardButton("Растения")

            markup_reply.add(climate,geography,animals,plants)
            bot.send_message(callback.message.chat.id, "Выбери подтему.", reply_markup=markup_reply)
        elif callback.data == "answer_abstract":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            place = types.KeyboardButton("Место")
            time = types.KeyboardButton("Время")
            metrics = types.KeyboardButton("Единицы измерения")

            markup_reply.add(place,time,metrics)
            bot.send_message(callback.message.chat.id, "Выбери подтему.", reply_markup=markup_reply)

        elif callback.data == "answer_numbers":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(callback.message.chat.id, "1 один\n"
                                                       "2 два\n"
                                                       "3 три\n"
                                                       "4 четыре\n"
                                                       "5 пять\n"
                                                       "6 шесть\n"
                                                       "7 семь\n"
                                                       "8 восемь\n"
                                                       "9 девять\n"
                                                       "10 десять\n"
                                                       "11 одиннадцать\n"
                                                       "12 двенадцать\n"
                                                       "13 тринадцать\n"
                                                       "14 четырнадцать\n"
                                                       "15 пятнадцать\n"
                                                       "16 шестнадцать\n"
                                                       "17 семнадцать\n"
                                                       "18 восемнадцать\n"
                                                       "19 девятнадцать\n"
                                                       "20 двадцать\n"
                                                       "21 двадцать один\n"
                                                       "22 двадцать два\n"
                                                       "30 тридцать\n"
                                                       "40 сорок\n"
                                                       "50 пятьдесят\n"
                                                       "60 шестьдесят\n"
                                                       "70 семьдесят\n"
                                                       "80 восемьдесят\n"
                                                       "90 девяносто\n"
                                                       "100 сто\n"
                                                       "200 двести\n"
                                                       "300 триста\n"
                                                       "400 четыреста\n"
                                                       "500 пятьсот\
                                                       600 шестьсот\n"
                                                       "700 семьсот\n"
                                                       "800 восемьсот\n"
                                                       "900 девятьсот\n"
                                                       "1.000 тысяча\n"
                                                       "1.000.000 миллион\n"
                                                       "1.000.000.000 миллиард", reply_markup=markup_reply)

        elif callback.data == "answer_phonetics":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(callback.message.chat.id, "В русском языке согласные звуки передаются буквами Б, В, Г, "
                                                       "Д, Ж, З, Й, К, Л, М, Н, П, Р, С, Т, Ф, Х, Ц, Ч, Ш, Щ.\n "
                                                       "Гласные звуки передаются буквами А, И, О, У, Ы, Э.\n"
                                                       "\n"
                                                       "Запомните: Всегда мягкие звуки: [й’], [ч’] , [щ’].\n"
                                                       "Всегда твёрдые звуки: [ж], [ш] , [ц].\n"
                                                       "Остальные звуки являются мягкими, если сразу за ними следуют "
                                                       "гласные буквы е, ё, и, ю, я или ь, и твёрдыми, если за ними "
                                                       "следуют другие гласные и согласные.", reply_markup=markup_reply)

        elif callback.data == "answer_syntax":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            type = types.KeyboardButton("Виды предложений")
            order = types.KeyboardButton("Порядок слов")

            markup_reply.add(type, order)
            bot.send_message(callback.message.chat.id, "Выбери подтему.", reply_markup=markup_reply)
        elif callback.data == "answer_morphs":
            markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
            noun = types.KeyboardButton("Существительное")
            pronoun = types.KeyboardButton("Местоимение")
            verb = types.KeyboardButton("Глагол")
            number = types.KeyboardButton("Числительные")

            markup_reply.add(noun,pronoun,verb,number)
            bot.send_message(callback.message.chat.id, "Выбери подтему.", reply_markup=markup_reply)

@bot.message_handler(content_types=['text'])
def theme(message):
    if message.text == "Возраст":
        bot.send_message(message.chat.id, "человек, молодой человек, люди, женщина, жизнь, мужчина, рождение, смерть, "
                                          "родиться, жить, день, умереть, месяц, год (лет), детский (возраст), "
                                          "дети, молодой, мальчик, младший, девочка, старший, девушка, старый")
    elif message.text == "Части тела, внешность":
        bot.send_message(message.chat.id, "голова, лицо, глаз, рука, высокий, маленький, красивый, сильный")
    elif message.text == "Здоровье":
        bot.send_message(message.chat.id, "медицина, врач, поликлиника, температура, аптека, "
                                          "чувствовать себя (плохо / хорошо), болен, здоров")
    elif message.text == "Питание":
        bot.send_message(message.chat.id, "завтрак, обед, ужин, суп, хлеб, рыба, яйцо, рис, салат, овощи, "
                                          "картофель, соль, фрукты, яблоко, мороженое, шоколад, сахар, молоко, "
                                          "чай, кофе, сок, вода, пиво, вино, колбаса, сыр, масло, курица, мясо, "
                                          "ложка, вилка, нож, чайник, чашка, кафе, ресторан, столовая, горячий, "
                                          "вкусно, есть, пить, готовить, завтракать, обедать, ужинать")
    elif message.text == "Жилье":
        bot.send_message(message.chat.id, " а) жилище: дом, здание, квартира, выход, вход, этаж, дверь, квартира, комната, "
                                          "кабинет, кухня, стена, окно;\n"
                                          "б) мебель: кресло, стул, стол, шкаф;\n"
                                          "в) предметы быта: зонт, картина, лампа, часы, сувенир, сумка. фотоаппарат;\n"
                                          "г) бытовая техника: телефон, радио, телевизор, холодильник, плита, стиральная машина")
    elif message.text == "Одежда":
        bot.send_message(message.chat.id, "одежда, костюм, платье, рубашка, брюки, футболка, шапка, "
                                          "шарф. обувь, покупать, дарить, современный, красивый, легкий")
    elif message.text == "Эмоции":
        bot.send_message(message.chat.id, "любовь, счастье, удовольствие, любить, нравиться, весело, "
                                          "внимательно, интересно, осторожно, приятно, спокойно, жаль, рад")
    elif message.text == "Характер":
        bot.send_message(message.chat.id, "активный, смелый, веселый, сильный")

    elif message.text == "Семья":
        bot.send_message(message.chat.id, "семья, мама, мать, папа, отец, муж, жена, родители, дети, "
                                          "дочь, сын, брат, сестра, бабушка, дедушка, внук, внучка, тетя, "
                                          "дядя, младший, родной, старший")
    elif message.text == "Отношения/связи":
        bot.send_message(message.chat.id,"а) по месту жительства и национальности:\n"
                                         "житель\n"
                                         "сосед — соседка\n"
                                         "москвич — москвичка — москвичи\n"
                                         "англичанин — англичанка — англичане\n"
                                         "иностранец — иностранка — иностранцы\n"
                                         "испанец — испанка — испанцы\n"
                                         "китаец — китаянка — китайцы\n"
                                         "немец — немка — немцы\n"
                                         "русский — русская — русские\n"
                                         "француз — француженка — французы\n"
                                         "\n"
                                         "б) по отношению друг к другу:\n"
                                         "друг — друзья\n"
                                         "подруга, товарищ, хозяин, гость")
    elif message.text == "Профессии":
        bot.send_message(message.chat.id,"профессия, экономист, работа, юрист, артист — артистка, "
                                         "врач, музыкант, инженер, журналист, переводчик, историк, "
                                         "математик, преподаватель — преподавательница, учитель — учительница, "
                                         "философ, химик, физик, филолог, работать (кем? где?), быть (кем?), "
                                         "делать — сделать (что?), получать — получить (профессию),  стать (кем?)")
    elif message.text == "Образование":
        bot.send_message(message.chat.id,"наука, школа, институт, университет, класс (первый класс), группа, "
                                         "курс, факультет, ученик — ученица, студент — студентка, учитель — учительница, "
                                         "преподаватель — преподавательница, учёный, биология, география, история, "
                                         "литература, математика, медицина, физика, язык (иностранный), философия, "
                                         "химия, экономика, программа, лекция, урок, экзамен, перерыв, класс, "
                                         "аудитория, вопрос, ответ, задача, упражнение, ошибка, буква, слово, "
                                         "фраза, номер, цифра, число, карандаш, ручка, книга, учебник, словарь, "
                                         "страница, текст, тетрадь")
    elif message.text == "Искусство":
        bot.send_message(message.chat.id,"художник, картина, фотография, выставка, музей, фотоаппарат, кино, "
                                         "билет, фильм, артист, писатель, поэт, литература, книга, рассказ, "
                                         "роман, комедия, стихи, музыкант, музыка, концерт, песня, опера,  "
                                         "гитара, пианино, петь, балет, танцевать")
    elif message.text == "Отдых":
        bot.send_message(message.chat.id,"отдых,  отдыхать, праздник, гулять, время (свободное время), "
                                         "идти (в гости), Новый год, приглашать — пригласить (кого? куда?), "
                                         "день рождения, дарить — подарить (кому? что?), желать (чего?), "
                                         "гость, хозяин, весело")
    elif message.text == "Путешествие":
        bot.send_message(message.chat.id,"турист, экскурсовод, машина, дорога, станция, остановка, "
                                         "касса, билет, экскурсия, карта, паспорт,  пойти (куда?), "
                                         "ехать (куда? откуда?), смотреть — посмотреть (что?)")
    elif message.text == "Транспорт":
        bot.send_message(message.chat.id,"транспорт, автобус, машина, метро, такси, трамвай, троллейбус, "
                                         "самолет, поезд, вагон, место, касса, билет, остановка, станция, "
                                         "вокзал, аэропорт, быстро, медленно")

    elif message.text == "Климат":
        bot.send_message(message.chat.id,"температура: жарко, тепло, холодно; \n"
                                         "времена года: зима, весна, лето, осень; \n"
                                         "погода: холодный, солнце, (сильный) дождь, снег, тепло, жарко, "
                                         "идти (дождь, снег идёт), холодно, хорошая (погода), плохая")
    elif message.text == "География":
        bot.send_message(message.chat.id,"солнце, земля, море, река, гора, континент, Австралия, Азия, "
                                         "Америка (Северная, Южная), Африка, Европа, страна, Америка, Англия, "
                                         "Аргентина, Бразилия, Германия, Египет, Индия, Испания, Италия, Китай, "
                                         "Корея, Ливия, Мексика, Норвегия, Россия, Сирия, Финляндия, Франция, "
                                         "Швейцария, Швеция, Эфиопия, Япония")
    elif message.text == "Животные":
        bot.send_message(message.chat.id,"кошка, собака, курица, рыба")
    elif message.text == "Растения":
        bot.send_message(message.chat.id,"дерево, картошка, цветок, овощи, фрукты, высокий, зеленый")

    elif message.text == "Место":
        bot.send_message(message.chat.id, "близко, недалеко, далеко, здесь, там, тут, рядом, слева, "
                                          "справа, сюда, туда, в, на, из, с")
    elif message.text == "Время":
        bot.send_message(message.chat.id, "месяцы: январь, февраль, март, апрель, май, июнь, июль, август, сентябрь, "
                                          "октябрь, ноябрь, декабрь; \n"
                                          "дни недели: понедельник, вторник, среда, четверг, пятница, суббота, воскресенье; \n"
                                          "время суток: утро, день, вечер, ночь; \n"
                                          "период: год, месяц, неделя, день, час, минута, век")
    elif message.text == "Единицы измерения":
        bot.send_message(message.chat.id, "километр, метр, час, секунда, минута, килограмм, грамм, копейка, рубль")

    elif message.text == "Виды предложений":
        bot.send_message(message.chat.id, "— повествовательные: Вчера приехал мой друг.\n"
                                          "— побудительные: Пойдём в парк.\n"
                                          "— утвердительные: Андрей смотрит телевизор. Сегодня тепло.\n"
                                          "— отрицательные: Гости не пришли\n"
                                          "— вопросительные: Сколько стоит эта книга?")
    elif message.text == "Порядок слов":
        bot.send_message(message.chat.id, "— прилагательное предшествует существительному (интересная выставка);\n"
                                          "— главное слово, потом зависимое (в центре города; читает газету);\n"
                                          "— наречия на о, е, потом глагол (хорошо танцует);\n"
                                          "— подлежащее перед сказуемым (Брат читает.);")

    elif message.text == "Существительное":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        nominative = types.KeyboardButton("Им.п.")
        genitive = types.KeyboardButton("Род.п.")
        dative = types.KeyboardButton("Дат.п.")
        accusative = types.KeyboardButton("Вин.п.")
        ablative = types.KeyboardButton("Твор.п.")
        prepos = types.KeyboardButton("Предл.п.")

        markup_reply.add(nominative,genitive,dative,accusative,ablative,prepos)
        bot.send_message(message.chat.id, "Выбери падеж.", reply_markup=markup_reply)

    elif message.text == "Им.п.":
        bot.send_message(message.chat.id,"— лицо активного действия: Нина смотрит телевизор.\n"
                                         "— название лица (предмета): Это Андрей. Вот книга.\n"
                                         "— обращение: Андрей, иди сюда!\n"
                                         "— характеристика лица: Брат — врач.\n"
                                         "— факты, события: Завтра экзамены.\n"
                                         "— наличие предмета: В городе есть театр.\n"
                                         "— предмет обладания: У меня есть книга.\n"
                                         "— идентификация лица: Меня зовут Лена.")
    elif message.text == "Род.п.":
        bot.send_message(message.chat.id,"а) без предлога:\n"
                                         "— определение предмета (лица): Это центр города. Вот машина брата.\n"
                                         "— отсутствие лица (предмета): У меня нет брата. \n"
                                         "— обозначение количества, меры в сочетании с числительными два, три, четыре, пять: "
                                         "Сейчас 2 часа. Ручки стоят 5 рублей.\n"
                                         "— месяц в дате (на вопрос «Какое сегодня число? Первое января.»)\n"
                                         "\n"
                                         "б) с предлогом:\n"
                                         "— исходный пункт движения (из, с):  Они приехали из Англии. Мы пришли с концерта.\n"
                                         "— лицо, которому принадлежит что-либо (у): У Андрея есть машина.")
    elif message.text == "Дат.п.":
        bot.send_message(message.chat.id,"а) без предлога:\n"
                                         "— адресат действия: Вечером я звоню отцу.\n"
                                         "— лицо (предмет), о возрасте которого идет речь (только с личными местоимениями): "
                                         "Это мой друг. Ему двадцать лет.\n"
                                         "— лицо, испытывающее необходимость в чем-либо (только с личными местоимениями): "
                                         "Мне нужно пойти в банк.\n"
                                         "\n"
                                         "б) с предлогом:\n"
                                         "— лицо как цель движения (к): Я иду к врачу.")
    elif message.text == "Вин.п.":
        bot.send_message(message.chat.id,"а) без предлога:\n"
                                         "— лицо (предмет) как объект действия: Анна купила журнал. Я встретил Анну.\n"
                                         "— логический субъект при глаголе звать: Меня зовут Сергей.\n"
                                         "— продолжительность действия, обозначает время, срок: Я живу здесь месяц.\n"
                                         "\n"
                                         "б) с предлогом:\n"
                                         "— направление движения (в, на): Утром я иду в институт, на работу.\n"
                                         "— время (час, день недели) (в): В среду у нас экскурсия.")
    elif message.text == "Твор.п.":
        bot.send_message(message.chat.id,"а) без предлога:\n"
                                         "— с глаголом заниматься: Брат занимается спортом.\n"
                                         "— профессия лица (при глаголе быть): Борис будет инженером.\n"
                                         "\n"
                                         "б) с предлогом:\n"
                                         "— совместность: Отец разговаривает с сыном.\n"
                                         "— определение: Я люблю чай с молоком.")
    elif message.text == "Предл.п.":
        bot.send_message(message.chat.id,"с предлогом:\n"
                                         "— объект речи, мысли: Я часто думаю о семье.\n"
                                         "— место (в/на): Книга в столе (на столе).\n"
                                         "— средство передвижения (на): Студенты едут в театр на автобусе.")

    elif message.text == "Местоимение":
        bot.send_message(message.chat.id, "Личные: я, ты, он, она, оно, мы, вы, они\n"
                                          "Вопросительные: какой?; чей?; сколько?\n"
                                          "Притяжательные: мой, твой, его, её, наш, ваш, их\n"
                                          "Указательные: этот, тот\n"
                                          "Отрицательные: никто, ничто")

    elif message.text == "Числительные":
        bot.send_message(message.chat.id, "Количественное-порядковое:\n"
                                          "\n"
                                          "один - первый\n"
                                          "два - второй\n"
                                          "три - третий\n"
                                          "четыре - четвёртый\n"
                                          "пять - пятый\n"
                                          "шесть - шестой\n"
                                          "семь - седьмой\n"
                                          "восемь - восьмой\n"
                                          "девять - девятый\n"
                                          "десять - десятый")

    elif message.text == "Глагол":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        present = types.KeyboardButton("Настоящее")
        past = types.KeyboardButton("Прошедшее")
        future = types.KeyboardButton("Будущее")

        markup_reply.add(present,past,future)
        bot.send_message(message.chat.id, "Выбери время.", reply_markup=markup_reply)

    elif message.text == "Настоящее":
        bot.send_message(message.chat.id, "1 спряжение: читать\n"
                                          "я читаю\n"
                                          "ты читаешь\n"
                                          "он/она читает\n"
                                          "мы читаем\n"
                                          "вы читаете\n"
                                          "они читают\n"
                                          "\n"
                                          "2 спряжение: говорить\n"
                                          "я говорю\n"
                                          "ты говоришь\n"
                                          "он/она говорит\n"
                                          "мы говорим\n"
                                          "вы говорите\n"
                                          "они говорят")
    elif message.text == "Прошедшее":
        bot.send_message(message.chat.id, "говорить\n"
                                          "\n"
                                          "он говорил\n"
                                          "она говорила\n"
                                          "они говорили\n"
                                          "оно говорило")
    elif message.text == "Будущее":
        bot.send_message(message.chat.id, "читать\n"
                                          "\n"
                                          "я буду читать\n"
                                          "ты будешь читать\n"
                                          "он/она будет читать\n"
                                          "мы будем читать\n"
                                          "вы будете читать\n"
                                          "они будут читать")


bot.polling()