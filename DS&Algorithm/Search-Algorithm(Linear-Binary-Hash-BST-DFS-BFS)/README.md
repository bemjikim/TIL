# Preview of search.py

### 1. 선형 탐색 알고리즘
    # 배열을 하나씩 꺼내면서 key값과 매칭되는지 확인
    def linear_search(arr, key):
        for i in arr:
            if (i == key):
                print(f'{i} is here!')
                return
            
        print(f'{key} is not here!')
---
### 2. 이진 탐색 알고리즘
    # 전제조건: 정렬되어 있어야함.
    def binary_search(arr, key):
        while(1):
            # 시작은 중간에서부터 시작! 
            i = int(len(arr)/2)
            # try&catch 문을 사용하여 key값이 arr에 있지 않는 경우, 출력하게 만든다.
            try:
              # key값이 중간값보다 크다면, 배열을 i+1 번째 부터 배열의 끝까지 잘라서 배열을 다시 만든뒤, while문을 다시 순회한다. (왜냐하면 오름차순 정렬이기 때문 -> i+1 번째 이상인 원소들에서 key값을 찾을 수 있기 때문)
              if (arr[i] < key): arr = arr[i+1:]
              # 반대 case -> key값이 중간값보다 크다면, 0번째 부터 i-1번째까지 원소들에서 중간값을 다시 찾아 비교한다 (while문)
              elif (arr[i] > key): arr = arr[:i-1]
              # 만약 key값이 일치한다면, 출력 후 반복문을 정지한다.
              elif (arr[i] == key): 
                  print(f'{key} is here!')
                  break
            except:
              print(f'{key} is not here!')
---
### 3-1. 해시 탐색 알고리즘 (저장)
    def hash_search_save(arr, search_key):
        # key를 저장하는 배열의 크기를 일부러 2배가량 더 크게 만든다 (conflict 방지)
        arr_key_save = [0 for i in range(len(arr)*2)]
        # 데이터가 들어가있는 배열을 접근한다
        for i in range(len(arr)):
            # key값은 key배열의 크기에 modulo 연산을 통해 구하고
            key = arr[i] % len(arr)*2
            # 그 값을 위에서 선언한 arr_key_save 배열에 값이 들어가있는지 확인하고 없으면 그 key 값을 저장한다.
            if(arr_key_save[key] == None): arr_key_save[key] = arr[i]
            # 값이 이미 있으면 while문을 통해 key 값을 계속 1로 더하여 arr_key_save배열에서 빈공간을 찾는다
            else:
                while(arr_key_save[key]):
                    if(key < len(arr_key_save) - 1): key += 1
                    else: key = 0
                arr_key_save[key] = arr[i]
        print(arr_key_save)
        hash_search(arr_key_save, search_key)
    
### 3-2. 해시 탐색 알고리즘 (탐색)
    def hash_search(arr, target):
        # 탐색은 위에서 저장한 것 처럼 arr_key_save배열의 크기만큼 modulo 연산을 통해 key값을 찾고
        key = target % len(arr)

        # 반복문을 통해 찾을 때 까지 key값을 +1 해주며 탐색한다.
        while(arr[key] != target):
            key = (key + 1) % len(arr)
        
        print(f'{target}가 존재하고 {key + 1}번 째에 존재합니다.')
---
### 4-0. 이진 탐색 트리 (전체 - linked list가 아닌 배열로 구현)
    def binary_search_tree_arr(key):
        # 빈 arr에 트리 구성 (100개)
        arr = [None for i in range(100)]
        while(1):
            # index 선택
            print('Select index you want (1)Insert (2)Delete (3)Search: ', end = '')
            select = int(input())
            # 삽입 알고리즘 선택
            if(select == 1):
                while(1):
                    print('Insert the number for insert (if you quit, input 0): ', end = '')
                    input_num = int(input())
                    if input_num == 0:
                        break
                    binary_search_tree_insert(arr, input_num)
            elif(select == 2):
                while(1):
                    print('Insert the number for delete (if you quit, input 0): ', end = '')
                    input_num = int(input())
                    if input_num == 0:
                        break
                    binary_search_tree_delete(arr, input_num)
            else:
                binary_search_tree_find(0, arr, key)

### 4-1. 이진 탐색 트리 (탐색)
    def binary_search_tree_find(root, arr, key):
        while(root < len(arr)):
            if (arr[root] == None): return 0
            lchild_idx = (root + 1) * 2 - 1
            rchild_idx = (root + 1) * 2
            # 현재 노드가 key값과 일치하면 해당 index 리턴
            if(arr[root] == key): 
                print(f'{key}가 존재하고 {root + 1}번 째에 존재합니다.')
                return root
            # 현재 노드가 key값 보다 작다면, 해당 노드에서 오른쪽 자식 노드 index를 확인 후, root를 옮겨준다
            elif(arr[root] < key): 
                if(rchild_idx < len(arr)) and (arr[rchild_idx] != None): 
                    root = rchild_idx
                # 그렇지 않다면, 해당 마지막 탐색 노드의 index를 return한다.
                else: 
                    print(f'{key}가 배열에 존재하지 않습니다.')
                    return rchild_idx
            # 현재 노드가 key값 보다 크다면, 해당 노드에서 왼쪽 자식 노드 index를 확인 후, root를 옮겨준다
            else:
                if(lchild_idx < len(arr)) and (arr[lchild_idx] != None):
                    root = lchild_idx
                # 그렇지 않다면, 해당 마지막 탐색 노드의 index를 return한다.
                else: 
                    print(f'{key}가 배열에 존재하지 않습니다.')
                    return lchild_idx
            
### 4-2. 이진 탐색 트리 (삽입)
    def binary_search_tree_insert(arr, key):
        # 먼저 탐색 후, 알맞은 자리를 return함
        idx = binary_search_tree_find(0, arr, key)
        # 탐색한 값이 존재하는지 확인! 있으면 그냥 값을 넣지 않고 return함
        if(arr[idx] != None) and (key == arr[idx]):
            print('이미 값이 배열안에 존재합니다.')
            return
        # 값이 존재하지 않는다면 해당 자리에 삽입
        else:
            arr[idx] = key

    print(f'arr는 다음과 같습니다 >> {arr}')

### 4-3. 이진 탐색 트리 (삭제)
    def binary_search_tree_delete(arr, key):
        # 먼저 탐색 후, 알맞은 자리를 return함
        idx = binary_search_tree_find(0, arr, key)
        # 탐색한 값이 존재하는지 확인! 있으면 그냥 값을 넣지 않고 return함
        if (key == arr[idx]):
            print(f'{key}값을 정상적으로 삭제했습니다.')
            # 해당 노드가 자식 노드를 가지고 있는지 확인
            lchild_idx = (idx + 1) * 2 - 1
            rchild_idx = (idx + 1) * 2
            # 1) Leaf Node일 경우 -> 그냥 삭제
            if(arr[lchild_idx] == None) and (arr[rchild_idx] == None):
                arr[idx] = None
            # 2) 자식 Node가 한 개일 경우 -> 칸을 땡겨 온다
            elif(arr[lchild_idx] == None) or (arr[rchild_idx] == None):
                # 해당되는 값을 일단 삭제한다
                arr[idx] = None
                # 재귀 함수로 계속 땡겨와야 할 듯
                if arr[lchild_idx != None]:
                    # 왼쪽 노드 한 개만 가지고 있을 경우에는, 지워진 node에 가지고 있던 왼쪽 노드의 값과 왼쪽노드의 자식 노드들을 함수의 parameter로 넣어준다
                    arr[idx] = arr[lchild_idx]
                    binary_search_tree_delete2(arr, idx, glchild = (lchild_idx + 1) * 2 - 1, grchild= (lchild_idx + 1) * 2, flag = 0)
                else:
                    # 오른쪽 노드 한 개만 가지고 있을 경우에는, 지워진 node에 가지고 있던 오른쪽 노드의 값과 오른쪽 노드의 자식 노드들을 함수의 parameter로 넣어준다
                    arr[idx] = arr[rchild_idx]
                    binary_search_tree_delete2(arr, idx, glchild = (rchild_idx + 1) * 2 - 1, grchild= (rchild_idx + 1) * 2, flag = 1)
        # 값이 존재하지 않는다면 그냥 return함
        else:
            return
        print(f'arr는 다음과 같습니다 >> {arr}')

### 4-4. 이진 탐색 트리 (삭제2) -> 배열을 다 앞으로 당기는 알고리즘 (배열 구현 중도 포기 (삭제 알고리즘에서 두 개의 자식 노드가 다 존재할 경우가 구현이 어려움))
    def binary_search_tree_delete2(arr, parent, glchild, grchild, flag):
        ############## 아래 알고리즘은 일단 자식노드가 한 개일 때를 가정함 #################### 
    
        # 자식의 자식 노드들이 없으면 실행을 중지
        if(arr[glchild] == None) and (arr[grchild] == None):
            return
        # parent의 자식노드들을 설정
        lchild, rchild = (parent + 1) * 2 - 1, (parent + 1) * 2
        
        # parent의 자식노드에 자식의 자식노드들의 값을 넣어줌
        arr[lchild], arr[rchild] =  arr[glchild], arr[grchild]
    
        # 그리고 그 자식의 자식노드들 값을 None으로 변경 (최종적으로는 제일 마지막 노드들이 None이 되면서 최종 변경 완료!)
        arr[glchild], arr[grchild] = None, None
    
        # 그리고 또 바꿔줄 자식의 자식 노드들을 다시 설정 
        l_glchild, l_grchild = (glchild + 1) * 2 - 1, (glchild + 1) * 2
        r_glchild, r_grchild = (grchild + 1) * 2 - 1, (grchild + 1) * 2
    
        # flag를 설정한 이유는, 왼쪽 자식 노드만 있을 경우에는 오른쪽을 먼저 바꿔줘야한다. (그 이유는 왼쪽 부터 바꿔주면 왼쪽 자리에 기존에 바꾸지 않은 오른쪽 자리에 들어가기 때문에 오른쪽 값을 잃어버린다)
        if flag == 0:
            binary_search_tree_delete2(arr, rchild, r_glchild, r_grchild)
            binary_search_tree_delete2(arr, lchild, l_glchild, l_grchild)
        # 마찬가지
        else:
            binary_search_tree_delete2(arr, lchild, l_glchild, l_grchild)
            binary_search_tree_delete2(arr, rchild, r_glchild, r_grchild)

---
### 4-6. BST Linked List로 바꿈
    class Node:
        def __init__(self, value) -> None:
            self.value = value
            self.left = None
            self.right = None
    
    # Node Management
    class NodeMgmt:
        def __init__(self, head) -> None:
            # head는 여기서 root를 의미함함
            self.head = head
    
        def insert(self, value) -> None:
            self.current_node = self.head
            while(True):
                # 입력한 값이 현재 노드의 값보다 작다면!
                if(value < self.current_node.value):
                    # 왼쪽 노드가 존재할 경우, 왼쪽 노드를 현재 노드로 변경하고 반복문을 재 수행한다
                    if(self.current_node.left != None):
                        self.current_node = self.current_node.left
                    # 왼쪽 노드에 아무것도 존재 하지 않으면, 그 자리에 새로 생성
                    else:
                        self.current_node.left = Node(value)
                        break
                # 입력한 값이 현재 노드의 값보다 크다면!
                elif(value > self.current_node.value):
                    # 오른쪽 노드가 존재할 경우!! (위 상황의 반대)
                    if(self.current_node.right != None):
                        self.current_node = self.current_node.right
                    else:
                        self.current_node.right = Node(value)
                        break
                # 입력한 값이 이미 존재한다면 message print후, 종료
                else:
                    print(f'{value} is already in BST!')
                    break
    
        def search(self, value) -> bool:
            self.current_node = self.head
    
            # 현재 노드가 None이 아닐 때 까지 돔
            while self.current_node:
                # 값을 찾으면 return True
                if(self.current_node.value == value):
                    return True
                # 찾는 값이 현재 노드의 값보다 크다면, 현재 노드를 오른쪽으로 옮김
                elif(self.current_node.value < value):
                    self.current_node = self.current_node.right
                # 찾는 값이 현재 노드의 값보다 작다면, 현재 노드를 왼쪽으로 옮김
                elif(self.current_node.value > value):
                    self.current_node = self.current_node.left
            # 값을 찾지 못한다면, return False
            return False
        
        def delete(self, value) -> bool:
            # 삭제할 노드 (계속 변경될 거임)
            self.current_node = self.head
            # 삭제할 부모 노드 (삭제할 노드의 부모노드)
            self.parent = self.head
    
            # 삭제하려는 노드가 실제로 BST안에 있는지 확인 (search와 비슷) -> 부모노드도 맞춰서 이동
            while(self.current_node):
                if(self.current_node.value == value):
                    searched = True
                    break
                elif(value < self.current_node.value):
                    self.parent = self.current_node
                    self.current_node = self.current_node.left
                else:
                    self.parent = self.current_node
                    self.current_node = self.current_node.right
    
            # 없으면 그냥 반환한다.
            if searched == False:
                return False
            
            # case1 (leaf node 일 경우에)
            if(self.current_node.left == None) and (self.current_node.right == None):
                # 삭제할 노드가 부모의 왼쪽에 있는지 오른쪽에 있는지 확인한다
                if(value < self.parent.value):
                    self.parent.left = None
                else:
                    self.parent.right = None
            # case2 (child node를 하나라도 가지고 있는 경우)
            # 왼쪽 child node만 가지고 있는 경우 (한 개만 바꿔주면 linked list라서 다 따라오게 된다)
            elif(self.current_node.left != None) and (self.current_node.right == None):
                # 삭제할 노드가 부모의 왼쪽에 있는지 오른쪽에 있는지 확인한다
                if(value < self.parent.value):
                    self.parent.left = self.current_node_left
                else:
                    self.parent.right = self.current_node_left
    
            # case 3-1 (삭제할 노드가 parent node의 왼쪽에 있는 경우)
            # 3-1-1. 삭제할 노드의 오른쪽 자식 중, 가장 작은 값을 가진 node의 child node가 없을 경우
            # 3-1-2. 삭제할 노드의 오른쪽 자식 중, 가장 작은 값을 가진 node의 오른쪽 child node가 있을 경우 (왼쪽에 있으면 그 node가 target이 될 것이므로 배제)
            elif (self.current_node.left != None) and (self.current_node.right != None):
                # case 3-1
                # 왼쪽 자식들을 그냥 해제하고 연결하면 되는데, right는 왼쪽 node에 새로이 연결 되어야 하므로 일단단 change_node라고 설정한다.
                if(value < self.parent.value):
                    # 이때, current node는 삭제되는 노드를 가르킨다.
                    self.change_node = self.current_node.right
                    self.change_node_parent = self.current_node.right
    
                    # 가장 작은 값들은 맨 왼쪽에 존재하므로 (오른쪽 노드 중)
                    while(self.change_node.left != None):
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                    
                    # 3-1-2 오른쪽 자식 노드가 존재한다면, change_node_parent의 왼쪽에 해당 노드를 연결한다다
                    if(self.change_node.right != None):
                        self.change_node_parent.left = self.change_node.right
                    # 3-1-1
                    else:
                        self.change_node_parent.left = None
    
                    # 위치 재설정
                    self.parent.left = self.change_node
                    # change_node의 오른쪽을 기존 삭제된 노드의 오른쪽을 연결시킨다.
                    self.change_node.right = self.current_node.right
                    self.change_node.left = self.current_node.left
                
                # 3-2 (삭제할 노드가 parent node의 오른쪽에 있는 경우!)
                # 3-2-1 위와 동일! 삭제할 오른쪽 자식중, 가장 작은 값을 가지는 노드의 child 노드가 존재하지 않는 경우 
                # 3-2-2 위와 동일! 삭제할 오른쪽 자식중, 가장 작은 값을 가지는 노드의 child 노드중 오른쪽 child node가 존재하는 경우우
                else:
                    # 이때, current node는 삭제되는 노드를 가르킨다.
                    self.change_node = self.current_node
                    self.change_node_parent = self.current_node
    
                    while(self.change_node.left != None):
                        self.change_node_parent = self.change_node
                        self.change_node = self.change_node.left
                    
                    # 3-2-2
                    if(self.change_node.right != None):
                        self.change_node_parent.left = self.change_node.right
                    # 3-2-1
                    else:
                        self.change_node_parent.left = None
                    
                    # 위치 재설정
                    self.parent.right = self.change_node
                    self.change_node.left = self.current_node.left
                    self.change_node.right = self.current_node.right
    
    def binary_search_tree_link(key):
        head = Node(1)
        BST = NodeMgmt(head)
        BST.insert(2)
        BST.insert(3)
        BST.delete(2)
---
### 5-1. BFS 구현 (dictionary 형식)
    from collections import deque
    
    graph={
      '1' : ['2','3','8'],   # 1
      '2' : ['1','7'],     # 2
      '3' :['1','4','5'],   # 3
      '4' : ['3','5'],     # 4
      '5' : ['3','4'],     # 5
      '6' : ['7'],       # 6
      '7' : ['2','6','8'],   # 7
      '8' : ['1','7']      # 8
    }
    
    
    def dic_bfs(g, start):
        # 시작 값으로 큐 초기화 (1이 들어가 있음음)
        queue = deque([start])
        # 노드를 방문 처리 한다.
        visited = set([start])
        # 그래프를 순환하면서 주변에 있는 노드를 가져온다
        while queue:
            # 선입선출
            v = queue.popleft()
            print(v)
            for i in g[v]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)

### 5-2. BFS 구현 (2D array 방식)
    graph = [
            ['O', 'O', 'O', 'O', 'O', 'X'],
            ['O', 'O', 'O', 'O', 'X', 'O'],
            ['O', 'O', 'O', 'X', 'O', 'O'],
            ['O', 'O', 'X', 'O', 'O', 'O'],
            ['X', 'O', 'O', 'O', 'O', 'O'],
        ]
    
    def arr_bfs(start_x, start_y, graph):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
    
        queue = deque([(start_x, start_y)])
        visited = set([(start_x, start_y)])
    
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
    
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
---
### 6-1. dfs (재귀함수, dictionary 방식)
    graph = [
        [],      # 0
        [2, 3],  # 1 
        [4, 5],  # 2
        [6],     # 3
        [2, 5],  # 4
        [2, 4],  # 5
        [3, 7],  # 6
        [6]      # 7
    ]
    
    visited = [False] * 8
    
    def r_dfs(v):
        # 먼저 들어온 것을 visited true로 만듦
        visited[v] = True
        print(v)
    
        for i in graph[v]:
            if visited[i] == False:
                visited[i] = True
                r_dfs(i)

### 6-2. dfs (반복문 stack 사용, dictionary) - 맨 오른쪽부터 dfs
    graph = [
            [],      # 0
            [2, 3],  # 1 
            [4, 5],  # 2
            [6],     # 3
            [2, 5],  # 4
            [2, 4],  # 5
            [3, 7],  # 6
            [6]      # 7
        ]
        
    visited = [False] * 8
        
    def i_dfs(v):
        visited[v] = True
        stack = []
        stack.append(v)
    
        while stack:
            v = stack.pop()
            print(v)
            for i in graph[v]:
                if visited[i] == False:
                    visited[i] = True
                    stack.append(i)
