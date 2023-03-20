#ex05_random.py
#import 모듈 불러오기
import random
# random() 0.0~1.0사이의 난수 값을 반환
num = random.random()
print(num)
#randint(start,end) start ~ end 정수 랜던 값을 반환
num2 = random.randint(1,5)
print(num2)
 
#01 평균구하기
# [70,60,55,75,95,90,80,80,85,100]
# for문을 사용하여 A학급의 평균 점수를 구해 보자.
# len(리스트) --> 리스트길이
listA =  [70,60,55,75,95,90,80,80,85,100]
total = 0
for i in listA:
    total += i
ave = total/len(listA)
print(ave)    

#02 별찍기
for i in range(1,6):
    print("*"*i)
    
# 03 가위바위보 게임 만들기
# 사용자로부터 가위, 바위 보중 하나를 입력
# 가위, 바위, 보가 아니면 잘못입력했습니다.
# 가위, 바위, 보 중 입력했을때 컴퓨터도 가위,바위,보 중 하나를 랜덤으로 지정
# 각각 지정
rps = input("가위, 바위, 보 중 하나 내놔 : ")
com = ""
if rps != '가위' and rps != '바위' and rps != '보' :
    print("잘못입력하셨습니다.")
else : 
    print("%s를 똑바로 입력했습니다." %rps)
    rpsnum = random.randint(1,3)
    com = "가위" if rpsnum == 1 else "바위" if rpsnum == 2 else "보"
    print("컴이 %s를 냈습니다." %com)
    if rps == com :
        print("썌임")
    elif (rps == "가위" and com == "보" 
    or rps == "바위" and com == "가위" 
    or rps == "보" and com == "바위") :
        print("이김")
    else : 
        print("짐")