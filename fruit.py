import random
from rich.console import Console
import logging
import os

logger = logging.getlogger(__name__)
logger.setlevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("fruit.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

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
    logger.info("printPlane function is succesfully finished.")

def checkBox(x, y, table):
    logger.debug("checking the table {} location whhich is ({},{})".format(table,x,y))

    if(table[x][y] != " "):
        logger.info("checkbox returned false")
        return False
    else:
        logger.info("checkbox returned true")
        return True

def fruit_spawn(table):
    empty_spots = [(x, y) for x in range(1, 22) for y in range(1, 22) if checkBox(x, y, table)]
    logger.debug("Empty spots are : {}".format(empty_spots))

    if empty_spots:
        random_x, random_y = random.choice(empty_spots)
        logger.debug("random_x : {}, random_y : {}".format(random_x,random_y))

        table[random_x][random_y] = "$"
        return (random_x, random_y)
    else:
        logger.exception("No available spots for fruit")
        raise Exception("No available spots for fruit")