# from model.room import *
from DAO.room_DAO import *
from controller.search_room_service import *
import datetime
from controller.time_service import *

TimeService = TimeService()
response = TimeService.show_time_detail('2025-01-04', '8:00:00', '9:59:00')
print(response[0])

