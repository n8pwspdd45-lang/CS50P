coin = [50, 25, 10, 5]
price = 0

print("Amount Due: 50")
insert = int(input("Insert coin: "))

while price < 50:
    if insert in coin:
        price += insert
        if price < 50:
            print("Amount Due:", (50 - price))
            insert = int(input("Insert coin: "))
        else:
            change = price - 50
            print("Change Owed: ", change, sep="")
            # print("Fan***o Panzone!")
    else:
        print("Amount Due:", (50 - price))
        insert = int(input("Insert coin: "))
