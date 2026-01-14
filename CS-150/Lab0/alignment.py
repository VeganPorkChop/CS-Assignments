# this a validating function for DNA strings. it makes sure that the strings only contain A, T, C, G, or - characters
def validate(dna_string):
    if len(dna_string) == 0:
        return False
    for char in dna_string:
        if char not in "ATCG-":
            return False
    return True

#this defines the prompting because it shows up multiple times in the program so its better to have it as a function
def promt():
    dnaFirst = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
    dnaSecond = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol): ")
    print(f"You entered:\n{dnaFirst}\n{dnaSecond}")
    return dnaFirst, dnaSecond


#this is the start of the main program
print("Hello and welcome to DNA sequence alignment program!")
dnaFirst, dnaSecond = promt()
score = 0

#looping through  the menu options until the user decides to quit
while True:
    data = input("Select one of the following commands:\n'u' to update sequences\n's' to score the alignment\n'q' to quit\n")
    #quitting the program
    if data == 'q':
        print("Thank you! Goodbye!")
        break

    #updating the DNA strings using prompt function
    if data == 'u':
        dnaFirst, dnaSecond = promt()

    #scoring the DNA strings
    if data == 's':
        if not validate(dnaFirst) or not validate(dnaSecond):
            print("Invalid DNA sequences entered, please re-enter sequences")
            continue
        for i in range(min(len(dnaFirst), len(dnaSecond))):
            if dnaFirst[i] == dnaSecond[i]:
                score += 1
        if score == 1:
            print(f"{score} match found between {dnaFirst} and {dnaSecond}")
        else:
            print(f"{score} matches found between {dnaFirst} and {dnaSecond}")
        score = 0