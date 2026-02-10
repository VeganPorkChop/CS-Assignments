from pdb import main
import random
import json

lst = list()

def setup():
    file = open("progress.json", "a")
    file.close()

def reset_progress():
    file = open("progress.json", "w")
    file.write("")
    file.close()

def get_random_country_txt():
    file = open("countries.txt", "r")
    countries = file.read().splitlines()
    file.close()
    return random.choice(countries)

def get_random_country_json():
    with open("states.json", "r") as file:
        countries = json.loads(file.read())
    countries_copy = countries.copy()
    for country in lst:
        countries_copy.pop(list(country.keys())[0])
    for country in lst:
        countries.pop(list(country.keys())[0])
    random_country = random.choice(list(countries_copy.keys()))
    return random_country, countries_copy[random_country]

def setup():
    # Ensure the file exists and contains valid JSON (an empty list)
    try:
        with open("progress.json", "r") as f:
            json.load(f)
    except:
        with open("progress.json", "w") as f:
            json.dump([], f)

def reset_progress():
    with open("progress.json", "w") as f:
        json.dump([], f)

def track_answer(new_items):
    with open("progress.json", "r") as f:
        try:
            old = json.load(f)
        except:
            old = []

    old.extend(new_items)

    with open("progress.json", "w") as f:
        json.dump(old, f, indent=2)

        
def print_title():
    print()
    print("==========================================")
    print("      COUNTRY → CAPITAL CHALLENGE")
    print("==========================================")
    print()

def print_instructions():
    print("------------------------------------------")
    print(" Guess the capital of the given country.")
    print(" Type 'quit' at any time to exit the game.")
    print("------------------------------------------")
    print()

def print_score(right, wrong):
    print("------------------------------------------")
    print(f" Score: {right} correct, {wrong} wrong")
    print("------------------------------------------")

def new_round():
    random_country, random_capitol = get_random_country_json()

    print()
    print("------------------------------------------")
    print(f" COUNTRY:  {random_country.upper()}")
    print("------------------------------------------")

    guess = input(" Capital? > ").lower()
    return guess.lower(), random_capitol, random_country

def check_win(right, wrong):
    if right >= 10:
        print()
        print("==========================================")
        print("      CONGRATULATIONS! YOU WIN!          ")
        print("==========================================")
        return True
    elif wrong >= 10:
        print()
        print("==========================================")
        print("      GAME OVER! BETTER LUCK NEXT TIME!  ")
        print("==========================================")
        return True
    return False
    

def frq():
    print_title()
    print_instructions()

    right = 0
    wrong = 0
    guess = ""
    while guess != "quit":
        guess, random_capitol, random_country = new_round()
        print(guess, random_capitol)
        if guess == random_capitol.lower():
            print()
            print("**********************************")
            print("*          CORRECT!              *")
            print("**********************************")
            lst.append({random_country: random_capitol})
            right += 1
        else:
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x          WRONG                 x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            wrong += 1
            guess = input(" Try again  for half credit or type 's' to skip > ").lower()
            if guess == "s":
                print()
                print("**********************************")
                print(f"* The correct answer was: {random_capitol.upper()} *")
                print("**********************************")
            elif guess == random_capitol.lower():
                print()
                print("**********************************")
                print("*          CORRECT!              *")
                print("**********************************")
                lst.append({random_country: random_capitol})
                right += 0.5
            else:
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("x          WRONG AGAIN           x")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                wrong += 1
        print_score(right, wrong)
        if check_win(right, wrong):
            track_answer(lst)
            with open ("progress.json", "r") as data:
                length = len(json.load(data))
            print(f"You have mastered {length} countries so far!")
            if input(" Reset Progress? (y/n) > ").lower() == "y":
                reset_progress()
                setup()
            if input(" Play Again? (y/n) > ").lower() == "y":
                main()
            break

def options():
    file = open("countries.txt", "r")
    countries = file.read().splitlines()
    file.close()
    for i in range(len(countries)):
        countries[i] = countries[i].split("@")
    options_list = random.sample(countries, 4)
    correct_choice = random.choice(options_list)
    return options_list, correct_choice

def new_round_mcq():
    [[optionA, optionB, optionC, optionD], correct_choice] = options()

    print()
    print("------------------------------------------")
    print(f" COUNTRY:  {correct_choice[0].upper()}")
    print("------------------------------------------")
    print("Which is the capital?")
    print(f"1. {optionA[1]}")
    print(f"2. {optionB[1]}")
    print(f"3. {optionC[1]}")
    print(f"4. {optionD[1]}")

    guess = input("Enter your answer (1-4) or 'quit' to exit > ").lower()
    return guess, optionA, optionB, optionC, optionD, correct_choice


def is_correct_mcq(guess, optionA, optionB, optionC, optionD, correct_choice):
    if guess == "1":
        return optionA == correct_choice
    elif guess == "2":
        return optionB == correct_choice
    elif guess == "3":
        return optionC == correct_choice
    elif guess == "4":
        return optionD == correct_choice
    return False


def mcq():
    print_title()
    print_instructions()

    right = 0
    wrong = 0
    guess = ""

    while guess != "quit":
        guess, optionA, optionB, optionC, optionD, correct_choice = new_round_mcq()
        if is_correct_mcq(guess, optionA, optionB, optionC, optionD, correct_choice):
            print()
            print("**********************************")
            print("*          CORRECT!              *")
            print("**********************************")
            lst.append({correct_choice[0]: correct_choice[1]})
            right += 1
        else:
            print()
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("x          WRONG                 x")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            wrong += 1

            guess2 = input("Try again for half credit or type 's' to skip > ").lower()

            if guess2 == "quit":
                guess = "quit"
                break

            if guess2 == "s":
                print()
                print("**********************************")
                print(f"* The correct answer was: {correct_choice[1].upper()} *")
                print("**********************************")
            elif is_correct_mcq(guess2, optionA, optionB, optionC, optionD, correct_choice):
                print()
                print("**********************************")
                print("*          CORRECT!              *")
                print("**********************************")
                lst.append({correct_choice[0]: correct_choice[1]})
                right += 0.5
            else:
                print()
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("x          WRONG AGAIN           x")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                wrong += 1

        print_score(right, wrong)

        if check_win(right, wrong):
            track_answer(lst)
            with open("progress.json", "r") as data:
                length = len(json.load(data))
            print(f"You have mastered {length} countries so far!")
            if input(" Reset Progress? (y/n) > ").lower() == "y":
                reset_progress()
                setup()
            if input(" Play Again? (y/n) > ").lower() == "y":
                main()
            break
    
def main():
    option = input("Choose a game mode: (1) Free Response, (2) Multiple Choice > ")
    if option == "1":
        frq()
    elif option == "2":
        mcq()
    else:
        print("Invalid input. Please try again.")
        main()

if __name__ == "__main__":
    setup()
    main()

        
