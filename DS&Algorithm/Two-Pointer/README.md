# Preview of twopointer.py
### Example of Two Pointer
    # 특정한 합을 지니는 부분 연속 수열 찾기
    def solution(arr, target):
        # 부분 연속 수열의 개수를 저장하는 변수
        count = 0
        # 부분 연속 수열의 합을 저장하는 변수
        sum = 0
        # 투 포인터 중 한 개를 맡음 (end)
        end = 0
        # 투 포인터 중 나머지를 맡음 (start)
        for start in arr:
            # 부분 연속 수열의 합이 부분합보다 작고 end가 가르키는 인덱스가 arr의 범위가 벗어나기 전까지 반복
            while sum < target and end < len(arr):
                # 위 조건을 만족하면 일단 부분 수열의 합을 계속해서 더해준다
                sum += arr[end]
                end += 1
            
            # 위 조건이 깨지는 경우는 두 가지 경우인데, sum이 target 보다 크거나 혹은 같거나이다. 만약 같을 경우에는 우리가 찾는 경우이므로 count에 1을 더해준다
            if sum == target:
                count += 1
    
            # 위 조건들을 다 지나고 나면, 무조건 sum에서 start는 +1의 위치로 움직이므로 전의 값을 빼줘야 한다!
            sum -= start
            
        return count
    
    if __name__ == '__main__':
        # 부분합을 5로 설정
        target = 5
        # arr 설정
        arr = [1, 2, 3, 2, 5]
        # 최종 부분수열의 개수를 출력
        print(solution(arr, target))
