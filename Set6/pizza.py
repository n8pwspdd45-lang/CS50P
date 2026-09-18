import sys
import csv
from tabulate import tabulate

def main():
    if control() == sys.argv[1]:
        nome_file = sys.argv[1]

    if csv_controllo(nome_file) == True:
        try:
            with open(nome_file, mode="r") as file:
                lettore_csv = csv.reader(file)
                headers = next(lettore_csv)
                dati = list(lettore_csv)
                print(tabulate(dati, headers, tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")

def control():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        return sys.argv[1]

def csv_controllo(controllo):
    if controllo.endswith(".csv"):
        return True
    else:
        return False

main()
