import sqlite3
from seed import database, seed_data


def create_db():
    # читаємо файл зі скриптом для створення БД
    with open("./my_db.sql", "r") as f:
        sql = f.read()

    # створюємо з'єднання з БД та утворюємо таблиці
    with sqlite3.connect(database) as con:
        cur = con.cursor()
        # виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)

    return print("Database has been created")


if __name__ == "__main__":
    create_db()
    seed_data(5, 4)
