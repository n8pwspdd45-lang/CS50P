from datetime import date
import inflect
import sys

def main():
    birth = input("Date of Birth (YYYY-MM-DD): ")
    try:
        print(get_minutes(birth))
    except ValueError:
        sys.exit("Invalid date")


def get_minutes(birth):
    try:
        year, month, day = birth.split("-")
        year, month, day = int(year), int(month), int(day)
        birth = date(year, month, day)

    except (ValueError, TypeError):
        raise ValueError("Invalid date")

    time = date.today() - birth

    p = inflect.engine()
    mins = p.number_to_words(time.days*24*60, andword='')
    return f"{mins.capitalize()} minutes"


if __name__ == "__main__":
    main()
