# Preview of sort.py

### 1. Selection Sort
    def selection_sort(arr):
        # initialzation minimum value
        min = 0
        tmp = 0
        for i in range(len(arr)-1):
            min = i
            for j in range(i+1, len(arr)):
                # j를 도는 반복문에서는 i를 제외한 나머지 배열들을 순회하여 가장 작은 값을 찾아낸다
                if arr[j] <= arr[min]:
                    # 가장 작은 값의 위치를 가져온다
                    min = j
            # 위에서 기준 값보다 작은 값을 정말로 찾아왔는지 검증한다
            if arr[min] <= arr[i]:
                # swap 과정
                tmp = arr[i]
                arr[i] = arr[min]
                arr[min] = tmp
            # 전체 sorting flow printing
            # print(arr)
        print(f'Selection sort result: {arr}')
---
### 2. Insertion Sort
    def insertion_sort(arr):
        # 첫 번째 for문은 기준값을 선정하는 것으로! (맨 왼쪽 부터 오른쪽으로 갈 수 있게!)
        # 근데 맨 왼쪽은 어차피 비교가 안되니까 1 ~ len(arr)로 하자
        for i in range(1, len(arr)):
            s_num = i
            # 두 번째 for문은 비교 배열들을 가져와야한다. 첫 번째부터 기준값 전까지!
            # i-1 부터 0 까지 -1씩 감소
            for j in range(i-1, -1, -1):
                # for문 안에는 비교 배열들과 기준값을 비교하면서 만약 크거나 같다면 오른쪽으로 자리를 비켜줘야한다.
                # 그러면 기준 값의 자리를 먼저 비운 후 (tmp에 저장) 오른쪽으로 옮겨준다. 또한 s_num을 j로 바꿔준다 (나머지 배열값들과 비교하기 위해)
                if arr[s_num] <= arr[j]:
                    tmp = arr[s_num]
                    arr[s_num] = arr[j]
                    arr[j] = tmp
                    s_num = j
            # 전체 sorting flow printing
            # print(arr)
        print(f'Insertion sort result: {arr}')
---
### 3. Bubble Sort
    def bubble_sort(arr):
        # 첫번째 for문은 0 ~ len(arr)까지 돌게한다
        for i in range(len(arr)):
            # 두번째 for문은 0 ~ len(arr)-i-1까지 돌게 한다 -> 맨 마지막은 항상 큰 수가 들어가므로 (정렬)
            # 또한 -1을 해주는 이유는 인접한 두 index만 비교하므로 왼쪽을 기준으로 그다음 +1을 비교하므로 len(arr)-i를 써버리면 마지막 배열에 out of range 에러가 발생
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    tmp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = tmp
            # 전체 sorting flow printing        
            # print(arr)
        print(f'Bubble sort result: {arr}')
---
### 4. Merge Sort (재귀함수)
    def merge_sort(arr):
        # 먼저, 각 배열들을 sementation을 하자
        if len(arr) < 2:
            return arr
        # arr길이의 몫 (나누기 결과)
        mid = len(arr) // 2
    
        # left/right 각각 따로 나눔 -> 재귀함수 때문에 결국에는 한 가지만 남음 left -> left / right 또 나뉘어짐
        left = merge_sort(arr[:mid])
        # left 다 거친 후, right도 똑같이 작업 -> right -> left/right로 또 쪼갬
        right = merge_sort(arr[mid:])
    
        # merge할 arr 초기화
        merged_arr = []
        low = high = 0
    
        # 분열된 왼쪽, 오른쪽을 비교해서 가장 작은 것만 배열에 차곡차곡 쌓음 (서로의 배열 값을 다 꺼낼 때까지)
        while low < len(left) and high < len(right):
            if left[low] < right[high]:
                merged_arr.append(left[low])
                low += 1
            else:
                merged_arr.append(right[high])
                high += 1
        
        # 제일 마지막에는 제일 큰 두덩이끼리 나뉘게 되고, 결국에는 서로 합쳐진다
        merged_arr += left[low:]
        merged_arr += right[high:]
    
        # 각 쪼개져서 한 정렬 값들을 이전에 함수를 부른 친구에게 넘겨준다
        return merged_arr
---
### 5-1. Quick Sort (이 때, pivot의 값은 항상 입력받은 배열의 left값에 의거해 정해진다.)
    def partition(arr, p, r):
        pivot = arr[p]
        # low는 항상 pivot보다 +1의 위치에 and low는 r값 (right)의 위치에
        low = p + 1
        high = r

        # low가 high위치와 반전될 때 까지 진행
        while(low <= high):
            while(low <= r and arr[low] < pivot): low += 1
            while(high > p and arr[high] > pivot): high -= 1
    
            if(low <= high):
                tmp = arr[low]
                arr[low] = arr[high]
                arr[high] = tmp
    
        tmp = arr[p]
        arr[p] = arr[high]
        arr[high] = tmp
    
        return high

    def quick_sort(arr, left, right):
        if (left < right):
            # initialization pivot's value
            pivot = partition(arr, left, right)
            # pivot을 기준으로 왼/오른쪽 정렬 (부분 정렬)
            quick_sort(arr, left, pivot-1)
            quick_sort(arr, pivot+1, right)

    print(f'Quick sort result: {arr}')
---
### 5-2. Try another version!! Quick Sort -> 한개의 함수로 합친 것 (순수 재귀함수)
    def quick_sort2(arr, left, right):
        # quick sort 재귀 함수를 부를 때, left가 right보다 크면 안되므로 if문 선언
        if left >= right:
            return
    
        # pivot은 arr[left] (맨 처음 시작할 때는 arr[0]임)
        pivot = left
        # low (왼쪽에서 오른쪽으로 오는 변수) -> pivot을 제외해야 하므로 pivot+1로 선언
        low = left + 1
        # high (오른쪽에서 왼쪽으로 오는 변수)
        high = right
    
        # low가 high를 지나치면 위치가 역전되는 순간 이므로 반복문을 다음과 같이 설정한다
        while(low < high):
            # low가 right를 넘지않고 arr[low] -> low가 가르키는 값이 pivot보다 작다면 계속 low를 1씩 더해준다
            while(low <= right and arr[low] < arr[pivot]): low += 1
            # high가 left를 넘지않고 arr[high] -> high가 가르키는 값이 pivot보다 크다면 계속 high를 1씩 더해준다
            while(high > left and arr[high] > arr[pivot]): high -= 1
    
            # low, high가 정지한 상황일 때 (arr[low]가 pivot보다 큰 값을 마주침 and arr[high]가 pivot보다 작은 값을 마주침)
            # low가 high보다 크다면 (지나친 상황이면), high가 가르키는 값과 pivot 값을 그냥 바꿔준다 (이후 반복문이 깨짐짐)
            if (low > high): arr[high], arr[pivot] = arr[pivot], arr[high]
            # low가 high를 지나치지 않았으면, low and high가 가르키는 값들을 서로 바꿔주고 다시 반복을 시킨다
            else: arr[low], arr[high] = arr[high], arr[low]
    
        # 마지막으로 left / right 로 분할해서 구해준다
        # left ~ high - 1 // high + 1 ~ right (이때 high가 가르키는 값은 pivot이 되므로 pivot 기준으로 왼쪽 / 오른쪽을 담당함)
        quick_sort2(arr, left, high - 1)
        quick_sort2(arr, high + 1, right)
---
### 6. Heap Sort
    def heapify(arr, arr_len):
        # 처음 arr가 들어오면 맨 밑에서 부터 큰 값이 있으면 끌어올려야 한다
        last_parent = arr_len // 2 - 1

        # current는 last_parent ~ 0 까지 1씩 감소하게 되고, 이는 마지막 parent로 부터 parent가 쭉 올라감을 의미한다.
        for current in range(last_parent, -1, -1):
            # 마지막에 current가 가르키는 값과 child값을 비교해서 바꿔주고 child가 혹시나 밑에도 바꿔줘야 하는 수가 있을 수도 있으므로 이런 반복문 사용 (위쪽을 고려한 것)
            while current <= last_parent:
                # 이때 child는 왼쪽 자식 노드를 의미하고 sibiling은 오른쪽 자식 노드를 의미한다
                child = current * 2 + 1
                sibiling = child + 1
                
                # 오른쪽 노드가 없는 경우도 있으므로 그것을 확인해주고 오른쪽 노드가 왼쪽 노드보다 더 값이 크다면, max heap을 위해 더 큰 값을 바꿔줘야하므로 child index를 바꿔준다
                if sibiling < arr_len and arr[child] < arr[sibiling]: child = sibiling
                # 자식노드랑 부모노드랑 비교해서 자식노드가 더 크다면 값을 바꿔주고, 자식노드를 current(부모)로 삼아서 자식노드들이 있는지 확인한다 (바꿔줘야하므로)
                if arr[current] < arr[child]:
                    arr[current], arr[child] = arr[child], arr[current]
                    current = child
                # 그렇지 않다면, 더이상 비교할게 없음 (max heap만족)
                else: break
                    

    def heapsort(arr):
        # 마지막 레벨에 있는 node들을 접근하기 위해 1씩 감소시키는 반복문을 사용하였다.
        for i in range(len(arr), 1, -1):
            heapify(arr, i)
            arr[0], arr[i-1] = arr[i-1], arr[0]


