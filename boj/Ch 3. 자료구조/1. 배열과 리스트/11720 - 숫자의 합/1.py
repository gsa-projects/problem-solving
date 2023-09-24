import sys

# AC. Python 3
problem_url = "https://boj.kr/11720"
problem_name = "숫자의 합"
input = sys.stdin.readline

n = int(input())
print(sum(map(int, input().strip())))
