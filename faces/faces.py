def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    text = input("Say something using :) or :( ->  " )
    print(convert(text))

main()
