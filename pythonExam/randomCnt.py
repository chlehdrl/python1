import random
rn = random.randrange(1,1001)
num = 0
t_cnt = 0


print('Game Start')


while(rn !=num)


    num = int(input("Enter a number between 1 and 1001"))


    if (num > rn):
	print("Down")
    elif (num < rn):
	print("UP")


    t_cnt+=1



print("Game Set")