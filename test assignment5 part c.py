# -*- coding: utf-8 -*-
# Student Name: Henian Shan
# Student Number: 400418368

from stubs_traffic_light import TrafficLight
import time
 
# When one traffic light is green the other must always be red.
#1. Briefly explain in a code comment on each file why the tests given are all necessary to test the requirement 
#2. and why the set you gave is sufficient to guarantee the system works as intended.    

#1. first question is The traffic light should be green for the main road unless traffic has been waiting on the side street for more than 90s
# there are two parameters to detemine if the main street traffic light should turn red
# side street is any car waiting and how long is has been waiting, total is 4 senarios

# 1) Car wait more than 90s
# 2) Car wait less than 90s, 
# 3) No car wait more than 90s
# 4) No car wait less than 90s
def test_main_street_traffic_light_turn_red():
    #inital twe traffic lights and one pedestrian
    main_street_traffic_light = TrafficLight('NS','GREEN','Main')
    side_street_traffic_light = TrafficLight('WE','RED','Side')
    #pair these two lights
    main_street_traffic_light.pair(side_street_traffic_light)
    side_street_traffic_light.pair(main_street_traffic_light)
    #change main street to green and set side street traffic light wait is 
    
    # test if the main street if traffic has been waiting on the side street for more than 90s
    main_street_traffic_light.color='GREEN'
    side_street_traffic_light.is_wait = True
    side_street_traffic_light.duration = 90
    assert main_street_traffic_light == 'RED', "main street traffic light should turn red when cars waiting on side street more than 90s"
    main_street_traffic_light.color='GREEN'
    side_street_traffic_light.is_wait = True
    side_street_traffic_light.duration = 60
    assert main_street_traffic_light == 'GREEN', "main street traffic light should be green when cars waiting on side street less than 60s"
    side_street_traffic_light.is_wait= False
    side_street_traffic_light.duration = 90
    assert main_street_traffic_light == 'GREEN', "main street traffic light should be green when no cars waiting on side street"
    side_street_traffic_light.duration = 60
    assert main_street_traffic_light == 'GREEN', "main street traffic light should be green when no cars waiting on side street"
     #time_stamp last vehicle passed exact time   
 
#2. second question test main street traffic light should be red and the side street light green until 30s after all traffic on the side street has cleared
# there are two parameters to detemine if the main street traffic light should kept green  
# 1) Currently side street traffic light is green and time stamp shows after last car crossed, it past less than 30s
# 2) Currently side street traffic light is green and time stamp shows after last car crossed, it past more than 30s
# 3) Currently car is still waiting for crossing and time stamp for last car crossing is zero
def test_main_street_traffic_light_keep_red():
    #inital twe traffic lights and one pedestrian
    main_street_traffic_light = TrafficLight('NS','RED','Main')
    side_street_traffic_light = TrafficLight('WE','GREEN','Side')
    #pair these two lights
    main_street_traffic_light.pair(side_street_traffic_light)
    side_street_traffic_light.pair(main_street_traffic_light)
    
    
    side_street_traffic_light.color='GREEN'
    #time stamp is less than current time
    side_street_traffic_light.times_stamp = time.time()-20
    assert main_street_traffic_light == 'RED',"main street should be red because the last car crossed just less than 30s "
    side_street_traffic_light.times_stamp = time.time()-30
    assert main_street_traffic_light == 'GREEN',"main street should be green because the last car crossed more than 30s "
    side_street_traffic_light.times_stamp= 0
    assert main_street_traffic_light == 'RED',"car is still waiting for crossing the side street "
    
    
    