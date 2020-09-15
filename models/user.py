import sqlite3


class UserModel:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('db/data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))

        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()

        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect('db/data.db')
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))

        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        conn.close()

        return user
