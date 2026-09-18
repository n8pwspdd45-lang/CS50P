def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if alnum(s) and max_min(s) and numbers(s):
        return True
    else:
        return False


def alnum(s):
    if s[0:1].isalpha() and s.isalnum():
        return True
    else:
        return False

def max_min(s):
    lenght = len(s)
    if 2 <= lenght <= 6:
        return True
    else:
        return False

def numbers(s):
    prima = None

    # Cerca la prima cifra
    for i in range(len(s)):
        if s[i].isdigit():
            prima = i
            break

    # Se dopo la prima ci sono solo cifre e la prima non è = 0 oppure se solo solo lettere
    if s[prima:].isdigit() and s[prima] != "0" or prima == None:
        return True
    else:
        return False

main()
