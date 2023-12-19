n = int(input())
D = [0] * (n + 1)
D[1] = 1

# note: base case가 n보다 큰 경우를 고려해야함. n = 1이면 D의 길이는 2라서 D[2]는 KeyError임
if n > 1:
    D[2] = 2

for i in range(3, n + 1):
    # note: 10007로 나눈 나머지로 출력하라는 것 좀 문제 꼼꼼히 보셈
    D[i] = (D[i - 1] + D[i - 2]) % 10007

print(D[n])
