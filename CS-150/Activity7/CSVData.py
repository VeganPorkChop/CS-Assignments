import csv

infile = open('scorecard-2.csv')
data = csv.reader(infile)
names = next(data)
max_score = 0
max_name = ""
for _ in range(len(names)):
    try:
        row = next(data)
        score = int(row[290])
        if score > max_score:
            max_score = score
            max_name = row[3]
    except:
        continue

print(f"The highest score is {max_score} by {max_name}")