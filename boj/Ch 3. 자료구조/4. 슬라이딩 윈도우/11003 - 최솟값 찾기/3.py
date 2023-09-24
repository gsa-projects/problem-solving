import sys
from collections import deque
from dataclasses import dataclass

# WC. Python 3
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
	tmp: deque[Item] = deque()
	
	for d in deq:
		if d.value > numbers[i] or i - d.index >= delay:
			# WC. 아마 이게 문제인 듯 - remove 하려면 다시 또 루프 돌아야 되니까 여기서 O(N) 생김
			continue
		tmp.append(d)
	
	deq = tmp
	deq.append(Item(i, numbers[i]))
	minimums.append(deq[0].value)

for minimum in minimums:
	print(minimum, end=' ')
