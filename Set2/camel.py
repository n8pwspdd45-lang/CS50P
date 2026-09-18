def main():
    camelCase = input("camelCase: ")
    camel_to_snake(camelCase)

def camel_to_snake(word):
    snake_case = ""
    for c in word:
        if c.isupper():
            snake_case += "_" + c.lower()
        else:
            snake_case += c
    print(snake_case)

main()
