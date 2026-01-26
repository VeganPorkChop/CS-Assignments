name_list = open("names.txt", "r")

for names in name_list:
    print(names.split()[1])