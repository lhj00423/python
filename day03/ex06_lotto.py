#random 모듈 불러오기
import random

#로또 번호 출력하기 1~45
lottolist = []
resultlist = []

for i in range(1,46):
    lottolist.append(i)
    
#숫자 6개 추출하여 출력 -->  resultlist
# [123456 ... 45] --> 5 --> resultlist ---->lottolist
for i in range(6):
    randomNum = random.randint(1,len(lottolist))-1
    lottol = lottolist.pop(randomNum)
    resultlist.append(lottol)
print(resultlist)