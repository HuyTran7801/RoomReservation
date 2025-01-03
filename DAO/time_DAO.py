from DAO.db_connection import DBConnection
# from model.user import User

class TimeDAO:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        self.cursor = self.__conn.cursor(buffered=True)
        
    # def get_time_detail(self, time):
    #     self.cursor.execute("""
    #                         select * 
    #                         from room_system.time t
    #                         where t.day=%s and t.start = %s and t.end = %s
    #                         """, (time.get_day(), time.get_start_time(), time.get_end_time()))
        
    #     return self.cursor.fetchone()
    
    def get_time_detail(self, day, start, end):
        self.cursor.execute("""
                            select * 
                            from room_system.time t
                            where t.day=%s and t.start = %s and t.end = %s
                            """, (day, start, end))
        
        return self.cursor.fetchone()
    
    def delete_over_time(self, id):
        self.cursor.execute("""
                            delete * from room_system.time t
                            where t.id=%s
                            """, (id,))
        self.__conn.commit()
        
    def get_all_times(self):
        self.cursor.execute("""select * from room_system.time t order by t.day""")
        return self.cursor.fetchall()
    
    
    def add_time(self, time):
        self.cursor.execute("""
                            insert into room_system.time(day, start, end)
                            values(%s, %s, %s)
                            """, (time.get_day(), time.get_start_time(), time.get_end_time()))
        self.__conn.commit()

    def delete_time(self, time_id):
        self.cursor.execute("""
                            delete from room_system.time
                            where id=%s 
                            """, (time_id,))
        self.__conn.commit()