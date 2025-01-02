# Preview of stack-queue-circularqueue.py

### Stack & Queue 모두 기존 append(), pop(), del 함수를 사용해서 비교적 간단하게 구현함
### 1. Stack
    def f_stack():
        stack = []
    
    while(1):
        opt_num = int(input("Stack selection option: 1.push, 2.pop, 3.Exit: "))

        if opt_num == 1:
            push_num = int(input("Input the number: "))
            stack.append(push_num)
            print(f"Stack array is {stack}")

        elif opt_num == 2:
            stack.pop()
            print(f"Stack array is {stack}")
        
        else: break
---
### 2. Queue
    def f_queue():
        queue = []
    
    while(1):
        opt_num = int(input("Queue selection option: 1.push, 2.pop, 3.Exit: "))

        if opt_num == 1:
            push_num = int(input("Input the number: "))
            queue.append(push_num)
            print(f"Queue array is {queue}")

        elif opt_num == 2:
            del queue[0]
            print(f"Queue array is {queue}")
        
        else: break
---
### 3. Circular Queue
    #이때, cirqueue의 배열의 크기는 6으로 고정하고 빈 배열을 None으로로 가정하자.
    def f_cirqueue():
        # 변수 초기화화
        cirqueue = [None, None, None, None, None, None]
        rear = 0
        front = 0

    while(1):
        opt_num = int(input("Circular queue selection option: 1.push, 2.pop, 3.Exit: "))

        if opt_num == 1:
            # 만약, rear = front가 같다면, 배열이 가득차거나 빈 상태이므로 추가적으로 배열 안에 None이 들어가있는지 확인한다. (빈 배열을 None이라고 가정했으므로로)
            if rear == front and not None in cirqueue:
                print("Circular queue is full")
                continue

            enqueue_num = int(input("Input the number: "))
            # 배열을 넣어주고 rear을 1 증가시킨다다
            cirqueue[rear] = enqueue_num
            rear += 1

            # rear가 배열 크기를 넘어간다면, 나머지 연산을 통해 다시 첫 번째 원소를 (0번째) 가르키도록 설정한다.
            if rear >= len(cirqueue):
                rear %= len(cirqueue)

            print(f"Circular queue array is {cirqueue}")

        elif opt_num == 2:
            # 비었을 때의 가정
            if rear == front and None in cirqueue:
                print("Circualr queue is empty")
                continue
            
            # 배열이 안 비어있다면 가장 최근에 들어왔던 배열의 값을 None으로 바꾸고 +1 한다.
            cirqueue[front] = None
            front += 1

            # front의 값이 배열의 길이를 넘는다면, 1번째 원소를 가르키도록 바꿔준다.
            if front >= len(cirqueue):
                front %= len(cirqueue)

            print(f"Circular queue array is {cirqueue}")
        
        else: break
---
### main function
    if __name__ == '__main__':
        f_stack()
        f_queue()
        f_cirqueue()
