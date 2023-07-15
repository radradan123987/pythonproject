'''
EX23-1-BubbleSort.py

1. 버블 정렬(Bubble Sort)
     인접한 두 원소를 비교하여 정렬하는 알고리즘 중 하나로
     가장 간단한 정렬 알고리즘 중 하나이다.

     시간복잡도 : O(n^2)
'''

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# 실행코드
arr = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubble_sort(arr))


