# from model.room import *
from DAO.room_DAO import *
from controller.search_room_service import *
import datetime


room_service = SearchRoomService()
rooms = room_service.search_all_rooms()
# print(rooms)
for i in rooms:
    print(i)
print(type(rooms))
# for i in rooms:
#     print(i)
# # print(rooms)
# current = datetime.datetime.now().replace(microsecond=0)
# print(current.year, ' ',current.month, ' ', current.day, ' ', current.hour, ' ', current.minute, ' ',current.second)
# print(current)

# current_time =  '2025-12-31 14:00:00'
# print(type(current_time))

# current_str = f'{current.year}-{current.month}-{current.day} {current.hour}:{current.minute}:{current.second}'
# print(type(current_str))