import sqlite3
from faker import Faker
import random

# Визначаємо назву БД
database = "./goit-ds-hw-02.db"

# Створення об'єкта Faker
fake = Faker()


def seed_data(number_user: int, number_tasks: int):

    # Підключення до бази даних
    con = sqlite3.connect(database)
    cursor = con.cursor()

    # Заповнення таблиці users
    user_data = [(fake.name(), fake.email()) for _ in range(number_user)]
    cursor.executemany("INSERT INTO users (fullname, email) VALUES (?, ?)", user_data)

    # Заповнення таблиці tasks
    status_count = cursor.execute("SELECT COUNT(*) FROM status").fetchone()[0]

    id_list = []
    user_ids = cursor.execute("SELECT id FROM users").fetchall()

    for user_id in user_ids:
        id_list.append(user_id[0])

    tasks_data = [
        (
            fake.word(),
            fake.sentence(),
            random.randint(1, status_count),
            random.choice(id_list),
        )
        for _ in range(number_tasks)
    ]
    cursor.executemany(
        "INSERT INTO tasks (title, description, status_id, user_id ) VALUES (?, ?, ?, ?)",
        tasks_data,
    )

    # Збереження змін та закриття з'єднання
    con.commit()
    con.close()

    return print("Database has been filled")


if __name__ == "__main__":
    seed_data(5, 4)
