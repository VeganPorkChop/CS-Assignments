 # height.py - A program to convert height in feet and inches into inches
# Add your name
# Add today's date
feet = int(input("Please enter the number of feet:"))
inches = int(input("Please enter the number of inches:"))
total_inches = feet * 12 + inches
print("Height in inches:", total_inches)
print("Height in centimeters:", total_inches*2.54)
