class ReservationDetail:
    def __init__(self, id, user_id, room_id, time_id, user_name, user_mail, room_name, capacity, day, start, end):
        self.__id = id
        self.__user_id = user_id
        self.__room_id = room_id
        self.__time_id = time_id
        self.__user_name = user_name
        self.__user_mail = user_mail
        self.__room_name = room_name
        self.__capacity = capacity
        self.__day = day
        self.__start = start
        self.__end = end
        
    def get_id(self):
        return self.__id
    def get_user_id(self):
        return self.__user_id
    def get_room_id(self):
        return self.__room_id
    def get_time_id(self):
        return self.__time_id
    def get_user_name(self):
        return self.__user_name
    def get_user_mail(self):
        return self.__user_mail
    def get_room_name(self):
        return self.__room_name
    def get_capacity(self):
        return self.__capacity
    def get_day(self):
        return self.__day
    def get_start(self):
        return self.__start
    def get_end(self):
        return self.__end
    