import random

def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                number = random.randint(1, n+1)
                print(number)
                break
        except ValueError:
            pass
    print(guessgame(number))


def guessgame(number):

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess > number:
                    print("Too large!")
                elif guess < number:
                    print("Too small!")
                else:
                    return "Just right!"

        except ValueError:
            pass

main()
