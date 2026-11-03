import validators

def main():
    email = input("What's your email adress? ")
    print(validation(email))

def validation(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
