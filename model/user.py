class User:
    def __init__(self, name, mail, password, phone):
        self.__name = name
        self.__mail = mail
        self.__password = password
        self.__phone = phone
        
        
    def get_name(self):
        return self.__name
    
    def get_mail(self):
        return self.__mail
    
    def get_password(self):
        return self.__password
    
    def get_phone(self):
        return self.__phone
    
    def set_name(self, name):
        self.__name = name
        
    def set_mail(self, mail):
        self.__mail = mail
        
    def set_password(self, password):
        self.__password = password
        
    def set_phone(self, phone):
        self.__phone = phone
        
    def show_user(self):
        return f"Name: {self.__name}, Mail: {self.__mail}, Phone: {self.__phone}"