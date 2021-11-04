# -*- coding: utf-8 -*-
# Student Name: Henian Shan
# Student Number: 400418368

# direction --- has two value WE or NS
# color     --- has two value Red or Green
# road_type --- has two value Main or Side 
# duration  --- how long has the current status lasted initial value is 0
# is_wait -- any car currently wait boolean True or False
# is_vehicle_passed -- all vehicle passed boolean True or False
# time_stamp --- the time stamp for last vehicle passed street
class TrafficLight:
    #constructor
    def __init__(self, direction, color, road_type, duration = 0, is_wait = False,time_stamp = 0  ):
      self.__direction = direction
      self.__color = color
      self.__road_type = road_type
      self.__duration = duration
      self.__is_wait = is_wait
      self.__time_stamp = time_stamp
    # pair the Main street and side street traffic light   
    def pair(self, traffic_light):      
        return None  
  
    