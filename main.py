from vk_api.longpoll import VkEventType, VkLongPoll
from core import *
from data import *
from config import *

for event in bot.longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_request = event.text.lower()
        user_id = event.user_id
        bot.user_info=bot.get_user_info(user_id)
        if user_request == 'привет' or user_request == 'hi':
            bot.message_send(user_id, f'Добрый день, {bot.get_name(user_id)}! \n' 
                                      f'Вас приветствует чат-бот Vkinder. Наберите команду "поиск" или "f".')
        elif user_request == 'поиск' or user_request == 'f':
            bot.get_age_of_user(user_id) # вычисление возраста обратившегося пользователя
            bot.get_city(user_id) # выбор города для поиска
            bot.searching_for_person(user_id)  # формируем список найденных анкет для последующего вывода
            bot.show_person(user_id)  # выводит в чат одну найденную анкету, записывает в базу данных просмотренный профиль
        elif user_request == 'удалить' or user_request == 'd':
            drop_table()  # удаляет текущую базу данных с просмотренными профилями.
            create_table()  # создает новую базу для дальнейшего поиска.
            bot.message_send(user_id, f'Список просмотренных профилей очищен. Для нового поиска наберите "поиск" или "f".')
        elif user_request == 'далее' or user_request == 'n':
            if bot.get_person_id(user_id) != 0:
                bot.show_person(user_id)
            else:
                bot.message_send(user_id, f'Сначала наберите "поиск" или "f"')
        elif user_request == 'выход' or user_request == 'e':
            bot.message_send(user_id, 'Всего доброго!')
            continue
        else:
            bot.message_send(user_id, f'Неизвестная команда. Наберите: \n'
                                      f' "поиск" или "f" - поиск людей, \n'
                                      f' "далее" или "n" - следующий профиль, \n'
                                      f' "выход" или "e" - завершение просмотра профилей.')
