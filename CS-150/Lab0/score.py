#program start
dnaFirst = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol):")
dnaSecond = input("Please enter DNA sequence (using uppercase letters A, T, C, G and an indel symbol):")
score = 0

for i in range(min(len(dnaFirst), len(dnaSecond))):
    if dnaFirst[i] == dnaSecond[i]:
        score += 1
if score == 1:
    print(f"{score} match found between {dnaFirst} and {dnaSecond}")
else:
    print(f"{score} matches found between {dnaFirst} and {dnaSecond}")