# -*- coding: utf-8 -*-

# Student Name: Henian Shan
# Student Number: 400418368

# direction --- has two value WE or NS
class Pedestrian:
    def __init__(self, direction ):
      self.__direction = direction

    # if pedestrian and traffic light are at same dirction and current traffic light is green, pedestrian can cross, otherwise no.
    def is_permitted_for_crossing( self, traffic_light): 
        if self.direction==traffic_light.direction:
            if traffic_light.color=='GREEN':
                return True  
        else:
            return False
  
    