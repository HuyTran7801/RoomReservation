from DAO.waiting_DAO import *

class WaitingService:
    def __init__(self):
        self.__waiting_dao = WaitingDAO()
        
    def add_to_waiting_list(self, user_id, room_id, time_id):
        self.__waiting_dao.add_waiting_list(user_id, room_id, time_id)
        
    def show_all_waiting_list(self, user_id):
        return self.__waiting_dao.get_all_waiting_list(user_id)
    
    def delete_from_waiting_list(self, id):
        self.__waiting_dao.delete_waiting_list(id)
        
    def check_exist_waiting_list(self, user_id, room_id, time_id):
        check = self.__waiting_dao.get_waiting_list_detail(user_id, room_id, time_id)
        if check is None:
            return True
        return False
    
    def show_all_waiting_list_total(self):
        return self.__waiting_dao.get_all_waiting_list_total()
    
    def delete_same_from_waiting_list(self, room_id, time_id):
        self.__waiting_dao.delete_same_waiting_list(room_id, time_id)
    def show_booking_deny_list(self, user_id):
        return self.__waiting_dao.get_booking_deny_list(user_id)
    def reject_waiting_list(self, id):
        self.__waiting_dao.reject_waiting_list(id)
    def get_all_deny_list(self):
        return self.__waiting_dao.get_all_deny_list()
    