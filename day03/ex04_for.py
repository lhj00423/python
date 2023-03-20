# ex04_for.py

list1 = ["one,","two","three"]
for i in list1:
        print(i)
for i in "blue":
        print(i)     
        
marks = [90,50,67,70,80]
number = 0
for stu in marks:
    number = number + 1
    if stu >= 70:
        print("%d번 학생은 합격입니다." %number)
    else :
        print("%d불합격입니다." %number)
print(list(range(3,10,3)))
           
#range()함수, range(stop), range(start,stop), range(start, stop, step)
sum = 0
for i in range(1,11,2):
    sum = sum + i
print('1~10까지 더한수는 %d이다.' %sum)

#for와 range를 사용해서 구구단 출력
#2단부터 9단
print("구구단을 출력합니다.\n")
for x in range(2, 10):
    print("[" + str(x) + "단]")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("끝")
############### pinkcandy~▽
for i in range(2,10):
    for j in range(1,10):
        print('%d * %d = %d' %(i,j,i*j))