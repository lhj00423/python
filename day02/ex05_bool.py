# 참과 거짓만 가지고 있음
#true, false만 나타내는 자료형
# 자료형의 참과 거짓 구분하기
# 문자열 -> 빈문자열: 거짓, "" , "a" : 참
# 리스트 , 딕셔너리, 튜플 -> 비어져 있으면 : 거짓,
# 요소가 있으면 참
# 숫자 1 : 참, 0 : 거짓, none:거짓
#문자열, 리스트, 딕셔너리, 튜플 값이 비어있으면 거짓
#bool(value) --> 불타입으로 변환
print(bool(0)) #f
print(bool(-1)) #t
print(bool("")) #f
print(bool("   ")) #t
print(bool("aa")) #t
print(bool([])) #f
print(bool(({}))) #f
print(bool(())) #f


#문자열 인덱싱문제
#01 pin = "881120-16068234" 성별을 나타내는 숫자를 출력하세요
# print()
#02 문자열 "a:b:c:d" 가 있다 replace를 사용해서 'a#b#c#d' 바꿔서 출력하세요
# a= "a:b:c:d"
# b=(a.replace(":","#"))
# print(b) "a#b#c#d"
# 03.[1,3,5,4,2] 리스트를 [5,4,3,2,1]로 출력
# list1= [1,3,5,4,2]
# list1.sort() [1,2,3,4,5]
# 04.["life","is","too","short"] 리스트로 문자열로 만들어서 출력하세요
# list2 = ["life","is","too","short"]
# result =(" ".join(list2))
# print(result)
# 05. [1,1,1,2,2,2,3,3,3,4,4,5,5,6] --> [1,2,3,4,5,6]에서 중복을 제거하여 출력하세요
# list3 = [1112223344556]
# setlist3 = set(list3)
# list4 = list(set)
# print(list4)
