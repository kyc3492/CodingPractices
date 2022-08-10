import heapq
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())   
    min_heap = []
    max_heap = []
    visited = [False] * N
    
    for i in range(N):
        c, n = input().split()

        if c == "I":
            heapq.heappush(min_heap, (int(n), i))
            heapq.heappush(max_heap, ((-int(n)), i))
            visited[i] = True

        elif c == "D":
            if int(n) == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif int(n) == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print("%d %d" % (-max_heap[0][0], min_heap[0][0]))