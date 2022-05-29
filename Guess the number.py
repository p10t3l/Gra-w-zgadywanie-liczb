import random


def user_number():
    while True:
        try:
            choice = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")
    return (choice)


def guess():
    computer_choice = random.randint(1, 100)
    player_number = user_number()
    while player_number != computer_choice:
        if player_number < computer_choice:
            print("To small.")
        else:
            print("To big.")
        player_number = user_number()
    print("You win!")


if __name__ == '__main__':
    guess()
