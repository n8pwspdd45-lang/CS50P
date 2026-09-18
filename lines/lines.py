import sys

def main():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        nome_file = sys.argv[1]
        controllo = py(nome_file)
        if controllo == True:
            try:
                with open(nome_file) as file:
                    number = count(file)
                    print(number)
            except FileNotFoundError:
                sys.exit("File does not exist")
        elif controllo == False:
            sys.exit("Not a Python file")

def py(nome_file):
    if nome_file.endswith(".py"):
        return True
    else:
        return False

def count(file):
    n_lines = 0
    for line in file:
        if line.isspace():
            pass
        elif line.lstrip().startswith("#"):
            pass
        else:
            n_lines += 1
    return n_lines

if __name__ == "__main__":
    main()
