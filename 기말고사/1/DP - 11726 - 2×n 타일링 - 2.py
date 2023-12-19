n = int(input())
D = {1: 1, 2: 2}
# note: base case 개수 고려하기 싫을 때 최고는 딕셔너리

for i in range(3, n + 1):
    D[i] = (D[i - 1] + D[i - 2]) % 10007

print(D[n])
