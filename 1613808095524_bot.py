importimport telebot
from telebot import types
import requests
import json
import os

bot = telebot.TeleBot("1645703081:AAE0SJlKjTgqOHwJCelu_1LHtzBn-Q7je_U")
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("Да", "Нет")
count1 = 0
count2 = 0
city = 0
work = 0
f = False
category = {"человек-человек": 0,
            "человек-природа": 0,
            "человек-техника": 0,
            "человек-знак": 0,
            "человек-искусство": 0, }
people_people = {"Юристы": 0, "Управление персоналом, Тренинги": 0,
                 "Маркетинг, Реклама, PR": 0, "Туризм, Гостиницы, Рестораны": 0,
                 "Спортивные клубы, Фитнес, Салоны красоты": 0, "Наука, Образование": 0}
people_nature = {"Туризм, Гостиницы, Рестораны": 0, "Производство, сельское хозяйство": 0,
                 "Добыча сырья": 0, "Наука, Образование": 0, "Медицина, Фармацевтика": 0, }
people_tech = {"Транспорт, логистика": 0, "Строительство, Недвижимость": 0,
               "Автомобильный бизнес": 0, "Безопасность": 0, "Наука, Образование": 0,
               "Производство, сельское хозяйство": 0}
people_zn = {"Банки, инвестиции, лизинг": 0,
             "Бухгалтерия, управленческий учет, финансы предприятия": 0,
             "Информационные технологии, интернет, телеком": 0}
people_art = {"Искусство, развлечения, масс-медиа": 0, "Маркетинг, Реклама, PR": 0, }
introduction = [["Вам нравится работать с людьми?", "человек-человек"],
                ["Вы любите собирать конструктор?", "человек-знак", "человек-техника"],
                ["Вы любите рисовать?", "человек-искусство"],
                ["Вам нравится работать за компьютером?", "человек-знак"],
                ["Вы часто гуляете на природе?", "человек-природа"],
                ["Вы любите творчество?", "человек-искусство"],
                ["Вы хорошо обращаетесь с техникой?", "человек-техника"],
                ["Вы бы хотели лечить людей?", "человек-человек", "человек-природа"],
                ["Вы разбираетесь в автомобилях?", "человек-техника"],
                ["Вам нравится изучать физику?", "человек-техника", "человек-природа"],
                ["У вас развито математическое мышление?", "человек-техника", "человек-природа", "человек-знак"],
                ["У вас развиты творческие способности?", "человек-искусство"],
                ["Вы легко находите общий язык с людьми?", "человек-человек"],
                ["Вам нравятся сельские животные?", "человек-природа"],
                ["Вам нравится готовить еду?", "человек-природа", "человек-человек"],
                ["Вам нравится информатика?", "человек-знак"]]
q_tech = [["Вам нравится водить машину?", "транспорт, логистика", "автомобильный бизнес"],
          ["Вам умеете строить кратчайшие маршруты?", "транспорт, логистика"],
          ["Вам нравится рисовать чертежи?", "транспорт, логистика"],
          ["Вам нравится работать с документами?", "строительство, недвижимость"],
          ["Вы умеете общаться с клиентами?", "строительство, недвижимость", "автомобильный бизнес"],
          ["Вы разбираетесь в машинах?", "автомобильный бизнес"],
          ["Вам нравится спасать людей?", "безопасность"],
          ["Вы умеете нестадартно мыслить и сохранять спокойствие в критической ситуации?", "безопасность"],
          ["Вы умеете передовать свои знания другим людям?", "наука, образование"],
          ["Вы любите учиться?", "наука, образование"],
          ["Вам нравится природа?", "производство, сельское хозяйство"],
          ["Вы любите производить что-либо?", "производство, сельское хозяйство"]]
q_people = [["Вы хорошо знаете конституцию?", "юристы"],
            ["Вы умеете управлять людьми? Быть лидером?", "управление персоналом, тренинги"],
            ["Вы бы хотели работать в сфере отдыха?(туризм, рестораны, кафе)?", "туризм, гостиницы, рестораны"],
            ["Вы занимаетесь спортом?", "спортивные клубы, фитнес, салон красоты"],
            ["Вы разбираетесь в маркетинге?", "маркетинг, реклама, PR"],
            ["Вы часто делаете косметические процедуры?", "спортивные клубы, фитнес, салон красоты"],
            ["Вы умеете преподавть свои знания?", "наука, образование", "управление персоналом, тренинги"],
            ["Вы умеете вести соц. сети для продвижения?", "маркетинг, реклама, PR"],
            ["Вы умеете убеждать людей в чем-либо?", "маркетинг, реклама, PR"],
            ["Вам нравится носить деловую одежду?", "туризм, гостиницы, рестораны", "наука, образование"],
            ["Вы следите за свой формой?", "спортивные клубы, фитнес, салон красоты"]]
q_zn = [["Вам нравится наблюдать за графиками?", "бухгалтерия, управленченский учет, финансы предприятия",
         "банки, инвестиции, лизинг"],
        ["Вы ведете учет своих финансов?", "бухгалтерия, управленченский учет, финансы предприятия"],
        ["Вы умеете программировать?", "информационные технологии, интернет, телеком"],
        ["Вы знаете анлийский язык?", "информационные технологии, интернет, телеком"],
        ["Вы знаете что такое сложный процент?", "банки, инвестиции, лизинг"],
        ["Вы бы хотели работать в IT сфере?", "информационные технологии, интернет, телеком"],
        ["Вы умеете общаться с клиентами?", "банки, инвестиции, лизинг"],
        ["Вы готовы долго ждать для получения прибыли?", "банки, инвестиции, лизинг"]]
q_art = [["Вам нравится театр?", "искусство, развлечения, масс-медиа"],
         ["Вы бы хотели придумывать рекламные компании?", "маркетинг, реклама, PR"],
         ["Вы бы хотели работать в сфере развлечений?", "искусство, развлечения, масс-медиа"],
         ["Вы умеете вести соц. сети для продвижения?", "маркетинг, реклама, PR"],
         ["Вы стеснительный человек?", "искусство, развлечения, масс-медиа"],
         ["Вы разбираетесь в маркетинге?", "маркетинг, реклама, PR"]]
q_nature = [["Вы бы хотели работать в сельском хозяйстве?", "производство, сельское хозяйство"],
            ["Вам нравится научная деятельность?", "наука, образование", "медецина, фармацевтика"],
            ["Вы бы хотели работать в сфере отдыха?(туризм, рестораны, кафе)?", "туризм, гостиницы, рестораны"],
            ["Вам нравится носить деловую одежду?", "туризм, гостиницы, рестораны", "наука, образование"],
            ["Вы бы хотели работать в сфере образования?", "наука, образование"],
            ["Вы хорошо знаете анатомию и физиологию?", "медецина, фармацевтика"],
            ["Вы бы смогли работать в карьерах, горах?", "добыча сырья"],
            ["Вы бы смогли выполнять однообразную работу?" "добыча сырья", "производство, сельское хозяйство"],
            ["Вам по нраву работа врача?", "медецина, фармацевтика"]]


def clear():
    global count1, count2, f, work, city
    for key in category.keys():
        category[key] = 0
    for key in people_people.keys():
        people_people[key] = 0
    for key in people_nature.keys():
        people_nature[key] = 0
    for key in people_tech.keys():
        people_tech[key] = 0
    for key in people_zn.keys():
        people_zn[key] = 0
    for key in people_art.keys():
        people_art[key] = 0
    count1 = 0
    count2 = 0
    f = False
    city = 0
    work = 0


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def get_category():
    if get_key(category, max(category.values())) == "человек-человек":
        return [q_people, people_people]
    elif get_key(category, max(category.values())) == "человек-знак":
        return [q_zn, people_zn]
    elif get_key(category, max(category.values())) == "человек-природа":
        return [q_nature, people_nature]
    elif get_key(category, max(category.values())) == "человек-техника":
        return [q_tech, people_tech]
    else:
        return [q_art, people_art]


def get_result():
    return get_key(get_category()[1], max(get_category()[1].values()))


def get_area(city):
    response = requests.get(
        f"https://api.hh.ru/suggests/areas?text={city}")
    json_response = response.json()
    c = json_response["items"][0]["id"]
    return c

@bot.message_handler(content_types=['location'])
def handle_loc(message):
    global city, work
    print(work)
    response = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=\
        {str(message.location.longitude)},{str(message.location.latitude)}&format=json")
    json_response = response.json()
    city = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]\
        ["GeocoderMetaData"]["Address"]["Components"][4]["name"]
    print(city)
    params = {
        'specialization': work,  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': get_area(city),  # Поиск ощуществляется по вакансиям города Москва
        'page': 1,  # Индекс страницы поиска на HH
        'per_page': 5  # Кол-во вакансий на 1 странице
    }

    req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
    print(req.url)
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    # Преобразуем текст ответа запроса в справочник Python
    js = json.loads(data)
    s = "Вакансии которые вам подходят:\n\n"
    zapros = "https://belgorod.hh.ru/vacancy/"
    for i in range(5):
        s += js["items"][i]["name"] + "\n" + (zapros + str(js["items"][i]["id"])) + "\n\n"

    keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
    keyboard2.row("Сброс")
    bot.send_message(message.chat.id, s, reply_markup=keyboard2)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Для начала теста напиши мне "/test"')


@bot.message_handler(commands=['test'])
def first_message(message):
    global f
    f = True
    bot.send_message(message.chat.id, introduction[0][0], reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def send_questions(message):
    global count1, count2, keyboard1, f, city, work
    if message.text.lower() == 'сброс':
        clear()
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
        keyboard3.row("/test")
        bot.send_message(message.chat.id, 'Для начала теста напиши мне "/test"', reply_markup=keyboard3)
    if f:
        if message.text.lower() == "да":  # действия после ответа да
            if count1 < len(introduction):  # блок для вводных вопросов
                for i in range(1, len(introduction[count1])):
                    category[introduction[count1][i]] += 1
                count1 += 1
                if count1 < len(introduction):
                    bot.send_message(message.chat.id, introduction[count1 - len(introduction)][0], reply_markup=keyboard1)
                else:  # первый вопрос классовго блока
                    bot.send_message(message.chat.id, get_category()[0][count2][0], reply_markup=keyboard1)
            else:  # блок для классовых вопросов
                if count2 < len(get_category()[0]):
                    for i in range(1, len(get_category()[0][count2])):
                        get_category()[1][get_category()[0][count2][i]] += 1
                    count2 += 1
                    if count2 < len(get_category()[0]):
                        bot.send_message(message.chat.id, get_category()[0][count2 - len(get_category()[0])][0],
                                         reply_markup=keyboard1)
                    else:  # блок итога
                        keyboard = telebot.types.ReplyKeyboardMarkup(True)
                        work = get_result()
                        button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
                        keyboard.add(button_geo, "Сброс")
                        bot.send_message(message.chat.id,
                                         message.from_user.first_name + " ,тебе подходят профессии: " + work,
                                         reply_markup=keyboard)
        elif message.text.lower() == "нет":  # действия после ответа нет
            if count1 < len(introduction):  # блок для вводных вопросов
                count1 += 1
                if count1 < len(introduction):
                    bot.send_message(message.chat.id, introduction[count1 - len(introduction)][0], reply_markup=keyboard1)
                else:  # первый вопрос классовго блока
                    bot.send_message(message.chat.id, get_category()[0][count2][0], reply_markup=keyboard1)
            else:  # блок для классовых вопросов
                if count2 < len(get_category()[0]):
                    count2 += 1
                    bot.send_message(message.chat.id, get_category()[0][count2 - len(get_category()[0])][0],
                                     reply_markup=keyboard1)
                else:  # блок итога
                    keyboard = telebot.types.ReplyKeyboardMarkup(True)
                    work = get_result()
                    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
                    keyboard.add(button_geo, "Сброс")
                    bot.send_message(message.chat.id,
                                     message.from_user.first_name + " ,тебе подходят профессии: " + work,
                                     reply_markup=keyboard)

        else:
            bot.send_message(message.chat.id, 'Нужно отвечать "да" или "нет"\n-_-')


bot.polling()

          ["Вы умеете общаться с клиентами?", "строительство, недвижимость", "автомобильный бизнес"],
          ["Вы разбираетесь в машинах?", "автомобильный бизнес"],
          ["Вам нравится спасать людей?", "безопасность"],
          ["Вы умеете нестадартно мыслить и сохранять спокойствие в критической ситуации?", "безопасность"],
          ["Вы умеете передовать свои знания другим людям?", "наука, образование"],
          ["Вы любите учиться?", "наука, образование"],
          ["Вам нравится природа?", "производство, сельское хозяйство"],
          ["Вы любите производить что-либо?", "производство, сельское хозяйство"]]
q_people = [["Вы хорошо знаете конституцию?", "юристы"],
            ["Вы умеете управлять людьми? Быть лидером?", "управление персоналом, тренинги"],
            ["Вы бы хотели работать в сфере отдыха?(туризм, рестораны, кафе)?", "туризм, гостиницы, рестораны"],
            ["Вы занимаетесь спортом?", "спортивные клубы, фитнес, салон красоты"],
            ["Вы разбираетесь в маркетинге?", "маркетинг, реклама, PR"],
            ["Вы часто делаете косметические процедуры?", "спортивные клубы, фитнес, салон красоты"],
            ["Вы умеете преподавть свои знания?", "наука, образование", "управление персоналом, тренинги"],
            ["Вы умеете вести соц. сети для продвижения?", "маркетинг, реклама, PR"],
            ["Вы умеете убеждать людей в чем-либо?", "маркетинг, реклама, PR", "менеджмент, консультирование"],
            ["Вам нравится носить деловую одежду?", "туризм, гостиницы, рестораны", "наука, образование"],
            ["Вы следите за свой формой?", "спортивные клубы, фитнес, салон красоты"]]
q_zn = [["Вам нравится наблюдать за графиками?", "бухгалтерия, управленченский учет, финансы предприятия",
         "банки, инвестиции, лизинг"],
        ["Вы ведете учет своих финансов?", "бухгалтерия, управленченский учет, финансы предприятия"],
        ["Вы умеете программировать?", "информационные технологии, интернет, телеком"],
        ["Вы знаете анлийский язык?", "информационные технологии, интернет, телеком"],
        ["Вы знаете что такое сложный процент?", "банки, инвестиции, лизинг"],
        ["Вы бы хотели работать в IT сфере?", "информационные технологии, интернет, телеком"],
        ["Вы умеете общаться с клиентами?", "банки, инвестиции, лизинг"],
        ["Вы готовы долго ждать для получения прибыли?", "банки, инвестиции, лизинг"]]
q_art = [["Вам нравится театр?", "искусство, развлечения, масс-медиа"],
         ["Вы бы хотели придумывать рекламные компании?", "маркетинг, реклама, PR"],
         ["Вы бы хотели работать в сфере развлечений?", "искусство, развлечения, масс-медиа"],
         ["Вы умеете вести соц. сети для продвижения?", "маркетинг, реклама, PR"],
         ["Вы стеснительный человек?", "искусство, развлечения, масс-медиа"],
         ["Вы разбираетесь в маркетинге?", "маркетинг, реклама, PR"]]
q_nature = [["Вы бы хотели работать в сельском хозяйстве?", "производство, сельское хозяйство"],
            ["Вам нравится научная деятельность?", "наука, образование", "медецина, фармацевтика"],
            ["Вы бы хотели работать в сфере отдыха?(туризм, рестораны, кафе)?", "туризм, гостиницы, рестораны"],
            ["Вам нравится носить деловую одежду?", "туризм, гостиницы, рестораны", "наука, образование"],
            ["Вы бы хотели работать в сфере образования?", "наука, образование"],
            ["Вы хорошо знаете анатомию и физиологию?", "медецина, фармацевтика"],
            ["Вы бы смогли работать в карьерах, горах?", "добыча сырья"],
            ["Вы бы смогли выполнять однообразную работу?" "добыча сырья", "производство, сельское хозяйство"],
            ["Вам по нраву работа врача?", "медецина, фармацевтика"]]


def clear():
    global count1, count2, f
    for key in category.keys():
        category[key] = 0
    for key in people_people.keys():
        people_people[key] = 0
    for key in people_nature.keys():
        people_nature[key] = 0
    for key in people_tech.keys():
        people_tech[key] = 0
    for key in people_zn.keys():
        people_zn[key] = 0
    for key in people_art.keys():
        people_art[key] = 0
    count1 = 0
    count2 = 0
    f = False


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def get_category():
    if get_key(category, max(category.values())) == "человек-человек":
        return [q_people, people_people]
    elif get_key(category, max(category.values())) == "человек-знак":
        return [q_zn, people_zn]
    elif get_key(category, max(category.values())) == "человек-природа":
        return [q_nature, people_nature]
    elif get_key(category, max(category.values())) == "человек-техника":
        return [q_tech, people_tech]
    else:
        return [q_art, people_art]


def get_result():
    return get_key(get_category()[1], max(get_category()[1].values()))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Для начала теста напиши мне "/test"')


@bot.message_handler(commands=['test'])
def first_message(message):
    global f
    f = True
    bot.send_message(message.chat.id, introduction[0][0], reply_markup=keyboard1)


@bot.message_handler(content_types=["text"])
def send_questions(message):
    global count1, count2, keyboard1, f
    if f:
        if message.text.lower() == 'сброс':
            clear()
            keyboard3 = telebot.types.ReplyKeyboardMarkup(True)
            keyboard3.row("/test")
            bot.send_message(message.chat.id, 'Для начала теста напиши мне "/test"', reply_markup=keyboard3)
        elif message.text.lower() == "да":  # действия после ответа да
            if count1 < len(introduction):  # блок для вводных вопросов
                for i in range(1, len(introduction[count1])):
                    category[introduction[count1][i]] += 1
                count1 += 1
                if count1 < len(introduction):
                    bot.send_message(message.chat.id, introduction[count1 - len(introduction)][0], reply_markup=keyboard1)
                else:  # первый вопрос классовго блока
                    bot.send_message(message.chat.id, get_category()[0][count2][0], reply_markup=keyboard1)
            else:  # блок для классовых вопросов
                if count2 < len(get_category()[0]):
                    for i in range(1, len(get_category()[0][count2])):
                        get_category()[1][get_category()[0][count2][i]] += 1
                    count2 += 1
                    if count2 < len(get_category()[0]):
                        bot.send_message(message.chat.id, get_category()[0][count2 - len(get_category()[0])][0],
                                         reply_markup=keyboard1)
                    else:  # блок итога
                        keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
                        keyboard2.row("Сброс")
                        bot.send_message(message.chat.id,
                                         message.from_user.first_name + " ,тебе подходят профессии: " + get_result(),
                                         reply_markup=keyboard2)
        elif message.text.lower() == "нет":  # действия после ответа нет
            if count1 < len(introduction):  # блок для вводных вопросов
                count1 += 1
                if count1 < len(introduction):
                    bot.send_message(message.chat.id, introduction[count1 - len(introduction)][0], reply_markup=keyboard1)
                else:  # первый вопрос классовго блока
                    bot.send_message(message.chat.id, get_category()[0][count2][0], reply_markup=keyboard1)
            else:  # блок для классовых вопросов
                if count2 < len(get_category()[0]):
                    count2 += 1
                    bot.send_message(message.chat.id, get_category()[0][count2 - len(get_category()[0])][0],
                                     reply_markup=keyboard1)
                else:  # блок итога

                    keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
                    keyboard2.row("Сброс")
                    bot.send_message(message.chat.id,
                                     message.from_user.first_name + " ,тебе подходят профессии: " + get_result(),
                                     reply_markup=keyboard2)

        else:
            bot.send_message(message.chat.id, 'Нужно отвечать "да" или "нет"\n-_-')


bot.polling()
