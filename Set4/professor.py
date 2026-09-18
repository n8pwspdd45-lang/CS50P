import random

def main():
    level = get_level()
    print(generate_integer(level))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    correct = 0
    for _ in range(10):
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        else:
            x = random.randint(10**(level-1), 10**(level)-1)
            y = random.randint(10**(level-1), 10**(level)-1)

        somma = x + y
        tentativi_rimasti = 3

        while tentativi_rimasti > 0:
            try:
                result = int(input(f"{x} + {y} = "))
                if result != somma:
                    print("EEE")
                    tentativi_rimasti -= 1
                else:
                    correct += 1
                    break

            except ValueError:
                continue

        if tentativi_rimasti == 0:
            print(f"{x} + {y} = {somma}")

    return correct

if __name__ == "__main__":
    main()
