from DAO.reservation_DAO import *
import datetime

class ReservationService:
    def __init__(self):
        self.__reservation_dao = ReservationDAO()

    def get_all_reservations(self):
        return self.__reservation_dao.get_all_reservations_detail()
    def deleteLateReservations(self):
        return self.__reservation_dao.delete_late_reservations()
    def deleteReservation(self, id):
        return self.__reservation_dao.delete_reservation(id)