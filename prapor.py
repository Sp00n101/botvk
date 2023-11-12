import vk_api.vk_api
import requests
import random
import schedule
import time

def start():

    schedule.every().day.at("13:50").do(stolovka)
    schedule.every().day.at("16:30").do(good)
    schedule.every().day.at("17:30").do(bigboy)
    schedule.every().day.at("18:30").do(fordaria)
    while True:
        schedule.run_pending()
        time.sleep(30)

def stolovka():
    session = requests.Session()
    login, password = '+79282922289', 'Qwerty123@1!'
    vk_session = vk_api.VkApi(login, password, app_id=2685278)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    from vk_api.longpoll import VkLongPoll, VkEventType
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    random_id = random.randrange(1, 10000)
    vk.messages.send(  # Отправляем собщение
        chat_id=2,
        random_id=random_id,
        attachment="video813824685_456239017"
    )

def good():
    session = requests.Session()
    login, password = '+79282922289', 'Qwerty123@1!'
    vk_session = vk_api.VkApi(login, password, app_id=2685278)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    from vk_api.longpoll import VkLongPoll, VkEventType
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    random_id = random.randrange(1, 10000)
    vk.messages.send(  # Отправляем собщение
    chat_id=2,
    random_id=random_id,
    attachment="photo813824685_457239020"
    )

def bigboy():
    session = requests.Session()
    login, password = '+79282922289', 'Qwerty123@1!'
    vk_session = vk_api.VkApi(login, password, app_id=2685278)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    from vk_api.longpoll import VkLongPoll, VkEventType
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    random_id = random.randrange(1, 10000)
    vk.messages.send(  # Отправляем собщение
        chat_id=2,
        random_id=random_id,
        attachment="photo813824685_457239019"
    )

def fordaria():
    session = requests.Session()
    login, password = '+79282922289', 'Qwerty123@1!'
    vk_session = vk_api.VkApi(login, password, app_id=2685278)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    from vk_api.longpoll import VkLongPoll, VkEventType
    longpoll = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    random_id = random.randrange(1, 10000)
    vk.messages.send(  # Отправляем собщение
        chat_id=2,
        random_id=random_id,
        attachment="photo813824685_457239018"
    )

        # for event in longpoll.listen():
        #    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        # Слушаем longpoll, если пришло сообщение то:
        #        if event.text == '123' or event.text == 'Второй вариант фразы':  # Если написали заданную фразу
        #            if event.from_user:  # Если написали в ЛС
        #                print("1")
        #                print(event.chat_id)
        #                print(event.user_id)
        #                random_id = random.randrange(1, 10000)
        #                vk.messages.send(
        #                   user_id=event.user_id,
        #                   random_id=random_id,
        #                   attachment="video813824685_456239017"

        #               )