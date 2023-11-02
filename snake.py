from fruit import printPlane
import time
import random

Init_tup = (1, 3)
queue = []
flag = False
y_count = 0


def snakeInit():
    for i in range(1,4):
        queue.append((1,i))


def snakeMove(fruitLocation, arr):
    global Init_tup
    while (flag == False):
        myqueue = minimove(fruitLocation, (Init_tup[0],Init_tup[1]), arr)
        time.sleep(0.21)
        if myqueue == -1:
            return 0
        else:
            return myqueue


def mynew(new_x, arr):
    global Init_tup, y_count
    local = random.choice([-1, 1])  # Randomly choose between -1 and 1
    Init_tup = (new_x, Init_tup[1] + local)
    if arr[Init_tup[0]][Init_tup[1]] == "#":
        mynew(new_x,arr)
    else:
        if local == 1 and y_count < 0:
            y_count = y_count - 1
        elif local == 1 and y_count > 0:
            y_count = y_count + 1
        elif local == -1 and y_count > 0:
            y_count = y_count + 1
        else:
            y_count = y_count - 1

def printQueue(queue):
    temp_queue = list(queue)
    for item in temp_queue:
        print(item)


def manhattan_single(p1,p2):
    return p1-p2

def checkBoundary(tuple, arr):
    if tuple is None or arr[tuple[0]][tuple[1]] in ["|", "~", "#"]:
        print("!!GAME OVER!!")
        printPlane()
        return False
    return True

def minimove(fruitPoint,head, arr):
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
    return queue

def game():
    snakeInit()
    printPlane()



