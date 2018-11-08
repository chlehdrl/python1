import random
rn = random.randrange(1,101,1)
num = 0


t_cnt = 0


print('Game Start')


while(rn !=num):


    num = int(input("Enter a number between 1 and 101:"))

    if (num > rn):
	print("Down")
    elif (num < rn):
	print("UP")


    t_cnt+=1



print(t_cnt,"번만에 맞추셨습니다.")
print("Game Set")
