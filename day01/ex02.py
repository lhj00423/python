num1 = 10
num2 = 3



#연산자
#+,-,*,/,**,%, \\ㅡ_ㅡOTL// 
print(num1* num2)
print(num1 / num2)
print(num1 // num2)
print(num1 + num2)
print(num1 - num2)

#문자열 곱하기
print("="*20)
#문자열 더하기 + 
head = "python"
tail = " isnot fun"
print(head+tail)
print(head * 2)
#문자열 길이 구하기 len(변수)
a ="what!"
print(len(a))
#문자열 인덱싱 슬라이싱
print(a[0])
#문자열 슬라이싱 (시작번호 : 끝번호) -끝번호 제외
print(a[0:2])
print(a[:3])
print(a[2:])

# 문자열 포메팅 : 문자열안에 어떤 값을 넣기
# 문자열 포맷코드
# %d 정수 %s 문자열 %f 소수
num = 3
str3 ="어젯밤에~ 우리아빠가~ 사다주신 크레파스로~~~나뭇잎을 그렸어요~~ 뚠뚠" 
print("아빠는 사과를 먹었다" % (str3,num))
print("%0.4f" %3.123456789)

#format 함수 사용하기
num2 = 10 
str4 ="어제"
print("나는 {str4} 사과 {num2}개를 먹었다" .format(str4="어제",num2=30))
number3 = 20
print("현재 온도는 {0}입니다. 내일 온도는 {to}입니다." .format(number3,to=30))
name = "lhj"
age = 28
print(f'나의 이름은{name}이고 나이는 {age}이다')
print(f'내년이면 나의 나이는 {age+1}이 됩니다.')
