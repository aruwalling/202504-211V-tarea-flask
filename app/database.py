import sqlite3
from flask import g

def init_app(app):
    app.teardown_appcontext(close_db_connection)

    with app.app_context():
        init_db()

def init_db():
    if 'db' not in g:
        g.db = sqlite3.connect("basedatos.db")
        g.db.row_factory = sqlite3.Row

def close_db_connection(exception=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def find_all():
    init_db()
    users = g.db.execute("SELECT * FROM user;").fetchall()
    return [dict(row) for row in users]

def find_by_id(user_id):
    init_db()
    user = g.db.execute("SELECT * FROM user where id = ? ", (user_id,)).fetchone()
    if user:
        return dict(user)

def insert_user(user:dict):
    init_db()

    cursor = g.db.execute(
        """
        INSERT INTO user (username, email, password) VALUES (?, ?, ?)
        """,
        (user['username'], user['email'],user['password'],)
    )

    g.db.commit()
    
    user_id = cursor.lastrowid
    cursor.close()

    return find_by_id(user_id)

def update_user(user:dict):
    init_db()

    cursor = g.db.execute(
        """
        update user set username=?, email=?, password=? where id = ? 
        """,
        (user['username'], user['email'],user['password'],user['id'],)
    )

    g.db.commit()
    cursor.close()

def delete_user(user_id):
    init_db()

    cursor = g.db.execute(
        """
        delete from user where id = ? 
        """,
        (user_id,)
    )

    g.db.commit()
    cursor.close()

