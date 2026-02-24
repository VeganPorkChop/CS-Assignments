import matplotlib.pyplot as plt
import csv

file = open("scorecard-2.csv")
data = csv.reader(file)
line = next(data)
i =0
numbers = []
while True:
    try:
        line = next(data)
        numbers.append(int(line[290]))
        i +=1
        print(f"try {i}")
    except ValueError as e:
        continue
    except:
        break

plt.hist(numbers)
plt.show()