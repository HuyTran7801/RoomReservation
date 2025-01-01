from DAO.db_connection import DBConnection
# from model.user import User

class TimeDAO:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        self.cursor = self.__conn.cursor()
        
    def get_time_detail(self, date, start_time, end_time):
        self.cursor.execute("""
                            select * 
                            from room_system.time t
                            where t.day=%s and t.start = %s and t.end = %s
                            """, (date, start_time, end_time))
        
        return self.cursor.fetchone()
    
    def delete_over_time(self, id):
        self.cursor.execute("""
                            delete * from room_system.time t
                            where t.id=%s
                            """, (id,))
        self.__conn.commit()
        
    def get_all_times(self):
        self.cursor.execute("""select * from room_system.time""")
        return self.cursor.fetchall()
    
    
    def add_time(self, date, start_time, end_time):
        self.cursor.execute("""
                            insert into room_system.time(day, start, end)
                            values(%s, %s, %s)
                            """, (date, start_time, end_time))
        self.__conn.commit()

    def delete_time(self, time_id):
        self.cursor.execute("""
                            delete from room_system.time
                            where id=%s 
                            """, (time_id,))
        self.__conn.commit()