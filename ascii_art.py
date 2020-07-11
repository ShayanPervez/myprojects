from pyfiglet import figlet_format
from termcolor import colored
def ascii_art(name, color):
         ascii_text= figlet_format(name, font='standard')
         if color not in ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'):color = "magenta"

         color_text = colored(ascii_text, color)
         return color_text

user_input = input("What message do you want to print? ")
colour = input("What is the color? ")

print(ascii_art(user_input, colour))




