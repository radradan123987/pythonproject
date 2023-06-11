'''

open 함수 모드
     w(write mode) : 쓰기 전용모드 / 파일이 없으면 생성
     t(text mode) : 해당 파일의

'''
file = open('hello.txt', 'wt', encoding='UTF-8')
file.write('안녕하세요.')
file.write('\n')
file.write('반갑습니다.')
file.write('\n')
print('hello.txt 파일이 생성되었습니다.')
file.close()

