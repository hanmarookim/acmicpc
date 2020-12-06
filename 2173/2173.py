from collections import deque
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
visit = [0 for _ in range(N)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
visit[0] = 1
q = deque([((0,0), 1)])
while q:
    pos, dis = q.popleft()
    if pos == (N-1, M-1):
        print(dis)
        exit()
    for i in range(4):
        nx, ny = pos[0] + dx[i], pos[1] + dy[i]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == '1':
            if not visit[nx] & 1<<ny:
                q.append(((nx, ny), dis+1))
                visit[nx] = visit[nx] | 1<<ny
