import sys
import csv

def main():
    if control():
        file_in = sys.argv[1]
        file_out = sys.argv[2]
        first_second(file_in, file_out)


def first_second(file_in, file_out):
    try:
        with open(file_in, 'r') as fin:
            csv_reader = csv.reader(fin)
            header = next(csv_reader)
            dati = list(csv_reader)
        with open(file_out, 'w', newline='') as fout:
            scrittore = csv.DictWriter(fout, fieldnames=["first","last","house"])
            scrittore.writeheader()
            for line in dati:
                name = line[0]
                last, first = name.split(",", 1)
                house = line[1]
                scrittore.writerow({"first": first.lstrip(), "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {file_in}")

def control():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return True

if __name__ == "__main__":
    main()
