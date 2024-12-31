# from model.user import *
from DAO.user_DAO import *

class LoginService:
    def __init__(self):
        self.__user_DAO = UserDAO()
        
    def validate_login(self, name, password):
        res = self.__user_DAO.get_user_by_name_and_password(name, password)
        if res is not None:
            return True
        return False
    
    def validate_sign_up(self, name, mail, password, phone):
        res_mail = self.__user_DAO.get_user_by_mail(mail)
        res_phone = self.__user_DAO.get_user_by_phone(phone)
        if res_mail is None and res_phone is None:
            self.__user_DAO.add_user(name, mail, password, phone)
            return True
        return False
    
    def show_user_detail(self, name, password):
        return self.__user_DAO.get_user_by_name_and_password(name, password)
    