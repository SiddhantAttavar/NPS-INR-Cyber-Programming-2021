# Import priority queue
from queue import PriorityQueue
from sys import setrecursionlimit
setrecursionlimit(int(1e6))

# Take input
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
	u, v, w = map(int, input().split())
	graph[u - 1].append((v - 1, w))
	graph[v - 1].append((u - 1, w))

# Dijkstras algorithm
dist = [int(3e9)] * n
dist[0] = 0
pq = PriorityQueue()
pq.put((0, 0))

while not pq.empty():
	d, u = pq.get()

	for v, w in graph[u]:
		x = d + w
		if x < dist[v]:
			dist[v] = x
			pq.put((x, v))

for i in range(1, len(dist)):
	if dist[i] == int(3e9):
		dist[i] = -1

print(*dist[1:])
assert int(3e9) not in dist
