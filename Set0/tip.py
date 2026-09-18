def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = d.replace("$", "")
    D = float(d)
    return D

def percent_to_float(p):
    p = p.replace("%", "")
    P = float(p)
    P = round(P/100, 2)
    return P

main()
