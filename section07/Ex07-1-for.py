'''

for문
    값의 범위나 횟수가 정해져 있을 때 
    사용하면 편리한 반복문
    while문보다 사용빈도 높다.
    
for 변수 in 반복가능한객치:
    반복실행문    
'''

pwd = input('비밀번호를 입력하세요 >>> ')

ch_count = 0
num_count = 0
for ch in pwd:    #abcd1234
    # 1: ch = a
    # 2: ch = b
    # 3: ch = c
    # 4: ch = d
    # 5: ch = 1
    # 6: ch = 2
    # 6: ch = 3
    # 6: ch = 4
    # 6: ch = 5

    if ch.isalpha(): # 문자여부
         ch_count += 1
    elif ch.isnumeric(): # 숫자여부 
        num_count += 1
        
if ch_count > 0 and num_count > 0:
    print('가능한 비빌번호 입니다.')
else:
    print('불가능한 비밀번호 입니다.')
