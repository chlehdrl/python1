import random
x = random.randrange(0,7)
y = random.randrange(0,7)

while (x!=y) :
    y = random.randrange(0,7)# 두 지역 랜덤 뽑기

print("출발지는",x,"입니다.")
print("도착지는",y,"입니다,")

short = [[0]*8 for i in range(9)]
shortest = 10000
def convert_table(short, n):
    for i in range(len(short)):
        short[i].insert(0, short[i].pop(n[0]))
        short[i].insert(len(short) - 1, short[i].pop(n[1]))
    short.insert(0, short.pop(n[0]))
    short.insert(len(short) - 1, short.pop(n[1]))
    return short
def calc_table(short):
    for n in range(2, len(short)):
        for i in range(len(short) - n):
            temp = []
            for j in range(n):
                if j == (n - 1):
		    temp.append(short[i+j+1][i])
		else:
		    temp,append(short[i+j+1][i] + short[i+n][i+j+1])
	    short[i+n][i] = mn(temp)
	    del temp
    return short


for i in range(0,7):
    for j in range(0,8):
	SW = random.randrange(0,2)
	#print(SW)
	if SW == 1:
	    short[i][j] = random.randreange(3,20)
	else:
	    short[i][j] = 999
print(short)
# short = convert_table(short, i)
# short = calc_table(short)
# print(shortpi[) for i in range(len(short))]
# distance = short[len(short) - 1][0]

while (short == mynum) :
    
    mynum = int(input("%s와 %s의 최단거리는?" %(x,y))
    if (mynum == short):
	print("correct answer")
    else:
	print("oops, try again.")

    
