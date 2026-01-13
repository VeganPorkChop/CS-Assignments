#input for DNA string validation
dnaString = input("Enter a DNA string: ")

#validate DNA string
for char in dnaString:
    if char not in "ATCG-":
        print("Invalid DNA string")
        #quits if invalid DNA string
        exit()
else:
    print(f"{dnaString.upper()} is a valid DNA string, make sure you only use A, T, C, and G characters.")
