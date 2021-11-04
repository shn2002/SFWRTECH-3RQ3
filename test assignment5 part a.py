# -*- coding: utf-8 -*-
# Student Name: Henian Shan
# Student Number: 400418368

from stubs_traffic_light import TrafficLight


# When one traffic light is green the other must always be red.
#1. Briefly explain in acode comment on each file why the tests given are all necessary to test the requirement 
#2. and why the set you gave is sufficient to guarantee the system works as intended.
# This test covers all the senarios when the traffic light turn green
# According to the question 1, this pair of traffic light are partly exclusive
# The status can be RED-RED, RED-GREEN, GREEN-RED 
# The test cover 2 senarios.
# when main street traffic light is green side street traffic light is red.
# when side traffic light is green main street traffic light is red.

def test_traffic_light_turn_green():
    #inital twe traffic lights
    main_street_traffic_light = TrafficLight('NS','RED','Main')
    side_street_traffic_light = TrafficLight('WE','RED','Side')
    
    # pair these two lights
    main_street_traffic_light.pair(side_street_traffic_light)
    side_street_traffic_light.pair(main_street_traffic_light)
    
    #change the main street traffic light to green
    main_street_traffic_light.color='GREEN'
    #check if side street traffic light is red 
    assert side_street_traffic_light.color =='RED', "When main street traffic light is green, side street traffic light should be red"
    #change the side street traffic light to green
    side_street_traffic_light.color='GREEN'
    #check if main street traffic light is red 
    assert main_street_traffic_light.color=='RED' , "When side street traffic light is green, main street traffic light should be red"

