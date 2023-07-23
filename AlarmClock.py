import time
import datetime
import re
from beepy.make_sound import beep


def inpt():
    check = True
    while check:
        set_time = input("ENTER the TIME in 24-HOUR format(HH:MM:SS):\n>>> ")
        alarm_time = [int(n) for n in set_time.split(':')]

        if re.search('\d\d:\d\d:\d\d',set_time):
            if alarm_time[0] < 0:
                check = True
            elif alarm_time[1] > 60:
                check = True
            elif alarm_time[2] > 60:
                check = True

            else:
                check = False
                break


        if re.search('\d\d:\d\d',set_time):
            
            alarm_time.append(0)
            set_time = set_time + ':00'
            if alarm_time[0] < 0:
                check = True
            elif alarm_time[1] > 60:
                check = True
            elif alarm_time[2] > 60:
                check = True

            else:
                check = False
                break
        else:
            print("INVALID")

        
        
        
        
        if re.search('\d\d',set_time):
            alarm_time.append(0)
            alarm_time.append(0)
            
            set_time = set_time + ':00' + ':00'
            
            if alarm_time[0] < 0:
                check = True
            elif alarm_time[1] > 60:
                check = True
            elif alarm_time[2] > 60:
                check = True

            else:
                check = False
                break


    return set_time 


def alarm1(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        print(current_time)
        print(alarm_time)
        if alarm_time == current_time:
            print("BEEP")
            for x in range(5):
                beep(5)
                time.sleep((1))
            
            break


if __name__ == '__main__':
    time1 = inpt()
    alarm1(time1)