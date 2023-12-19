n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]

cnt = 0
# for i in range(n - 1, -1, -1):
#     # note: 이렇게 풀어도 맞지만 마치 괄호 문제에서 exit 빨리 안 했다고 감점되기 딱 좋은 경우
#     c, k = divmod(k, A[i])
#     cnt += c

for a in reversed(A):
    c, k = divmod(k, a)
    cnt += c

    if k == 0:
        print(cnt)
        exit()
