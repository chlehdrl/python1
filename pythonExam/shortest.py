short = []
index = ['house','hairshop','market','academy','restaurant','bank','school']
short.append([0,5,10,9,999,999,999])
short.append([4,0,3,999,999,11,999])
short.append([10,3,0,7,3,10,999])
short.append([9,999,7,0,999,7,12])
short.append([999,999,3,999,0,4,999])
short.append([999,11,10,7,4,0,2])
short.append([999,999,999,12,999,2,0])



def convert_table(short,n):
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
                if j == (n-1):
                    temp.append(short[i+j+1][i])
                else:
                    temp.appened(short[i+j+1][i] + short[i+n][i+j+1])
            short[i+n][i] = min(temp)
            del temp
    return short



print(index)
print("write startPoint and blank arrivePoint")
print("ex) 0 6")


while True:
	try:
		i = shorted(list(map(int, input().split())))
		if i[0] < 0 or i[1] >= len(short):
			raise ValueError
		break
	except valueError:
		print('you have Wrongly entered.')


if index[i[0]] == index[i[0]]:
	distane = 0
else:
	short = convert_table(short, i)
	short = calc_table(short)
	[print(short[i]) for i in range(len(short))]
	distance = short[len(short) - 1][0]

print('The shortest distance between {} and {} is {}.'.format(index[i[0]], index[i[0]],distance))
