from mpi4py import MPI
import board
import fruit
import snake

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
table = board.arr
snake_start = snake.queue

score = 3;

#Rank 0 is Table
if rank == 0:
    Ready = input("Ready to play? (Yes/No): ")
    if Ready.lower() == "yes":
        snake.game()
        snake1 = comm.recv(source = 2, tag = 3)
        for i in range(1,len(snake1)):
            table[1][i] = "#"
        while(True):
            comm.send(table, dest = 1, tag=0)   #Send the game board to Rank 1
            bot = comm.recv(source=1, tag=1)    #Receive fruit position
            table[bot[0]][bot[1]] = "$"         #Spawning the fruit
            comm.send(bot, dest = 2, tag = 4)   #Sending the fruit position to Rank 2
            comm.send(table, dest = 2, tag=2)   #Sending the updated game board to the Rank 2
            snake_mid = comm.recv(source = 2, tag = 5)  #Receiving the snake's next move
            if(snake_mid == 0):
                break
            for i in range(1, len(snake_mid)):
                table[1][i] = "#"
        print("Game Over. Score:", score)
    else:
        print("Game aborted.")


#Rank 1 is fruitspawner
elif rank == 1:
    botTable = comm.recv(source = 0, tag = 0)
    fruitPos = fruit.fruitSpawn(botTable)

    comm.send(fruitPos, source = 1, tag = 1)
    print("Fruit is just appeared")


#Rank 2 is snake
elif rank == 2:
    comm.send(snake_start, source = 2, tag = 3)
    fruit_snake = comm.recv(source = 0, tag = 4)
    moveTable = comm.recv(source = 0, tag = 2)
    snake_last = snake.snakeMove(fruit_snake, moveTable)
    comm.send(snake_last, dest = 0, tag = 5)


MPI.Finalize()