#input from user
number = input("Enter price history: ")
for i in number:
    lowest_price = int(number[0])
    highest_price = int(number[0])
    if int(i) < lowest_price:
        lowest_price = int(i)
    if int(i) > highest_price:
        highest_price = int(i)
    

#print line for output
print(f"Profit: {highest_price - lowest_price}")