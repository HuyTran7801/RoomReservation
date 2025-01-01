from DAO.room_DAO import *
import datetime

class SearchRoomService:
    def __init__(self):
        self.__room_dao = RoomDAO()
        
    def search_all_rooms(self):
        return self.__room_dao.get_all_rooms()
    
    def show_available_times(self, id, date):
        return self.__room_dao.get_available_times(id, date)
    
    def search_room_detail(self, id):
        return self.__room_dao.get_room_detail(id)
    
    def delete_room(self, id):
        self.__room_dao.delete_room(id)
    def create_room(self, roomName, capacity):
        self.__room_dao.create_room(roomName, capacity)
    def search_room_by_name(self, name):
        return self.__room_dao.get_room_by_name(name)