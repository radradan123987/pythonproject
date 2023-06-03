'''
파일명: Ex02-7-set

set
    순서가 없다
    인덱싱되지 않은 컬렉션
    중복값 없다.

'''

thissset = {"파카츄", "라이츄", "파이리"}
# 실행할 때 마다 순서가 변경된다.
print(thissset)

# 항목 가져오기
for x in thissset: # thissset 길이만큼 반복
    print(x)

# 값이 있는지 확인
thissset = {"피카츄", "잠만보", "야도란"}
print("피카츄" in thissset)
print("꼬부기" in thissset)

# 항목 추가하기
thissset.add("꼬부기")
print(thissset)

# 다른 Set 항목 추가
thissset1 = {"피카츄", "라이츄", "파이리"}
thissset2 = {"꼬부기", "잠만보", "뮤츠"}
thissset1.update(thissset2)
print(thissset1)

#항목제거
thissset = {"피카츄", "라이츄", "파이리"}
thissset.remove("피카츄")
print(thissset)
# 없는 항목 삭제시 에러발생
# thissset.remove("피카츄")
# print(thissset)

thissset = {"피카츄", "라이츄", "파이리"}
thissset.discard("피카츄")
print(thissset)
# 없는 항목 삭제시 에러발생 안함
thissset.discard("피카츄")
print(thissset)

# 항목제거2
thissset.pop()
print(thissset)

# 비우기
thissset.clear()
print(thissset)









