n = int(input())

#%% bottom-up
D = [0] * (n + 1)
for i in range(2, n + 1):
    D[i] = D[i - 1] + 1     # 1을 빼는 방법
    if i % 2 == 0:  # 2로 나누는 방법
        D[i] = min(D[i // 2] + 1, D[i])
    if i % 3 == 0:  # 3으로 나누는 방법
        D[i] = min(D[i // 3] + 1, D[i])
    
#%% top-down
D = {1: 0}
# note: 맨 처음에 리스트로 시도했다가 털림
#   - 모종의 이유로 x가 0이 되었을 때 0은 조건문을 항상 만족하기에 0//2 -> 0, 0//3 -> 0... 계속 무한 루프가 생겼음
def topdown(x):
    if x not in D:
        if x % 6 == 0:
            D[x] = min(topdown(x // 2), topdown(x // 3)) + 1
        elif x % 3 == 0:
            D[x] = min(topdown(x // 3), topdown(x - 1)) + 1
        elif x % 2 == 0:
            D[x] = min(topdown(x // 2), topdown(x - 1)) + 1
        else:
            D[x] = topdown(x - 1) + 1
        
    return D[x]

print(topdown(n))
