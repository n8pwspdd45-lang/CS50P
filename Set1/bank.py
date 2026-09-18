def main():
    greeting = input("Greeting: ").lower().strip()
    print(value(greeting))


def value(greeting):
    if greeting[0:5] == "hello":
        return "$0"
    elif greeting[0] == "h" and greeting[0:5] != "hello":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()
