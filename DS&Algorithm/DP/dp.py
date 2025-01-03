# 피보나치 수열로 전체의 예시를 듦

# Bottom-up (Tabulation방식 - 반복문)
def dp_bottom_up():
    n = 4
    bottoup_table = [None] * (n+1)
    # 기저 상태 (inital state)를 먼저 저장
    bottoup_table[0], bottoup_table[1] = 0, 1

    # 반복문 사용
    for i in range(2, n+1):
        bottoup_table[i] = bottoup_table[i-1] + bottoup_table[i-2]

    print(bottoup_table[n])

# Top-down (Memoziation방식 - 재귀)
n = 30
memoziation = [0] * (n+1)
def dp_top_down(n):
    # 기저상태 도달시 0, 1로 초기화
    if n < 2:
        memoziation[n] = n
        return memoziation[n]
    
    elif memoziation[n] > 0:
        return memoziation[n]
    
    memoziation[n] = dp_top_down(n-1) + dp_top_down(n-2)

    return memoziation[n]

if __name__ == '__main__':
   
    dp_bottom_up()
    #print(dp_top_down(n))