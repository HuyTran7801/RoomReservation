from DAO.reservation_DAO import *
from controller.time_service import *
import datetime

class BookService:
    def __init__(self):
        self.__reservation_dao = ReservationDAO()
        
    def show_all_reservations(self):
        return self.__reservation_dao.get_all_reservations()
    
    def add_new_reservation(self, booking):
        self.__reservation_dao.add_reservation(booking)
        
        
        
    
        