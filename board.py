from fruit import printPlane

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


def checkBoundary(coord):
    x, y = coord
    if arr[x][y] in ["|", "~", "#"]:
        print("!!GAME OVER!!")
        printPlane()
        return False
    return True





