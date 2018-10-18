short = []
index = ['house','hairshop','market','academy','restaurant','bank','school']
short.append([0,5,10,9,999,999,999])
short.append([0,5,10,9,999,999,999])
short.append([0,5,10,9,999,999,999])
short.append([0,5,10,9,999,999,999])
short.append([0,5,10,9,999,999,999])
short.append([0,5,10,9,999,999,999])
short.append([0,5,10,9,999,999,999])



def convert_table(short,n):
	for i in range(len(short)):
		short[i].insert(0, short[i].pop(n[0]))
		short[i].insert(len(short) - 1, short[i].pop(n[1]))
	short.insert(0, short.pop(n[0]))
	short.insert(len(short) - 1, short.pop(n[1]))
	return short


def calc_table(short):
	for n in range(2, len(short)):
		for i in range(len(short) - ):
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
