mport random
# 게임을 위한 랜덤 숫자 생성
rn = [0,0,0]
rn[0] = str(random.randrange(1,9))
rn[1] = rn[0]
rn[2] = rn[0]
while (rn[0] == rn[1]):
    rn[1] = str(random.randrange(1,9))
while (rn[0] == rn[2] or rn[1] == rn[2]):
    rn[2] = str(random.randrange(1,9))


#print(rn)

t_cnt = 0 # 시도횟수
s_cnt = 0 # 스트라이크
b_cnt = 0 # 볼

print("start")

while (s_cnt < 3):
    num = str(input("3자리 입력:"))


    s_cnt = 0
    b_cnt = 0

    for i in range(0,3):
	for j in range(0,3):
	    if (num[i] == str(rn[j]) and i==j):
		s_cnt += 1
	    elif (num[i] == str(rn[j]) and i != j):
		b_cnt += 1
    print("결과 :strike",s_cnt,"개 ball",b_cnt"개")
    t_cmt+=1
print(t_cnt,"회 걸렸습니다.")
