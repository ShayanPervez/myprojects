from random import randint
while True:
    random_number = randint(1, 10)
    guess = int(input("enter the number between 1 and 10: "))
    if guess == random_number:
        print("You Win!")
        ans = input("Do you wnat to play again?(y/n)").lower()
        if ans == "y":
            random_number = randint(1,10)
            guess = None
        elif ans == "n":
            print("Thank you!! for playing ")
            break
        else:
            print("Please enter the correct choice among (y/n)!! ")


    ans = input("Do you wnat to play again?(y/n)").lower()
    elif guess > random_number:
        print("Too High!!")
    else:
        print("Too Low")






