import sys
from PIL import Image
from PIL import ImageOps
import os

def main():
    if arg():
        before = sys.argv[1]
        after = sys.argv[2]
        if file_type(before, after) and existence(before):
            overlapping_shirt(before, after)



def arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return True



def file_type(file1, file2):
    _, ext1 = file1.rsplit(".", 1)
    _, ext2 = file2.rsplit(".", 1)
    extensions = ("jpg", "jpeg", "png")
    if file1.lower().endswith(extensions) and file2.lower().endswith(extensions):
        if ext1 in ["jpg", "jpeg"] and ext2 in ["jpg", "jpeg"]:
            return True
        elif ext1 == "png" and ext2 == "png":
            return True
        else:
            sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")



def existence(name_file):
    if not os.path.exists(name_file):
        sys.exit("IInput does not exist")
    else:
        return True



def overlapping_shirt(file1, file2):
    shirt = Image.open("shirt.png")
    person = Image.open(file1)
    person = ImageOps.fit(person, (600, 600))
    person.paste(shirt, (0,0), shirt)
    person.save(file2)
    return file2


if __name__ == "__main__":
    main()
