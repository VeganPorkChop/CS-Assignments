# this a validating function for DNA strings. it makes sure that the strings only contain A, T, C, G, or - characters
def validate(dna_string):
    for char in dna_string:
        if char not in "ATCG-":
            return False
    return True

#this defines the prompting because it shows up multiple times in the program so its better to have it as a function
def promt():
    dnaFirst = input("Enter the first DNA string: ")
    dnaSecond = input("Enter the second DNA string: ")
    score = 0
    return dnaFirst, dnaSecond, score


#this is the start of the main program
print("Hello, and welcome to the DNA allignment program!")
dnaFirst, dnaSecond, score = promt()

#looping through  the menu options until the user decides to quit
while True:
    data = input("Please select an option below: \n'u' to update the DNA string \n's' to score allignment\n'q' to quit the program \n")
    #quitting the program
    if data == 'q':
        print("Thank you for using the DNA allignment program, goodbye!")
        break

    #updating the DNA strings using prompt function
    if data == 'u':
        dnaFirst, dnaSecond, score = promt()

    #scoring the DNA strings
    if data == 's':
        if not validate(dnaFirst) or not validate(dnaSecond):
            print("One or both DNA strings are invalid. Please update the DNA strings.")
            continue
        for i in range(min(len(dnaFirst), len(dnaSecond))):
            if dnaFirst[i] == dnaSecond[i]:
                score += 1

        print(f"The score is: {score}")