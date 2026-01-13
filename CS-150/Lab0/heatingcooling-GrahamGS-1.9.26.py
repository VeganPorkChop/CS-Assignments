#setting global variables
warm_days = 0
cold_days = 0

try:
    #recieving temperature from user until they type something that isnt a number
    while True:
        temp = int(input("Enter the temperature (or type something that isnt a number or anything less than -459F): "))
        if temp > 80:
            warm_days += 1
        elif temp < 60:
            cold_days += 1
        elif temp < -459:
            raise ValueError
        
except ValueError:
    #printing the results
    print(f"Number of warm days (above 80): {warm_days}")
    print(f"Number of cold days (below 60): {cold_days}")

