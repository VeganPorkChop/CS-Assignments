# recieving string input from user
input_str = input()

total_chars = 0

# counting characters in the string
for char in input_str:
    if char != ' ' and char != '.' and char != ',' and char != '!':
        total_chars += 1
        
# displaying the total character count
print(total_chars)