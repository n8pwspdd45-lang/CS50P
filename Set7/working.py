import re

def main():
    print(convert(input("Hours: ")))

def convert(s):

    hours = re.fullmatch(r"(\d{1,2})(?::([0-5][0-9]))? (AM|PM) to (\d{1,2})(?::([0-5][0-9]))? (AM|PM)", s.strip(), re.IGNORECASE)
    if not hours:
        raise ValueError("Invalid format")

    # estraggo gli orari
    h1 = int(hours.group(1))
    mins1 = int(hours.group(2)) if hours.group(2) else 0
    mer1 = hours.group(3).upper()

    h2 = int(hours.group(4))
    mins2 = int(hours.group(5)) if hours.group(5) else 0
    mer2 = hours.group(6).upper()

    # controllo ora valida
    if not (1 <= h1 <= 12 and 1 <= h2 <= 12):
        raise ValueError("Invalid time (hours)")

    # conversione orario
    def to_24(h, mer):
        if mer == "AM":
            return 0 if h == 12 else h
        else: # PM
            return 12 if h == 12 else h + 12

    h1_24 = to_24(h1, mer1)
    h2_24 = to_24(h2, mer2)

    hours_24 = f"{h1_24:02d}:{mins1:02d} to {h2_24:02d}:{mins2:02d}"
    return hours_24


if __name__ == "__main__":
    main()
