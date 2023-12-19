n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
A.sort(key=lambda x: (x[1], x[0]))

end = A[0][1]
cnt = 1
for i in range(1, n):   # note: range(n) 으로 해서 틀림
    if end <= A[i][0]:
        end = A[i][1]
        cnt += 1

print(cnt)
