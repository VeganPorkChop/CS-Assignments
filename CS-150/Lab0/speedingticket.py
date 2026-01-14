
#recieving inputs
speed_limit = int(input())
recorded_speed = int(input())

#calculating the price paid for speeding ticket
price = 0
if recorded_speed <= speed_limit-10:
    price += 50
if recorded_speed > speed_limit+40:
    price += 300
elif recorded_speed >= speed_limit+21:
    price += 150
elif recorded_speed >= speed_limit+6:
    price += 75

#printing the resulting speeding ticket price
print(price)