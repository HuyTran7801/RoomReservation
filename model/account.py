class Account:
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        
    def get_name(self):
        return self.__name
    def get_password(self):
        return self.__password