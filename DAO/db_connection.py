from mysql.connector import connect

class DBConnection:
    def __init__(self):
        self.__connection = connect(
            host="127.0.0.1",
            user="root",
            password="admin",
            database="room_system"
        )
        
    def get_connection(self):
        return self.__connection