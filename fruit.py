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

def fruit_spawn(table):
    empty_spots = [(x, y) for x in range(1, 22) for y in range(1, 22) if checkBox(x, y, table)]
    if empty_spots:
        random_x, random_y = random.choice(empty_spots)
        table[random_x][random_y] = "$"
        return (random_x, random_y)
    else:
        raise Exception("No available spots for fruit")

