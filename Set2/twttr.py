def main():
    word = input("Input: ")
    twttr(word)

def twttr(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    wrd = ""
    for c in word:
        if c in vowels:
            c = c.replace(c, "")
            wrd += c
        else:
            wrd += c
    print("Output:", wrd)

main()
