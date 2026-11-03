import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        matches = re.search(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$", ip.strip())
        first = int(matches.group(1))
        second = int(matches.group(2))
        third = int(matches.group(3))
        fourth = int(matches.group(4))

        if first <= 255 and second <= 255 and third <= 255 and fourth <= 255:
            return True
        else:
            return False

    except AttributeError:
        return False

if __name__ == "__main__":
    main()
