#setting global variables
warm_days = 0
cold_days = 0
#recieving temperature from user until they type something that isnt a number
while True:
    temp = int(input("Enter the average daily temperature: "))
    if temp > 80:
        cold_days += 1
    if temp < -459:
        #printing the results and exiting the program
        print(f"Heating Days: {warm_days}")
        print(f"Cooling Days: {cold_days}")
        exit()
    if temp < 60:
        warm_days += 1