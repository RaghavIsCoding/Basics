import time

name = input("Enter your name: ")
hour = int(time.strftime('%H'))
if hour >= 0 and hour < 10:
    print("Good morning {0}".format(name))
elif(hour > 10 and hour < 19):
    print("Good afternoon {}".format(name))
elif(hour > 20):
    print(f"Good night {name}")
print("The time is:", time.strftime("%H:%M:%S"))
