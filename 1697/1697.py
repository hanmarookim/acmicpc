from collections import deque
chk = [0 for i in range(100001)]
N,K=map(int,input().split())
if K < N:
    print(N-K)
else:
    queue = deque()
    visit = []
    queue.append((N,0))
    answer = -1
    while queue:
        node = queue.popleft()
        if node[0] == K:
            answer = node[1]
            break
        visit.append(node[0])
        if node[0]+1 <= 100000 and chk[node[0]+1] == 0:
            chk[node[0]+1] = 1
            queue.append((node[0]+1, node[1]+1))
        if node[0]-1 >= 0 and chk[node[0]-1] == 0:
            chk[node[0]-1] = 1
            queue.append((node[0]-1, node[1]+1))
        if node[0]*2 <= 100000 and chk[node[0]*2] == 0:
            chk[node[0]*2] = 1
            queue.append((node[0]*2, node[1]+1))
    print(answer)
