n = int(input())

# 어케 묶냐면:
# (a, 1)는 a*1 < a+1 이므로 1은 묶지 않고 무조건 더하기
# (-n, -m)은 곱해서 양수 만들기 -> 가장 큰 것부터 곱하기
# (n, m)은 큰 것부터 곱하기
# 0은 음수가 남았을 때 곱해서 없애주거나 안 남으면 더하기

sum = 0
P, N = [], []
zero = False
for _ in range(n):
    x = int(input())

    if x == 1:
        sum += x
    elif x == 0:
        zero = True
    elif x > 0:
        P.append(x)
    else:
        N.append(-x)

P.sort()
N.sort()

while len(P) >= 2:
    sum += P.pop() * P.pop()

while len(N) >= 2:
    sum += N.pop() * N.pop()

if P:
    sum += P[0]

if N and not zero:  # 0이 있다면 그리고 음수가 1개 남아 있다면 0과 곱해져 0이 더해짐 = 아무것도 안 함
    sum += -N[0]

print(sum)
