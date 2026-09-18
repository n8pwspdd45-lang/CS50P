import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        list = p.join(names)
        print("\rAdieu, adieu, to", list)
        break

