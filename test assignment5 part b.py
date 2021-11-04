# -*- coding: utf-8 -*-
# Student Name: Henian Shan
# Student Number: 400418368

from stubs_traffic_light import TrafficLight
from stubs_pedestrian import Pedestrian


# When one traffic light is green the other must always be red.
#1. Briefly explain in acode comment on each file why the tests given are all necessary to test the requirement 
#2. and why the set you gave is sufficient to guarantee the system works as intended.    
# This test covers all the senarios when pedestrian would like to cross street
# two parameters to determine if pedestrian can pass the street
#so there are four senarios
#1.street and pedestrian are at same directions and that traffic light is green
#2.street and pedestrian are at same directions and that traffic light is red
#1.street and pedestrian are not at same directions and that traffic light is green
#1.street and pedestrian are not at same directions and that traffic light is red

def test_pedestrian_cross_street():
    #inital twe traffic lights and one pedestrian
    main_street_traffic_light = TrafficLight('NS','RED','Main')
    side_street_traffic_light = TrafficLight('WE','RED','Side')
    pedestrian= Pedestrian('WE')
    # pair these two lights
    main_street_traffic_light.pair(side_street_traffic_light)
    side_street_traffic_light.pair(main_street_traffic_light)
    
    #1. test if traffic light and pedestrian are same direction but that traffic light is red
    side_street_traffic_light.color='RED'
    assert pedestrian.is_permitted_for_crossing(side_street_traffic_light) == False, "traffic light and pedestrian are at same direction but that traffic light is red can't cross"
    #2. test if traffic light and pedestrian are same direction and that traffic light is green
    side_street_traffic_light.color='GREEN'
    assert pedestrian.is_permitted_for_crossing(side_street_traffic_light) == True, "traffic light and pedestrian are at same direction, that traffic light is green can cross"
    #3.test if traffic light and pedestrian are not same direction and that traffic light is red
    main_street_traffic_light.color='RED'
    assert pedestrian.is_permitted_for_crossing(main_street_traffic_light) == False, "traffic light and pedestrian are not at same direction but can't cross"
    #3.test if traffic light and pedestrian are not same direction and that traffic light is red
    main_street_traffic_light.color='GREEN'
    assert pedestrian.is_permitted_for_crossing(main_street_traffic_light) == False, "traffic light and pedestrian are not at same direction even though traffic light is green but can't cross"
    
    