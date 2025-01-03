class WaitingList:
    def __init__(self, user_id, room_id, time_id, status):
        self.__user_id = user_id
        self.__room_id = room_id
        self.__time_id = time_id
    
    def get_user_id(self):
        return self.__user_id
    def get_room_id(self):
        return self.__room_id
    def get_time_id(self):
        return self.__time_id
    
    def get_id(self):
        return self.__id
    
    def get_status(self):
        return self.__status
    