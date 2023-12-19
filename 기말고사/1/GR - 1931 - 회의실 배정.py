n = int(input())
A = [tuple(map(int, input().split())) for _ in range(n)]

# note: 일단 빨리 끝나는 회의부터 골라 하면 됨, 동시에 끝나면 빨리 시작하는 회의
#   - for 문으로 회의를 찾아나가다가 동시에 끝나는 회의들은 시작 시간을 정렬해야
#   - for 를 진행할수록 점점 같은 종료 시간 대비 회의 시간이 짧아질테니 연속으로 할 수도 수도 있?음
#   - 예시: (2, 2), (1, 3), (2, 3), (3, 3) -> (2, 2), (2, 3), (3, 3) 를 할 수 있음
#   - 근데 이걸 어떻게 알아내?

A.sort(key=lambda x: (x[1], x[0]))

cnt = 1     # note: 첫 회의는 일단 고름 <- 가장 빨리 끝나고 가장 빨리 시작함 (맨 처음이라 시작 시간은 딱히 상관 없음)
end = A[0][1]

for s, e in A[1:]:
    if end <= s:
        end = e
        cnt += 1

# for i in range(1, n):
#     if end <= A[i][0]:
#         end = A[i][1]
#         cnt += 1

print(cnt)
