import sqlite3

connection = sqlite3.connect("basedatos.db")

with open("schema.sql", "w") as f:
    f.write("""
DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    username TEXT NOT NULL unique,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);
""")

with open("schema.sql", "r") as f:
    connection.executescript(f.read())


def insert_data(data: tuple):
    connection = sqlite3.connect("basedatos.db")
    cur = connection.cursor()

    cur.execute("INSERT INTO user (username, email, password) VALUES (?, ?, ?)", data)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    insert_data(('test_user_01','test_user_01@mail.com','test_user_01'))
    insert_data(('test_user_02','test_user_02@mail.com','test_user_02'))
    insert_data(('test_user_03','test_user_03@mail.com','test_user_03'))
    insert_data(('test_user_04','test_user_04@mail.com','test_user_04'))