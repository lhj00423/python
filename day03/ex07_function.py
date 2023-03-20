# 함수  입력값 ==> 함수 ==> 리턴값
#1.일반적인 함수 : 입력값과 리턴값이 있는 함수
def add(a,b) :
    return a+b 
#2. 입력값이 없는 함수
def printHi():
    print("안녕")

print(printHi())

#매개변수 지정해서 호출하기
#매개변수를 지정해서 호출하면 순서에 상관없이 사용할수 있음
def sub(a,b):
    return a - b
re2 = sub(b=10,a=20)
print(re2)

#매개변수 입력값이 몇개가 될 지 모를때
#입력값을 전부 모아서 튜플로 만들어줌 !
def addMany(**args):
    result = 0
    for i in args:
        result = result +1
    return result

addMany(1,2,3,4,5)
addMany(2,3,4)   
# 매개변수에 초기값 설정하기
#12345를 인수로 받아서 [5,4,3,2,1]리턴
# int("100") --> 정수로 형변환
# list() --> 리스트로 형변환
# str() --> 문자열로 형변환
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer

print(solution(12345))

#인수로 주는 모든 수의 평균값을 구하는 함수를 작성하시오
def avgNumber(*args):
    sum = 0
    for i in args:
        sum += i
    avgre = sum / len(args)
    return avgre

print(avgNumber(1,2,3))
print(avgNumber(5,6,7,8,9,10))

#람다 함수
#lambda 매개변수1, 매개변수2 : 매개변수를 사용한 표현식
lambdaAdd = lambda a,b : a+b 