import sys
from dataclasses import dataclass

# WC. PyPy3
#  - 1377번이랑 똑같은 코드 넣어봤는데 틀렸습니다 가 뜬다.
#  - [1, 1]를 넣으면 0이 아니라 1이 나오는 것이 문제
#  - 갑자기 1377번이 왜 AC를 맞는지 이해가 안된다. [3, 2, 1]을 정렬할 때
#  - [3, 2, 1] -> [2, 3, 1] -> [2, 1, 3] -> [1, 2, 3]
#  - 1377번에서 우리가 마지막에 +1을 한 건, for 문이 스왑을 하지 않아 헛스윙을 할 때의 인덱스가 스왑 + 1이였기 때문
#  - 근데 위의 3 2 1 예제에서는 1을 내비두고 2, 3을 스왑하기 때문에 1의 스왑을 한 번 하지 않고 횟수가 하나 증가해서 이게 우연히 + 1과 맺어져서 결과값은 같긴 함
#  - 뭐지 1377 왜 맞았지?
#  - 1377번은 스왑의 개수를 세는 것이 아니라 스왑이 1개 이상 일어난 for의 루프 개수 + 1(헛스윙)를 세는거임 ㅇㅎ
problem_url = "https://boj.kr/1517"
problem_name = "버블 소트"
input = sys.stdin.readline

# idea: 버블 소트할 때, 어떤 값이 1 iteration에 몇 번 오른쪽으로 밀리는지 알 수 있을까?
#  그건, 그 값이 겁나게 크다면 1 iteration에 끝까지도 쭈루룩 밀릴 수 있기 때문에 알 수 없다.
#  다만, 왼쪽으로는 진행하지 않으므로, 왼쪽으로 가는 것은 오직 다른 값에 의해 swap 된 경우 뿐이라, 최대 1번이다.

@dataclass
class element:
	value: int
	origin_idx: int
	
	def __repr__(self):
		return f"[{self.origin_idx}]={self.value}"
	
	__str__ = __repr__

n = int(input())
A = list(map(int, input().split()))
for i in range(n):
	A[i] = element(value=A[i], origin_idx=i)
A_sort = sorted(A, key=lambda x: x.value)

print(A)
print(A_sort)

max_count = 0
for j in range(n):
	i = A_sort[j].origin_idx
	
	count = i - j + 1
	# print(i, j, count)
	
	if count > max_count:
		max_count = count

print(max_count)
