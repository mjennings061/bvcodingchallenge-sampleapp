import mysql.connector


class Database:

    def __init__(self):
        self.con = mysql.connector.connect(
            host="db",
            user="root",
            password="password",
            database="uu_code_challenge"
        )
        self.cursor = self.con.cursor()

    def fetch_all(self, query_sql):     # fetch all rows as a list of tuples
        self.cursor.execute(query_sql)
        result = self.cursor.fetchall()
        self.con.commit()
        return result

    def fetch_one(self, query_sql):     # fetch one rows as a list of tuples
        self.cursor.execute(query_sql)
        result = self.cursor.fetchone()
        self.con.commit()
        return result

    # Ensure we clean up the db instance
    def __del__(self):
        self.cursor.close()
        self.con.close()