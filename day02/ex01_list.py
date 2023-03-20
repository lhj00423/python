list1 = ["1","3","6","9"]
print(list1)
print(type (list1))
print(list1[1])
# 리스트의 슬라이싱 [start:end] end번째는 포함하지 않음 
print(list1[0:3])
print(list1[2:])
list2 = [9,8,7]
list3 = [6,5,4]
list4 = [3,2,1]
#리스트 더하기 + 기호를 사용하면 리스트 합쳐준다
list5 = list1 + list4
print(list5)
#리스트 반복하기 * 기호를 사용하면 리스트를 반복해서
#새로운 리스트를 반환함
list6 = list5*3
print(list6)
#리스트 길이 구하기 len(리스트)
print(len(list6))
# 리스트 수정, 삭제 (del 객체)
list2[0] = 10
print(list2)
del list2[0]
del list3[4:]
print(list3) 

students = ["stu1","stu2","stu3","stu4"]
#리스트에 요소 추가 append(value)
students.append("stu5")
print(students)
# 리스트에 요소 추가 (원하는 위치에) insert(start,value)
students.insert(1,"newStu")
print(students)
# 리스트 뒤집기 reverse()
students.reverse()
print(students)
# 리스트 정렬 .sort()
students.sort()
print(students)
numberList = [5,2,1,3,4]
numberList.sort()
print(numberList)
#인덱스 반환 index(value)
num = students.index("stu1")
print(num)
# 리스트 요소 제거 remove(value)
students.remove("stu3")
print(students)
numberList.remove(2)
print(numberList)
#리스트 마지막 요소 리턴후 삭제 pop()
lastList = students.pop()
print(lastList)
print(students)
# 리스트에 포함된 요소의 개수 세기 count(value)
fruits = ["사과","딸기","바나나","귤","제주도감귤","특산명물 파인애플","사과","샤과"]
applenum  = fruits.count("사과")
print(applenum)








