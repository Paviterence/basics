# Conditional statement
# if pavi reachs railway station before 5 mins ------> catch up the train
# else  train missed

# time=? , train departure time

time=float(input("enter the reach time"))

if (time==9.50):
	print("train ah puduchuruva")
elif(time<=9.50):
	print("kandipa train ah puduchuruva")
elif(time>=9.51 and time<=9.55):
	print("pudikirathu kashtam vema platform ku ponum.")
elif(time>=9.56 and time<10):
	print("train ah pudukirathu kashtam")
else:
	print('train ah kelambiruchu')