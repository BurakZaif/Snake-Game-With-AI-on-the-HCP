from fruit import printPlane
import time
import random

Init_tup = (1, 3)
queue = []

def snakeInit():
    for i in range(1,4):
        queue.append((1,i))


def snakeMove(fruitLocation):
    global Init_tup, interrupt
    while (True):
        if(flag == True):
            return
        minimove(fruitLocation, (Init_tup[0],Init_tup[1]))
        time.sleep(0.21)


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

def game():
    snakeInit()
    printPlane()

