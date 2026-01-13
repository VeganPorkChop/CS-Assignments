#this function checks the strings to make sure they are valid DNA strings with acceptable characters
def validate(dna_string):
    for char in dna_string:
        if char not in "ATCG-":
            return False
    return True

#program start
dnaFirst = input("Enter the first DNA string: ")
dnaSecond = input("Enter the second DNA string: ")
score = 0

#checks validity of DNA strings before scoring
if not validate(dnaFirst) or not validate(dnaSecond):
    print("One or both DNA strings are invalid. Please update the DNA strings.")
    exit()
for i in range(min(len(dnaFirst), len(dnaSecond))):
    if dnaFirst[i] == dnaSecond[i]:
        score += 1

print(f"The score is: {score}")