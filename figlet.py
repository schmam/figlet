# Interface for printing text via ASCII art called Frank, Ian, and Glen's Letters -- http://www.figlet.org/faq.html. If no command-line arguments, prints in random font.
# Accepts -f or --font to allow user to specify the font used.

import sys                          # for capturing sysargv
import random                       # necessary for using random font
from pyfiglet import Figlet         # imports Figlet package
figlet = Figlet()                   # unsure but apparently required to use package

def main():

    fonts = figlet.getFonts()                   # gets list of fonts from Figlet and assigns to  fonts

    if len(sys.argv) == 1:                      # if no paramaters are used in the command line, proceed to print text in a random font
        user_input = input("Input: ")           # gets text from user to be passed to print function below
        f = random.choice(fonts)                # chooses random font from list fonts
        figlet.setFont(font=f)                  # prepares Figlet to print in randomly selected font f
        print(figlet.renderText(user_input))    # prints user input

    elif len(sys.argv) == 2:                    # exits if only one argument included in command line
        sys.exit("Too few arguments")           # exits if more than two arguments included in command line

    elif len(sys.argv) > 3:
        print("Too many arguments")

    else:
        if len(sys.argv) == 3:
            if (sys.argv[1] == "-f" or sys.argv[1] == "--font"):    # checks for "-f" or "--font" in command line
                if sys.argv[2] in fonts:                            # if valid font, proceeds to print user input in specified font
                    user_input = input("Input: ")
                    figlet.setFont(font=sys.argv[2])
                    print(figlet.renderText(user_input))
                else:                                               # if invalid font, exit
                    sys.exit("Invalid font")

            elif sys.argv[1] != "-f" or sys.argv[1] != "--font":    # if arguments are passed but do not include "-f" or "--font", exit
                sys.exit("Invalid syntax")


main()
