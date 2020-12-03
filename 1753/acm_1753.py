import sys
import heapq

V,E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = {i: {} for i in range(1, V+1)}
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    try:
        if graph[u][v] > w:
            graph[u][v] = w
    except ImportError:
         graph[u][v] = w
INF = 10*300000 + 1
distance = [INF for _ in range(V)]
distance[K-1] = 0
heap = []
heapq.heappush(heap, (0, K))
while heap:
    node = heapq.heappop(heap)
    for adj in graph[node[1]]:
        if distance[adj-1] > node[0] + graph[node[1]][adj]:
            distance[adj-1] = node[0] + graph[node[1]][adj]
            heapq.heappush(heap, (node[0] + graph[node[1]][adj], adj))
for d in distance:
    print(d if d != INF else 'INF')
