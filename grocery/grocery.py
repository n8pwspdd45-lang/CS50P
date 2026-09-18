def main():
    glist = get_list()

def get_list():
    glist = {}
    while True:
        try:
            item = input().upper()
            if item not in glist:
                glist[item] = 1
            else:
                glist[item] += 1

        except EOFError:
            print()
            for key, value in sorted(glist.items()):
                print(f"{value} {key}", sep='\n')
            break

main()
