import sys

# AC. Python 3
problem_url = "https://boj.kr/1546"
problem_name = "평균"
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
sum = sum(scores) / max(scores) * 100

print(sum / n)
