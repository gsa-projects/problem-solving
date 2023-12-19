expr = input().strip()
S = [sum(map(int, e.split('+'))) for e in expr.split('-')]
print(S[0] - sum(S[1:]))
