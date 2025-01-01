class Room:
    def __init__(self, name, capacity, status):
        self.__name = name
        self.__capacity = capacity
        self.__status = status
        
    def get_name(self):
        return self.__name
    
    def get_capacity(self):
        return self.__capacity
    
    def get_status(self):
        return self.__status
    
    def set_name(self, name):
        self.__name = name
    
    def set_capacity(self, capacity):
        self.__capacity = capacity
        
    def set_status(self, status):
        self.__status = status    
        
    def show_room(self):
        return f"Name: {self.__name}, Capacity: {self.__capacity}, Status: {self.__status}"