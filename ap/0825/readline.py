import sys

n, payload_limit = map(int, sys.stdin.readline().split())

weights = []
values = []
for _ in range(n):
	w, v = map(int, sys.stdin.readline().strip().split())
	weights.append(w)
	values.append(v)

print(n, payload_limit)
print(weights)
print(values)