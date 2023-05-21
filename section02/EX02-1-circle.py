'''

개요 : 반지름을 전달하면 원의 넓이를
      반환하는 GET_area()함수

ctri+/ 한줄주석 단축키

'''


# math 모듈포함
import math

#get_area() 함수정의
def get_area(radius):
    """반지름을 입력 받아서 원의 넓이를 반환하는 get_area() 함수"""
    area = math.pi + math.pow(radius, 2)
    return area

# 실행코드
radius + 1.5
print(radius)

#get_area() 함수 호출결과를 area 변수에 저장
area = get_area(radius)
print(area)
print(get_area:__doc__) # Doctring 확인