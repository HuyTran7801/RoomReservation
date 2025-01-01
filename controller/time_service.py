from DAO.time_DAO import *

class TimeService:
    def __init__(self):
        self.__time_dao = TimeDAO()
    def show_all_times(self):
        return self.__time_dao.get_all_times()
        
    def show_time_detail(self, time):
        return self.__time_dao.get_time_detail(time)
    
    def delete_over_time(self, time_id):
        self.__time_dao.delete_over_time(time_id)
        
    def add_time(self, time):
        return self.__time_dao.add_time(time)
    def delete_time(self, time_id):
        return self.__time_dao.delete_time(time_id)
