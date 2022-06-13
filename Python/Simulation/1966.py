T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    Queue = list(map(int, input().split()))
    Order = []
    for i in range(N):
        Order.append(i)

    Counter = 0
    Primary = max(Queue)
    while 1:
        if Queue[0] == Primary:
            Counter += 1
            del Queue[0]
            if Order[0] == M:
                break
            else:
                del Order[0]
            Primary = max(Queue)
            N -= 1
        else:
            tmp_Queue = Queue[0]
            tmp_Order = Order[0]
            for i in range(N - 1):
                Queue[i] = Queue[i + 1]
                Order[i] = Order[i + 1]
            Queue.pop()
            Order.pop()
            Queue.append(tmp_Queue)
            Order.append(tmp_Order)

    print(Counter)