from mpi4py import MPI
import board
import fruit
import snake
import logging

logger = logging.getlogger(__name__)
logger.setlevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler("main.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
table = board.arr
snake_start = snake.queue

logger.debug("table is {}, and snake_start is {}".format(table, snake_start))

score = 3;

logger.info(("Main script is ready to start"))

#Rank 0 is Table
if rank == 0:
    Ready = input("Ready to play? (Yes/No): ")
    logger.debug("Ready answer is : {}".format(Ready))

    if Ready.lower() == "yes":
        snake.game()

        snake1 = comm.recv(source = 2, tag = 3)
        logger.debug("snake1 is : {}".format(snake1))

        for i in range(1,len(snake1)):
            table[1][i] = "#"
        while(True):
            comm.send(table, dest = 1, tag=0)   #Send the game board to Rank 1
            bot = comm.recv(source=1, tag=1)    #Receive fruit position
            logger.debug("bot is : {} ".format(bot))

            table[bot[0]][bot[1]] = "$"         #Spawning the fruit
            comm.send(bot, dest = 2, tag = 4)   #Sending the fruit position to Rank 2
            comm.send(table, dest = 2, tag=2)   #Sending the updated game board to the Rank 2
            snake_mid = comm.recv(source = 2, tag = 5)  #Receiving the snake's next move
            logger.debug("snake_mid value is : {} ".format(snake_mid))

            if(snake_mid == 0):
                break
            for i in range(1, len(snake_mid)):
                table[1][i] = "#"
        print("Game Over. Score:", score)
        logger.debug("Game Over. Score: {}".format(score))

    else:
        print("Game aborted.")
        logger.debug("Game aborted")

#Rank 1 is fruitspawner
elif rank == 1:
    botTable = comm.recv(source = 0, tag = 0)
    logger.debug("botTable is : {}".format(botTable))

    fruitPos = fruit.fruitSpawn(botTable)
    logger.debug("fruitPos is : {}").format(fruitPos)

    comm.send(fruitPos, source = 1, tag = 1)
    print("Fruit is just appeared")
    logger.info("Fruit is just appeared")

#Rank 2 is snake
elif rank == 2:
    comm.send(snake_start, source = 2, tag = 3)
    fruit_snake = comm.recv(source = 0, tag = 4)
    logger.debug("furit_snake is: {}".format(fruit_snake))

    moveTable = comm.recv(source = 0, tag = 2)
    logger.debug("moveTable is: {}".format(moveTable))

    snake_last = snake.snakeMove(fruit_snake, moveTable)
    logger.debug("snake_last is: {}".format(snake_last))

    comm.send(snake_last, dest = 0, tag = 5)


logger.info("Mpi finalized")
MPI.Finalize()