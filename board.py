from fruit import printPlane
import logging

logger = logging.getlogger(__name__)
logger.setlevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("board.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

rows, cols = 22, 22
arr = [[" " for i in range(cols)] for j in range(rows)]

for i in range(1, 21):
    arr[0][i] = "~"
    arr[21][i] = "~"
for j in range(1, 21):
    arr[j][0] = "|"
    arr[j][21] = "|"

arr[0][0] = "+"
arr[0][21] = "+"
arr[21][0] = "+"
arr[21][21] = "+"

logger.debug("arr: {}".format(arr))

def checkBoundary(coord):
    x, y = coord
    logger.debug("coordinates are ({},{})".format(x,y))

    if arr[x][y] in ["|", "~", "#"]:
        print("!!GAME OVER!!")
        logger.info("Touched the boundary so Game Over!")
        printPlane()
        return False
    logger.info("There is nothing on the boundary. Game on...")
    return True