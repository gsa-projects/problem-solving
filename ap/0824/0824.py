# 배열의 주어진 범위의 합을 2로 나눈 몫을 구하세요
import random

testcase = int(input())
A = [0] * 100001

for i in range(0, 100001):
    A[i] = random.randrange(1, 101)

for t in range(1, testcase + 1):
    start, end = map(int, input().split())
    
    # answer = 0
    # for i in range(start, end + 1):
    #     answer = answer + A[i]
    answer = sum(A[start:end+1])

    print(str(t) + " " + str(answer // 2))