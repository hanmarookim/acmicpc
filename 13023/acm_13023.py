import sys
r = sys.stdin.readline
N, M = map(int, r().split())
graph = {i: [] for i in range(N)}
for _ in range(M):
    a, b = map(int, r().split())
    graph[a].append(b)
    graph[b].append(a)
stack = []
answer = False
for n in range(N):
    visit = 1 << n
    stack = [(n, visit, 1)]
    while stack:
        node = stack.pop()
        if node[2] >= 5:
            answer = True
            break
        for adj in graph[node[0]]:
            if not node[1] & (1 << adj):
                stack.append((adj, node[1]|(1<<adj), node[2]+1))
    if answer:
        break
print(1 if answer else 0)
