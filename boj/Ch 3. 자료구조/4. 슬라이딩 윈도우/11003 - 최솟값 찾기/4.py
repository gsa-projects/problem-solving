import sys
from collections import deque
from dataclasses import dataclass

# WC. PyPy3
#  - 시간 초과
problem_name = "최솟값 찾기"
problem_url = "https://boj.kr/11003"
input = sys.stdin.readline

@dataclass
class Item:
	index: int
	value: int
	
	def __eq__(self, other):
		return isinstance(other, Item) \
			and self.index == other.index \
			and self.value == other.value

length, delay = map(int, input().split())
numbers = list(map(int, input().split()))
deq: deque[Item] = deque()
minimums = []

# naive
# for i in range(length):
# 	minimums.append(min(numbers[max(0, i - delay + 1):i + 1]))

for i in range(length):
	deq = deque([d for d in deq if not (d.value > numbers[i] or i - d.index >= delay)])
	deq.append(Item(i, numbers[i]))
	minimums.append(deq[0].value)

for minimum in minimums:
	print(minimum, end=' ')
