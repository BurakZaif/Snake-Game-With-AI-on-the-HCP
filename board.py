from fruit import printPlane

rows, cols = 22, 22
arr = [[" " for i in range(cols)] for j in range(rows)]

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
arr[0][21] = "+"
arr[21][0] = "+"
arr[21][21] = "+"


def checkBoundary(tuple):
    if tuple == None or arr[tuple[0]][tuple[1]] == "|" or arr[tuple[0]][tuple[1]] == "~" or arr[tuple[0]][tuple[1]] == "#" :
        print("!!GAME OVER!!")
        printPlane()
        return False
    return True





