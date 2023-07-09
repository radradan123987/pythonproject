'''
Ex21-6-O(2^n).py

O(2^n)
    지수 시간 복잡도, 피보니치 수열처럼 재귀적 알고리즘
'''
def fidonacci(n):
    if n <= 1:
        return n
    return fidonacci(n-1) + fidonacci(n-2)

print(fidonacci(50))


