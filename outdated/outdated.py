months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    x = convert()

def convert():
    while True:
        try:
            date = input("Date: ")
            if  "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 < day <= 31 and 1 < month <= 12:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    pass

            elif "," in date:
                month_and_day, year = date.split(",")
                year = year.strip()
                year = int(year)
                month, day = month_and_day.split(" ")
                day = int(day)
                month = months.index(month) + 1
                if 1 <= day <= 31 and 1 <= month <= 12:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    pass

            else:
                print("Nope")

        except ValueError:
            print("Nope")

main()
