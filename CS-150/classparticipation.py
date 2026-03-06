def mySum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + mySum(lst[1:])

assert 3 == mySum([1, 2])

def stringReverse(s):
    if len(s) == 1:
        return s
    return s[len(s)-1: len(s)] + stringReverse(s[0: len(s)-1])

assert "racecar" == stringReverse("racecar")

def drinkingAge(lst, age):
    if lst[0] < age:
        return lst[0].append(drinkingAge(lst[1:], age))
    if lst[0] >= age:
        return drinkingAge(lst[1:], age).append(lst[0])
    if len(lst) == 1:
        return lst[0]
    
drinkingAge([1, 5, 4, 3, 2, 0, 5, 432,62, 36, 46, 3, 5, 6, 5, 434], 18)
        