class Time:
    def __init__(self, start_time, end_time, day):
        self.__start_time = start_time
        self.__end_time = end_time
        self.__day = day
    def get_start_time(self):
        return self.__start_time
    def get_end_time(self):
        return self.__end_time
    def get_day(self):
        return self.__day
    