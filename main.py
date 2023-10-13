import time
import keyboard
import threading
import random
from rich import print as rprint
from rich.console import Console
import os
import heapq

console = Console(force_terminal=True)

rows, cols = 22, 22
arr = [[" " for i in range(cols)] for j in range(rows)]
queue = []
first = True
Init_tup = (1, 3)
flag = False
values = [-1,1]
x_count = 0
y_count = 0

for i in range(1, 21):
    arr[0][i] = "~"
    arr[21][i] = "~"
for j in range(1, 21):
    arr[j][0] = "|"
    arr[j][21] = "|"

arr[0][0] = "+"
arr[0][11] = "+"
arr[21][0] = "+"
arr[21][21] = "+"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def printPlane():
    output = ""

    for row in arr:
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
    print("SCORE:", len(queue))



def snakeInit():
    for i in range(1,4):
        queue.append((1,i))
        arr[1][i] = "#"


def checkBoundary(tuple):
    if tuple == None or arr[tuple[0]][tuple[1]] == "|" or arr[tuple[0]][tuple[1]] == "~" or arr[tuple[0]][tuple[1]] == "#" :
        print("!!GAME OVER!!")
        printPlane()
        return False
    return True

def checkBox(x, y):
    if(arr[x][y] != " "):
        return False
    else:
        return True

def checkBoxMove(x, y, dir):
    global values, x_count, y_count
    mylocal = y
    initmove = random.choice(values)
    if arr[x][y] == "#" and dir == "y":
        mylocal = initmove + y
        return checkBoxMove(x,mylocal, "x")
    else:
        if  initmove == 1 and y_count < 0:
            y_count = y_count -1
        elif initmove == 1 and y_count > 0:
            y_count = y_count + 1
        elif initmove == -1 and y_count > 0:
            y_count = y_count + 1
        else :
            y_count = y_count - 1
        y = mylocal
        return (x,y)

def mynew(new_x):
    global Init_tup, y_count
    local = random.choice(values)
    Init_tup = (new_x, Init_tup[1] + local)
    if arr[Init_tup[0]][Init_tup[1]] == "#":
        mynew(new_x)
    else:
        if local == 1 and y_count < 0:
            y_count = y_count - 1
        elif local == 1 and y_count > 0:
            y_count = y_count + 1
        elif local == -1 and y_count > 0:
            y_count = y_count + 1
        else:
            y_count = y_count - 1

def fruitSpawn():
    random_x = random.randint(1,21)
    random_y = random.randint(1,21)
    if(checkBox(random_x, random_y)):
        arr[random_x][random_y] = "$"
        point = (random_x,random_y)
        return point
    else:
        return fruitSpawn()

def printQueue(queue):
    temp_queue = list(queue)
    for item in temp_queue:
        print(item)


def manhattan_single(p1,p2):
    return p1-p2


def minimove(fruitPoint,head):
    global Init_tup, flag, x_count, y_count
    x_count = manhattan_single(fruitPoint[0], head[0])
    y_count = manhattan_single(fruitPoint[1], head[1])
    i = abs(x_count)
    j = abs(y_count)
    while (i != 0):
        next_body = queue.pop(0)
        x = next_body[0]
        y = next_body[1]
        if (x_count < 0):
            new_x = Init_tup[0] - 1
        else:
            new_x = Init_tup[0] + 1

        Init_tup = (new_x, Init_tup[1])
        if arr[Init_tup[0]][Init_tup[1]] == "#":
            Init_tup = mynew(new_x)

        if checkBoundary(Init_tup) == False:
            flag = True
            return
        arr[x][y] = " "
        queue.append(Init_tup)
        arr[Init_tup[0]][Init_tup[1]] = "#"
        printPlane()
        time.sleep(0.1)
        i -= 1
    while (j != 0):
        next_body = queue.pop(0)
        x = next_body[0]
        y = next_body[1]
        if (y_count < 0):
            new_y = Init_tup[1] - 1
        else:
            new_y = Init_tup[1] + 1

        Init_tup = (Init_tup[0], new_y)
        if checkBoundary(Init_tup) == False:
            flag = True
            return
        arr[x][y] = " "
        queue.append(Init_tup)
        arr[Init_tup[0]][Init_tup[1]] = "#"
        printPlane()
        time.sleep(0.1)
        j -= 1
    queue.insert(0, next_body)




def snakeMove():
    global Init_tup, interrupt
    while (True):
        if (first):
            if(flag == True):
                return
            minimove(fruitSpawn(), (Init_tup[0],Init_tup[1]))
            #printQueue(queue)
            time.sleep(0.21)



def game():
    snakeInit()
    printPlane()
    snakeMove()

game()