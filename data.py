import sqlite3

class UserDatabase():
    def __init__(self):
        self.con = sqlite3.connect("users.db")
        self.c = self.con.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS user_data (email varchar(255) UNIQUE, password varchar(20), account_status int);")
        self.con.commit()

    def validateLogin(self, email, password):
        self.c.execute("SELECT * FROM user_data WHERE email=?", email)
        result = self.c.fetchone()
        print(result)

    def CreateUser(self, email, password):
        self.c.execute("SELECT * FROM user_data WHERE email=?", [email])
        result = self.c.fetchone()
        print(result)
        #Check if the email is already in the database

        info = [email, password]
        self.c.execute("INSERT INTO user_data VALUES (?, ?)", info)
        self.con.commit()
        print(self.c)
        # Add all the info and create a new user