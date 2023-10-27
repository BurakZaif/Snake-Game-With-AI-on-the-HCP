from mpi4py import MPI
import board
import fruit
import snake

score = 3;
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
table = board.arr
snake_start = snake.queue
#Rank 0 is Table
if rank == 0:

    Ready = input(("Ready to play?")
    if Ready == "Yes":
        snake.game()
        snake1 = comm.recv(source = 2, tag = 3)
        for i in range(1, 4):
            table[1][i] = "#"

        comm.send(table, dest = 1, tag=0)
        bot = comm.recv(source=1, tag=1)
        table[bot[0]][bot[1]] = "$"

        comm.send(table, dest = 2, tag=2)


#Rank 1 is fruitspawner
elif rank == 1:
    botTable = comm.recv(soruce = 0, tag = 0)
    fruitPos = fruit.fruitSpawn(botTable)

    comm.send(fruitPos, source = 1, tag = 1)
    print("Fruit is just appeared")

#Rank 2 is snake
elif rank == 2:
    comm.send(snake_start, source = 2, tag = 3)
    moveTable = comm.recv(source = 0, tag = 2)
    snake.snakeMove()