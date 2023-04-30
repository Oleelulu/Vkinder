import psycopg2
from config import host, user, password, db_name

with psycopg2.connect(host = host, user = user, password = password, database = db_name) as con:
    con.autocommit = True

"""Создание таблицы для записи просмотренных профилей"""
def create_table():
    with con.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS viewed_profiles(
            id serial, 
            id_vk varchar(50) PRIMARY KEY);""")

"""Добавление просмотренных профилей в таблицу"""
def insert_profiles(id_vk):
    with con.cursor() as cursor:
        cursor.execute(f"""INSERT INTO viewed_profiles (id_vk) 
                       VALUES (%s)""",
                       (id_vk,))

"""Проверка наличия записи в таблице"""
def select_profiles():
    with con.cursor() as cursor:
        cursor.execute("""SELECT vp.id_vk
                       FROM viewed_profiles AS vp;""")
        return cursor.fetchall()

"""Удаление таблицы"""
def drop_table():
    with con.cursor() as cursor:
        cursor.execute("""DROP TABLE  IF EXISTS viewed_profiles CASCADE;""")

create_table()
print("Подключение к базе данных выполнено.")
