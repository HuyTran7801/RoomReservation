from DAO.db_connection import DBConnection
# from model.user import User

class UserDAO:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        self.cursor = self.__conn.cursor()
        
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM room_system.user")
        return self.cursor.fetchall()
    
    def get_user_by_id(self, id):
        self.cursor.execute("""
                            select * from room_system.user u
                            where u.id = %s
                            """, (id,))
        return self.cursor.fetchone()
    
    def get_user_by_name_and_password(self, name, password):
        self.cursor.execute("SELECT * FROM room_system.user u WHERE u.name = %s AND u.password = %s", 
                            (name, password))
        return self.cursor.fetchone()
    
    def get_user_by_mail(self, mail):
        self.cursor.execute("SELECT * FROM room_system.user u WHERE u.mail = %s", (mail,))
        return self.cursor.fetchone()
    
    def get_user_by_phone(self, phone):
        self.cursor.execute("SELECT * FROM room_system.user u WHERE u.phone = %s", (phone,))
        return self.cursor.fetchone()
    
    def add_user(self, name, mail, password, phone):
        self.cursor.execute("INSERT INTO room_system.user (name, mail, password, phone) VALUES (%s, %s, %s, %s)",
                            (name, mail, password, phone))
        self.__conn.commit()