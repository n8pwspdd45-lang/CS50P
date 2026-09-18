def main():
    first, op, second = input("Espression (with whitespaces): ").split()
    first = float(first)
    second = float(second)
    operation(first, op, second) # chiamo la funzione operation


def operation(first, op, second): # chiede come input first, op, second
    if op == "+":
        print("result =", round(first + second, 1))
    elif op == "-":
        print("result =", round(first - second, 1))
    elif op == "*":
        print("result =", round(first * second, 1))
    elif op == "/" :
        print("result =", round(first/second, 1))
    else:
        print("not valid")

main()
