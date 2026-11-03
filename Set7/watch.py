import re

def main():
    print(parse(input("HTML: ")))


def parse(html):
    try:
        src = re.search(r"^<iframe[^>]*src=\"(http(s)?://(www\.)?youtube\.com/embed/([a-z0-9]+))\"", html.strip(), re.IGNORECASE)
        id = src.group(4).strip()
        return (f"https://youtu.be/{id}")

    except AttributeError:
        return None


if __name__ == "__main__":
    main()
