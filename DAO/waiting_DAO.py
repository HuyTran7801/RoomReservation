from DAO.db_connection import *


class WaitingDAO:
    def __init__(self):
        self.__conn = DBConnection().get_connection()
        self.cursor = self.__conn.cursor()
    
    def add_waiting_list(self, user_id, room_id, time_id):
        self.cursor.execute("""
                            insert into room_system.waiting_list (user_id, room_id, time_id, status)
                            values (%s, %s, %s, 'waiting')
                            """, (user_id, room_id, time_id)) 
        self.__conn.commit()
        
    def delete_waiting_list(self, id):
        self.cursor.execute("""
                            delete from room_system.waiting_list w
                            where w.id=%s
                            """,(id,))
        self.__conn.commit()
        
    def delete_same_waiting_list(self, room_id, time_id):
        self.cursor.execute("""
                            delete from room_system.waiting_list w
                            where w.room_id=%s and w.time_id=%s
                            """,(room_id, time_id))
        self.__conn.commit()
        
        
    def get_all_waiting_list(self, user_id):
        self.cursor.execute("""
                            select w.id, r.name, r.capacity, t.day, t.start, t.end
                            from room_system.waiting_list w, room_system.room r, room_system.user u, room_system.time t
                            where u.id = w.user_id and r.id = w.room_id and t.id = w.time_id and w.status = 'waiting' and u.id=%s
                            """, (user_id,))
        return self.cursor.fetchall()
    
    def get_waiting_list_detail(self, user_id, room_id, time_id):
        self.cursor.execute("""
                            select *
                            from room_system.waiting_list w
                            where w.user_id= %s and w.room_id = %s and w.time_id = %s
                            """, (user_id, room_id, time_id))
        return self.cursor.fetchone()
    
    def get_all_waiting_list_total(self):
        self.cursor.execute("""
                            select w.id, w.user_id, w.room_id, w.time_id, u.name, u.mail, r.name, r.capacity, t.day, t.start, t.end
                            from room_system.waiting_list w, room_system.room r, room_system.user u, room_system.time t
                            where w.room_id = r.id and w.user_id = u.id and w.time_id = t.id and w.status = 'waiting'
                            """)
        return self.cursor.fetchall()
    def get_booking_deny_list(self, user_id):
        self.cursor.execute("""
                            select w.id, r.name, r.capacity, t.day, t.start, t.end
                            from room_system.waiting_list w, room_system.room r, room_system.user u, room_system.time t
                            where u.id = %s and r.id = w.room_id and t.id = w.time_id and u.id=1 and w.Status ='reject'
                            """, (user_id,))
        return self.cursor.fetchall()
    def reject_waiting_list(self, id):
        self.cursor.execute("""
                            update room_system.waiting_list w
                            set w.status = 'reject'
                            where w.id=%s
                            """,(id,))
        self.__conn.commit()
    def get_all_deny_list(self):
        self.cursor.execute("""
                            select w.id, u.name, u.mail, r.name, r.capacity, t.day, t.start, t.end
                            from room_system.waiting_list w, room_system.room r, room_system.user u, room_system.time t
                            where r.id = w.room_id and t.id = w.time_id and w.status = 'reject' and u.id = w.user_id
                            """)
        return self.cursor.fetchall()
    def delete_status_reject(self, status):
        self.cursor.execute("""
                            delete from room_system.waiting_list w
                            where w.status=%s
                            """,(status,))
        self.__conn.commit()