from fruit import printPlane
import time
import random
import logging

logger = logging.getlogger(__name__)
logger.setlevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("snake.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

Init_tup = (1, 3)
queue = []
flag = False
y_count = 0

logger.info("Init_tup : {}, queue: {}, y_count : {}".format(Init_tup,queue,y_count))

def snakeInit():
    for i in range(1,4):
        queue.append((1,i))
    logger.debug("queue after append: {}".format(queue))

def snakeMove(fruitLocation, arr):
    global Init_tup
    while (flag == False):
        myqueue = minimove(fruitLocation, (Init_tup[0],Init_tup[1]), arr)
        logger.debug("myqueue after minimove {}".format(myqueue))

        time.sleep(0.21)
        if myqueue == -1:
            return 0
        else:
            return myqueue


def mynew(new_x, arr):
    global Init_tup, y_count
    local = random.choice([-1, 1])  # Randomly choose between -1 and 1
    logger.debug("local is {}".format(local))

    Init_tup = (new_x, Init_tup[1] + local)
    logger.debug("Init_tup after local {}".format(Init_tup))

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
    logger.debug("Receiving queue".format(queue))

    temp_queue = list(queue)
    for item in temp_queue:
        print(item)


def manhattan_single(p1,p2):
    logger.debug("Manhattan single value is: {}".format(p1-p2))
    return p1-p2

def checkBoundary(tuple, arr):
    logger.debug("Receiving tuple is {}".format(tuple))

    if tuple is None or arr[tuple[0]][tuple[1]] in ["|", "~", "#"]:
        print("!!GAME OVER!!")
        logger.info("Game Over, checkboundary returned false")
        printPlane()
        return False
    logger.info("checkBoundary returned True")
    return True

def minimove(fruitPoint,head, arr):
    global Init_tup, flag, x_count, y_count
    x_count = manhattan_single(fruitPoint[0], head[0])
    y_count = manhattan_single(fruitPoint[1], head[1])
    logger.debug("x_count is {}, y_count is {}".format(x_count,y_count))

    i = abs(x_count)
    j = abs(y_count)
    while (i != 0):
        next_body = queue.pop(0)
        logger.debug("Popping next body is {}".format(next_body))

        x = next_body[0]
        y = next_body[1]
        if (x_count < 0):
            new_x = Init_tup[0] - 1
        else:
            new_x = Init_tup[0] + 1

        Init_tup = (new_x, Init_tup[1])
        logger.debug("Changed next body is {}".format(Init_tup))

        if arr[Init_tup[0]][Init_tup[1]] == "#":
            logger.debug("next body spot is NOT empty so go to mynew function")
            Init_tup = mynew(new_x)
            logger.debug("After the mynew function, Init tup value is {}".format(Init_tup))

        if checkBoundary(Init_tup) == False:
            logger.info("There is something on the boundary, Flag turn the True!")
            flag = True
            return
        arr[x][y] = " "
        queue.append(Init_tup)
        arr[Init_tup[0]][Init_tup[1]] = "#"
        logger.debug("New part of the body is added.")

        printPlane()
        time.sleep(0.1)
        i -= 1
    while (j != 0):
        next_body = queue.pop(0)
        logger.debug("Popping next body is {}".format(next_body))

        x = next_body[0]
        y = next_body[1]
        if (y_count < 0):
            new_y = Init_tup[1] - 1
        else:
            new_y = Init_tup[1] + 1

        Init_tup = (Init_tup[0], new_y)
        logger.debug("Changed next body is {}".format(Init_tup))

        if checkBoundary(Init_tup) == False:
            logger.info("There is something on the boundary, Flag turn the True!")
            flag = True
            return
        arr[x][y] = " "
        queue.append(Init_tup)
        arr[Init_tup[0]][Init_tup[1]] = "#"
        logger.debug("New part of the body is added.")

        printPlane()
        time.sleep(0.1)
        j -= 1
    queue.insert(0, next_body)
    logger.info("New body inserted to the queue, queue is returning")
    logger.debug("Returning queue is {}".format(queue))
    return queue

def game():
    logger.info("Game is starting in game() func")
    snakeInit()
    printPlane()