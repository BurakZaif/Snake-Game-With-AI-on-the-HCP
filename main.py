import time
import keyboard
import threading
import random
from rich import print as rprint
from rich.console import Console

console = Console(force_terminal=True)

rows, cols = 12, 12
arr = [[" " for i in range(cols)] for j in range(rows)]
queue = []
first = True
Init_tup = (1, 3)
interrupt = "d"

interrupt_lock = threading.Lock()

for i in range(1, 11):
    arr[0][i] = "~"
    arr[11][i] = "~"
for j in range(1, 11):
    arr[j][0] = "|"
    arr[j][11] = "|"

arr[0][0] = "+"
arr[0][11] = "+"
arr[11][0] = "+"
arr[11][11] = "+"

def process_key_events():
    global interrupt
    while True:
        if keyboard.is_pressed('w'):
            interrupt = "w"
            print("\n")
            # Do something based on the 'w' key press
        elif keyboard.is_pressed('a'):
            interrupt = "a"
            print("\n")
            # Do something based on the 'a' key press
        elif keyboard.is_pressed('s'):
            interrupt = "s"
            print("\n")
            # Do something based on the 's' key press
        elif keyboard.is_pressed('d'):
            interrupt = "d"
            print("\n")
            # Do something based on the 'd' key press

        time.sleep(0.1)  # Add a small delay to avoid excessive checking

keyboard_thread = threading.Thread(target=process_key_events)
keyboard_thread.start()

def printPlane():
    for row in arr:
        for element in row:
            if element == "#":
                console.print("[green]" + str(element), end=' ')
            elif element in ['+', '|', '~']:
                console.print("[red]" + str(element), end=' ')
            else:
                console.print(element, end=' ')
        console.print()


def snakeInit():
    for i in range(1, 4):
        arr[1][i] = "#"

def playerMove():
    move = input("Sıradaki hamle..")

def checkBoundary(tuple):
    if arr[tuple[0]][tuple[1]] == "|" or arr[tuple[0]][tuple[1]] == "~" or arr[tuple[0]][tuple[1]] == "#":
        print("!!GAME OVER!!")
        return False
    return True

def checkBox(x, y):
    if(arr[x][y] != " "):
        return False
    else:
        return True

def fruitSpawn():
    random_x = random.randint(1,11)
    random_y = random.randint(1,11)
    if(checkBox(random_x, random_y)):
        return (random_x, random_y)
    else:
        return fruitSpawn()

def spawnPoint(currentFruit):
    if(currentFruit):
        point = fruitSpawn()
        arr[point[0]][point[1]] = "$"
    return False

def checkFruit(mytuple):
    print("Girdimm")
    print(arr[mytuple[0]][mytuple[1]])
    if arr[mytuple[0]][mytuple[1]] == "$":
        print("I am inside ")
        return True
    return False


def printQueue(queue):
    temp_queue = list(queue)  # Create a temporary list with the contents of the queue
    for item in temp_queue:
        print(item)

def snakeMove(isEat):
    global Init_tup, interrupt
    while (True):
        if (first):
            with interrupt_lock:
                next_body = queue.pop(0)
                x = next_body[0]
                y = next_body[1]
                print("son" + str(x) + str(y))
                if(interrupt == "s"):
                    new_x = Init_tup[0] + 1
                    new_y = Init_tup[1]
                elif interrupt == "w":
                    new_x = Init_tup[0] - 1
                    new_y = Init_tup[1]
                elif interrupt == "d":
                    new_x = Init_tup[0]
                    new_y = Init_tup[1] + 1
                elif interrupt == "a":
                    new_x = Init_tup[0]
                    new_y = Init_tup[1] - 1
                Init_tup = (new_x, new_y)
                if checkBoundary(Init_tup) == False:
                    return
                print("baş" + str(new_x) + str(new_y))
                if checkFruit(Init_tup):
                    print("burdayımmm")
                    isEat = True
                    queue.insert(0, next_body)
                    queue.append(Init_tup)
                else:
                    arr[x][y] = " "
                    queue.append(Init_tup)
                arr[Init_tup[0]][Init_tup[1]] = "#"
                printQueue(queue)
                time.sleep(1)
                printPlane()
                print(isEat)
                isEat = spawnPoint(isEat)
                time.sleep(0.2)

def game():
    isEat = True
    queue.append((1, 1))
    queue.append((1, 2))
    queue.append((1, 3))
    snakeInit()
    printPlane()
    snakeMove(isEat)


game()