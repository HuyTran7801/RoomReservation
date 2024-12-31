from DAO.db_connection import *

class ReservationDAO:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        self.cursor = self.__conn.cursor()
        
    def get_all_reservations(self):
        self.cursor.execute("""
                            select * 
                            from room_system.reservation re, room_system.room r, room_system.user u, room_system.time t
                            where re.room_id = r.id and re.user_id = u.id and re.time_id = t.id         
                            """)
        return self.cursor.fetchall()
    
    def add_reservation(self, user_id, room_id, time_id):
        self.cursor.execute("""
                            insert into room_system.reservation (user_id, room_id, time_id)
                            values (%s, %s, %s)
                            """, (user_id, room_id, time_id))
        self.__conn.commit()
        
    def get_over_current_date(self, date):
        self.cursor.execute("""
                            select * from room_system.reservation re, room_system.time t
                            where re.time_id = t.id and t.day < %s
                            """, (date,))
        return self.cursor.fetchall()
        
    def get_over_current_time(self, date, time):
        self.cursor.execute("""
                            select * from room_system.reservation re, room_system.time t
                            where re.time_id = t.id  and t.day = %s and t.end < %s
                            """, (date, time))
        return self.cursor.fetchall()
    
    def delete_reservation(self, reservation_id):
        self.cursor.execute("""
                            delete from room_system.reservation re
                            where re.id = %s
                            """, (reservation_id,))
        self.__conn.commit()
        