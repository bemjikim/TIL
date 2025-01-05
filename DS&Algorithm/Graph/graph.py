# Graph를 활용한 Dijkstra, Bellman Ford, Floyd Warshall Algorithms들 구현!

# 1. Dijkstra Algorithm
""" This is input value. you can just copy and paste it. 
5 6 1
1 2 3
1 4 8
1 5 9
2 1 2
2 3 2
3 2 2
3 4 1
3 5 3
4 1 8
4 3 1
5 1 9
"""
import heapq

def dijkstra(start):
    heap = [] 
    # 최소 힙에서 힙 push (Initial value - 자기자신은 가중치가 0)
    heapq.heappush(heap, [0, start])
    # 무한대 값 설정
    INF = float('inf')
    # vertex의 개수 + 1 개만큼 설정한다 (왜냐하면 그래프의 구조가 1부터 시작하므로! 0번째는 배제해야함)
    # 이때, weights는 dp table로 설정한다 (계속 최적의 상태를 업데이트 해줘야 하므로)
    weights = [INF] * (vertex + 1)
    # 함수의 파라미터 (시작하는 노드)를 0으로 만들어준다 (자기자신은 0이므로)
    weights[start] = 0

    # heap 안에 있는 것을 다 꺼낼 때 까지
    while heap:
        weight, node = heapq.heappop(heap)
        # weight 값이 dp table안에 들어있는 값보다 크다면 고려할 필요가 없음
        if weight > weights[node]:
            continue
        
        for n, w in graph[node]:
            # graph안에 이웃된 노드와 weight를 확인
            # 현재 weight와 가르키고 있는 노드의 weight를 더함
            up_w = weight + w
            # 만약 그 값이 dp talble안에 있는 값 보다 작다면, 해당 값으로 dp table 업데이트
            if weights[n] > up_w:
                weights[n] = up_w
                # 그리고 그 노드와 weight를 push해서 나중에 꺼내서 업데이트 할 수 있도록 함
                heapq.heappush(heap, [up_w, n])
    return weights

vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex+1)]

for i in range(vertex + edge):
    src, dst, weight = map(int, input().split())
    graph[src].append([dst, weight])

weights = dijkstra(1)
print(weights)

# 2. Bellman Ford Algorithm
""" This is input value. you can just copy and paste it. 
5 9
1 2 -6
1 3 3
1 4 9
1 5 8
2 3 -2
3 4 5
3 5 -7
4 3 -4
5 3 -13
"""
def bellman_ford(start):
    weights[start] = 0
    # i = 0 ~ V-1 까지 v번 반복한다
    for i in range(v):
        # graph에서 src, dst, weight를 뽑아와서
        for src, dst, weight in graph:
            # src까지의 거리비용과 src -> dst 거리 비용을 미리 더한다
            up_w = weights[src] + weight
            # src가 INF가 아니고 (만약 INF면 나중에 자기자신이 업데이트하게 냅둬야함) dp table값보다 up_w값이 작다면 해당 값으로 업데이트! 
            if weights[src] != INF and weights[dst] > up_w:
                weights[dst] = up_w
                # 0 ~ v-1번째 까지인데, 1~v 까지로 볼 수 있다. 즉, v번까지 반복문이 돌았다는 의미인데, v-1번까지 돌고 그 다음 반복문 부터는 dp table의 값이 변하면 안된다. 
                # 그러나 v번째 반복문에서 dp table값이 변했다는 것은, 음의 사이클이 존재한다는 의미로 False를 return하는 것이다.
                if i == v-1:
                    return False
    return True
            
# 입력 받는 노드와 간선의 개수
v, e = map(int, input().split())
# graph 초기화
graph = []

# 간선의 개수를 반복하며 src, dst, weight를 입력받는다 (src -> dst를 가르키는 weight)
for _ in range(e):
    src, dst, weight = map(int, input().split())
    graph.append([src, dst, weight])

# INF 값 초기화
INF = float('inf')
weights = [INF] * (v + 1)

# 만약 이 그래프가 음순환을 하지 않는다면, 최소비용을 가진 dp table 출력!
if bellman_ford(1):
    for i in range(1, v+1):
        print(i, end='')
# 아니라면... 이것은 음순환을 가진 그래프임을 명시!
else:
    print('Graph has negative cycle!')


# 3. Floyd Warshall Algorithm
""" This is input value. you can just copy and paste it.
4 7
1 2 5
1 4 7
2 1 4
2 3 -3
3 1 6
3 4 4
4 3 2
"""
# vertex, edge의 개수 입력
v, e = map(int, input().split())
# INF 초기화
INF = float('inf')
# 위의 dp table이라 봐도 됨. -> 2차원 배열로 만듦
graph = [[INF] * (v + 1) for _ in range(v + 1)]

# edge 개수만큼의 src->dst의 가중치를 입력
for _ in range(e):
    src, dst, weight = map(int, input().split())
    graph[src][dst] = weight

# k를 필두로 반복문 시작
for k in range(1, v + 1):
    # 자기 자신은 0으로 초기화
    graph[k][k] = 0
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            # i->j 값이랑 i->k->j 값을 비교해서 작은 값을 채택
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 최종 graph의 최소비용 출력
for i in range(1, v + 1):
    for j in range (1, v + 1):
        print(graph[i][j], end = " ")
    print()