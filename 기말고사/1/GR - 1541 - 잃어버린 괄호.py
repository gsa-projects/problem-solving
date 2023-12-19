expr = input().strip()

# note: 55-50+40 -> 55-(50+40) 이렇게 하면 최소 -> '-' 로 스플릿하고 싹다 묶어서 더해버려
#   - 문제에서 '-'로 시작하는 수식을 없다고 했으니 반례는 없음

A = [sum(map(int, e.split('+'))) for e in expr.split('-')]
print(A[0] - sum(A[1:]))
