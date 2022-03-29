
#to find the aircraft status using aircraft departure status  based on speed
a=int(input("eneter the speed of the aircraft in knots :"))
if(a>=150 and a<=170):
    print("aircraft is able to takeoff")
elif(a>=171 and a<=1000):
    print("aircraft is on the sky")
elif(a>=1 and a<=30):
    print("aircraft is taxing or going to the runway")
elif(a>=30 and a<=149):
    print("aircraft is on the runway reaching vroll(takeoff speed speed)")
else:
    print("aircraft is on ground or in the ramp")

#to check the bike speed is normal or over speed for traffice penalty
speed=int(input("captured vehicle speed(kmph)in radar speed gun or camera :"))
if(speed>=1 and speed<=40):
    print("safe speed in city limit go ahead")
elif(speed>=41 and speed<=60):
    print("normal speed in city limit go ahead")
elif(speed>=61 and speed<=80):
    print("over speed warning")
elif(speed>=81):
    print("over speed in city limit penalty applicable capture the number plate")
else:
    print("bike is stopped")
#if else
x=int(input('enter the value of x :'))
if x in range(1,10):
    print(x)
else:
    print("not in range")
