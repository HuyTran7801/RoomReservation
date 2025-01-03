# from model.user import *
from DAO.user_DAO import *
from model.account import Account
from model.user import User

class LoginService:
    def __init__(self):
        self.__user_DAO = UserDAO()
        
    def validate_login(self, account):
        res = self.__user_DAO.get_user_by_name_and_password(account)
        if res is not None:
            return True
        return False
    
    def validate_sign_up(self, user):
        res_mail = self.__user_DAO.get_user_by_mail(user.get_mail())
        res_phone = self.__user_DAO.get_user_by_phone(user.get_phone())
        if res_mail is None and res_phone is None:
            self.__user_DAO.add_user(user)
            return True
        return False
    
    def show_user_detail(self, account):
        return self.__user_DAO.get_user_by_name_and_password(account)
    