prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = get_the_order()
    print(f"\r-> Final Total: ${total:.2f}")

def get_the_order():

    tot = 0.00

    while True:
        try:
            x = prices[input("Item: ").title()]
            tot += x
            print(f"Total: ${tot:.2f}" )

        except KeyError:
            pass

        except EOFError:
            return tot

main()
