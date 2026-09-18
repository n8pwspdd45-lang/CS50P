from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

# Se l'utente specifica il font
if len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font = figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(input("Input: ")))

# Se l'utente non specifica il font
elif len(sys.argv) == 1:
    font = figlet.setFont(font=random.choice(fonts))
    print(figlet.renderText(input("Input: ")))

elif len(sys.argv) != 3 or sys.argv[1] not in ["-f", "--font"]:
     sys.exit("Invalid usage")
