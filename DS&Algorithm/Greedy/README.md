# Preview of greedy.py

### Greedy에 대한 예제 문제 2개

### 1. 회의실 문제
    # 문제
    # 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
    
    # 입력
    # 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.
    
    # 출력
    # 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
    
    def solution(meet_list):
        select_r = 0
        # meet_list에 맨 처음 있는 것이 끝나는 시간이 제일 빠른 것이므로 최종 result에 먼저 넣어준다.    
        result = [select_r + 1]
        # 첫 번째 이후의 회의실을 돌면서 최근에 선택된 미팅 룸의 끝나는 시간과 그 이후의 시작 시간을 비교한다.
        for i in range(1, len(meet_list)):
            if meet_list[select_r][1] <= meet_list[i][0]:
                select_r = i
                # +1해주는 이유는 index는 0번째 부터이므로.. 우리는 몇 번째 (1번째 ~ n 번째 를 보고 싶음)
                result.append(i + 1)
        # 최대 개수의 회의실을 사용하는데 몇 번째 회의실들이 포함되는지 보여줌
        # print(result)
        return len(result)
    
    if __name__ == "__main__":
        num = int(input())
        meet_r = []
        for _ in range(num):
            # 시작, 끝 시간을 입력하여 list에 입력해준다
            s, f = map(int, input().split())
            meet_r.append([s, f])
    # 끝나는 시간 기준으로 오름차순으로 정렬해준다.
    meet_r.sort(key = lambda x: [x[1], x[0]])
    print(solution(meet_r))

---

### 2. 거스름돈 내기

    def solution(money):
        # 거스름돈
        coin = [500, 100, 50, 10, 5, 1]
        # 최소로 줄 수 있는 거스름돈의 총 개수
        count = 0
    
        # 거스름돈에서 가장 큰 수부터 나눠서 준다.
        for i in coin:
            count += money // i
            # 쓴 동전 만큼 돈에서 빼준다
            money %= i
        
        return count
    
    
    if __name__ == "__main__":
        money = 1000 - int(input())
        print(solution(money))
    
    
