import random

def gtn():
    ans = "y"
    while ans == "y":
        low = random.randint(0, 500)
        up = random.randint(500, 1000)
        main = random.randint(low, up)
        # print(main)
        print("The number is chosen and you only have 6 chances to guess that number.")
        live = 6
        guesses = 0
        while guesses < live:
            guesses += 1
            guess = int(input("Enter your guess : "))
            if guess == main:
                print("Congratulations, you have won the game in",
                      guesses, "guess(es).")
                ans = input("Do you want to play again (y/n) : ")
                break
            elif guess < main:
                print("The number is bigger than", guess,
                      "\nYou have", 6 - guesses, "lives left.")
            elif guess > main:
                print("The number is smaller than", guess,
                      "\nYou have", 6 - guesses, "lives left.")
        if guesses >= 6:
            print(
                "It seems that you run out of lives.\nThe number which was guessed is", main)
            ans = input("Do you want to play again (y/n) : ")
