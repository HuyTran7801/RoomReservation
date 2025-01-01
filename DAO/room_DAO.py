import mysql.connector
from DAO.db_connection import DBConnection

class RoomDAO:
    def  __init__(self):
        self.__conn = DBConnection().get_connection()
        self.cursor = self.__conn.cursor()
        
    def get_all_rooms(self):
        self.cursor.execute("SELECT * FROM room_system.room")
        return self.cursor.fetchall()
    
    def get_room_detail(self, id):
        self.cursor.execute("""
                            select r.capacity, r.name 
                            from room_system.room r
                            where r.id = %s
                            """, (id,))
        return self.cursor.fetchone()
    
    # show reservation of this room
    def get_available_times(self, id, date):
        self.cursor.execute("""
                            SELECT t.start, t.end
                            FROM room_system.time t
                            WHERE t.day = %s
                            AND t.id NOT IN (
                                SELECT re.time_id
                                FROM room_system.reservation re
                                JOIN room_system.room r ON r.id = re.room_id
                                WHERE r.id = %s
                                AND re.time_id IS NOT NULL
                                AND re.room_id = r.id
                            );
                            """, (date,id))
        return self.cursor.fetchall()
    
    
    def delete_room(self, id):
        self.cursor.execute("""
                            DELETE FROM room_system.room
                            WHERE id = %s
                            """, (id,))
        self.__conn.commit()
    def create_room(self, roomName, capacity):
        self.cursor.execute("""
                            INSERT INTO room_system.room (name, capacity)
                            VALUES (%s, %s)
                            """, (roomName, capacity))
        self.__conn.commit()
    def get_room_by_name(self, name):
        self.cursor.execute("""
                            SELECT * FROM room_system.room
                            WHERE name = %s
                            """, (name,))
        return self.cursor.fetchall()