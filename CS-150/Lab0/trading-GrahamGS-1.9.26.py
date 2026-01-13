try:
    #input from user
    number = input("Enter stock string: ")
    for i in number:
        lowest_price = int(number[0])
        highest_price = int(number[0])
        if int(i) < lowest_price:
            lowest_price = int(i)
        if int(i) > highest_price:
            highest_price = int(i)
        

    #print line for output
    print(f"Profit: {highest_price - lowest_price}\nBuy on day of price: {lowest_price}\nSell on day of price: {highest_price}")

#checking to make sure every char is an integer
except (TypeError, ValueError):
    print("Your stock string could not be processed, please check your input and try again.")