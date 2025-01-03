class Room:
    def __init__(self, id, capacity, name):
        self.__id = id
        self.__name = name
        self.__capacity = capacity
        
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name
    
    def get_capacity(self):
        return self.__capacity

    def set_name(self, name):
        self.__name = name
    
    def set_capacity(self, capacity):
        self.__capacity = capacity
        
        
    def show_room(self):
        return f"Name: {self.__name}, Capacity: {self.__capacity}"