import random

number = random.randint(1, 100)
guess = 0
tries = []

while guess != number:
    if guess < number:
        print("Pamēģini lielāku skaitli.")
    else:
        print("Pamēģini mazāku skaitli.")

    guess = int(input("Uzmini skaitli: "))
    tries.append(guess)
else:
    print(f"You won from {len(tries)} tries!")
    print("Here is your guessing history:")
    print(tries)

    sum_of_difference = 0
    
    for t in tries:
        sum_of_difference += abs(t - number)
    
    print(f"Average difference was {sum_of_difference/len(tries)}")