def main():
    user_in = input("What time is it? ")
    time = convert(user_in)
    if time is not None:
        if 7 <= time <= 8:
            print("breakfast time")
        elif 12 <= time <= 13:
            print("lunch time")
        elif 18 <= time <= 19:
            print("dinner time")

def convert(user_in):
    hrs, mins = user_in.split(":")
    hrs = int(hrs)
    mins = int(mins)
    time = float(hrs + (mins/60))
    if (mins/60) < 1 and 0 <= hrs <= 24:
        return time

if __name__ == "__main__":
    main()
