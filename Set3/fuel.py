def main():
    fraction = how_much_fuel()
    print(fraction)


def how_much_fuel():
    while True:
        try:
            x, y = input("Fraction: ").split('/')
            x = int(x)
            y = int(y)

            if x >= 0 and y >=0 :
                f = (x/y)*100
                fr = round((x/y)*100)
                if f <= 1:
                    return "E"
                elif 99 <= f <= 100:
                    return "F"
                elif f > 100:
                    pass
                else:
                    return f"{fr}%"

            else:
                pass

        except (ValueError, ZeroDivisionError):
            pass

main()
