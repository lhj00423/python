#abs(x) 절대값을 반환
result1 = abs(-100)
print(result1)

#all(x) 리스트, 튜플, 문자열 전체가 True일때만 True리턴 나머지 False리턴
#any(x)  하나라도 true면 true리턴
print(any([""," ","",[]]))
print(all([1,"A","a"]))

# divmod(a,b) 몫과 나머지를 tuple로 반환
print(divmod(10,3))

# enumerate()열거하다
list = ["a","b","c","d","e"]
for i in range(len(list)):
    print(i,list[1])
    
for i, v in enumerate(list):
    print(i, v)    
    
    
#max()
print(max([80,90,60,70,50]))
#min
print(min([10,20,30,50]))

scroes = [10,20,30,60,12,90]
maxscore = max(scroes)
maxindex = scroes.index(maxscore)
print("최대값은 %d 이고 $d번째 값입니다." %(maxscore,maxindex))

#round() 반올림해서 반환
print(round(12.6789, 2))

#sum(x) 리스트나 튜플을 입력받아 모든 요소의 합을 ㅂ나환
numTuple = (2,3,4,5)
print(sum(numTuple))