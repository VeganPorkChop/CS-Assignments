#These are the story inputs
first = input("Write down a Person: ")
second = input("Write down a Number: ")
third = input("Write down a Noun: ")
fourth = input("Write down a Place: ")  

#this is a the error handling for the inputs, just incase the madlibs user cant follow instructions
try:
    #These are the type checks for each input
    str(first)
    float(second)
    str(third)
    str(fourth)

    #This is the full story output
    print(f"Here is your story:\nOne day, {first} was walking through the park when they stumbled upon a mysterious box. \nCurious, {first} opened the box and found {second} {third}s inside! \nExcited by the discovery, {first} decided to take the box to {fourth} to show their friends. \nLittle did they know, this box would change their life forever...\n")
except (TypeError, ValueError):
    print("Your story could not be generated, please check your inputs and try again.")