import random
from rich.console import Console
import os

console = Console(force_terminal=True)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def printPlane(table, score):
    output = ""

    for row in table:
        for element in row:
            if element == "#":
                output += "\033[32m" + str(element) + " "  # Green color
            elif element in ['+', '|', '~']:
                output += "\033[31m" + str(element) + " "  # Red color
            else:
                output += str(element) + " "
        output += "\033[0m\n"  # Reset color and move to the next line

    clear_terminal()  # Clear the terminal
    print("\033[H" + output)  # Move cursor to the top and print the entire output
    print("SCORE:", score)


def checkBox(x, y, table):
    if(table[x][y] != " "):
        return False
    else:
        return True

def fruitSpawn(table):
    random_x = random.randint(1,21)
    random_y = random.randint(1,21)
    if(checkBox(random_x, random_y)):
        table[random_x][random_y] = "$"
        point = (random_x,random_y)
        return point
    else:
        return fruitSpawn()

