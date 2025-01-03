class ListWaiting:
    def __init__(self, id, name_room, capacity, day, start, end):
        self.__id = id
        self.__name_room = name_room
        self.__capacity = capacity
        self.__day = day
        self.__start = start
        self.__end = end
        
    def get_id(self):
        return self.__id
    
    def get_name_room(self):
        return self.__name_room
    
    def get_capacity(self):
        return self.__capacity
    
    def get_day(self):
        return self.__day
    
    def get_start(self):
        return self.__start
    
    def get_end(self):
        return self.__end