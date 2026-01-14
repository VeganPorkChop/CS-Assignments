#input for DNA string validation
dnaString = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")

#validate DNA string
for char in dnaString:
    if char not in "ATCG-" or char.isspace():
        print(f"{dnaString} is not a valid DNA sequence")
        #quits if invalid DNA string
        exit()
if len(dnaString) == 0:
    print(f"{dnaString} is not a valid DNA sequence")
    exit()
print(f"{dnaString.upper()} is a valid DNA sequence")
