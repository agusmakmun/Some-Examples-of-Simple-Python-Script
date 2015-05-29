"""
Name             : Alarm with Timer
Created By       : Agus Makmun (Summon Agus)
Blog             : bloggersmart.net - python.web.id
License          : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
Documentation    : https://github.com/agusmakmun/Some-Examples-of-Simple-Python-Script/
Powered          : Python-2.7, mpg321

[+]--- use --- [+]
$sudo apt-get install mpg321
$python Alarm\ with\ Timer.py
"""

import time, os
break_time = 1

print 'The current time is: ', time.strftime('%H:%M:%S')
while True:
    try:
        inp_hour = raw_input('Enter hour of Alarm (ex: 02): ')
        inp_minute = raw_input('Enter minute of Alarm (ex: 20): ')
        break
    except:
        print 'Your Input is wrong!, please Integer'

print 'Waiting Alarm...'
while (break_time):
    timer = time.strftime('%H:%M:%S')
    hour = timer[:2]
    minute = timer[3:5]
    if hour == inp_hour and minute == inp_minute:
        os.system('mpg321 rest_alert.mp3')
        #print 'Alarm has been executed, Thank you ..'
        #break_time = 0

        #adding before break_time = 0
        print "Start alarm looping over short distances"
        count = 0
        maximum = 5 #for how many times will run
        time_minute = 60
        while True:
            print "Start alarm looping over short distances"
            count += 1
            if count == maximum:
                print 'Alarm has been executed, Thank you ..'
                break_time = 0
              
            time.sleep(time_minute)
            os.system('mpg321 rest_alert.mp3')
        
