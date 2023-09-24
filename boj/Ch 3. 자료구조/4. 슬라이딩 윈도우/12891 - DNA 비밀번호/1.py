import sys

# WC. PyPy3
#  - 시간 초과
problem_name = "DNA 비밀번호"
problem_url = "https://boj.kr/12891"
input = sys.stdin.readline

length, part_length = map(int, input().split())
dna_str = input()
min_A, min_C, min_G, min_T = map(int, input().split())

min_limit = {'A': min_A, 'C': min_C, 'G': min_G, 'T': min_T}
count = 0
end = part_length

while end <= length:
	part = dna_str[end - part_length:end]
	
	freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	for c in part:
		freq[c] += 1
	
	if all(freq[k] >= min_limit[k] for k in freq):
		count += 1
	
	end += 1

print(count)
