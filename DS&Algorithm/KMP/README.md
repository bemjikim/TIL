# Preview of kmp.py

### 1. LPS (Longest Prefix Suffix)
    def cal_lps(str_arr, lps):
        # lps에 담을 값 (prefix, suffix의 각 길이 - 겹치는 길이가 얼마인지)
        leng = 0
        # str_arr의 1~len(str_arr)-1 까지 배열을 순회해 검사하기 위한 변수
        cmp_i = 1
        # 배열을 다 돌때 까지 반복!
        while cmp_i < len(str_arr):
            # 만약 cmp_i가 순회하다가 leng까지의 배열값을 비교해서 같다면! (같은 문자를 발견하면)
            if str_arr[cmp_i] == str_arr[leng]:
                # leng 값을 증가시키고 (기존 lps값에서 +1 시킴)
                leng += 1
                # 현재 배열을 도는 index까지의 lps값을 저장시킴
                lps[cmp_i] = leng
                # cmp_i의 값을 1 증가시켜 다음 배열을 준비한다.
                cmp_i += 1
    
            # 만약 str_arr[cmp_i] != str_arr[leng] 일 때!
            else:
                # leng이 0인지 아닌지 먼저 판별한다. (지금은 0이 아닐 때)
                if leng != 0:
                    # leng값을 lps에서 leng에 해당하는 -1 부분으로 초기화 한다!
                    # (앞 쪽에 있는 index에 접근하기 위함!)  
                    leng = lps[leng - 1]
                # leng 값이 0이라면 아무 것도 없는 상태이므로 그냥 lps[cmp_i] 값을 0으로 하고 cmp_i을 1 증가시킨다.
                else:
                    lps[cmp_i] = 0
                    cmp_i += 1
        
    if __name__ == "__main":
        str_arr = 'ABAAB'
        # lps 배열을 0으로 먼저 초기화
        lps = [0] * len(str_arr)
        cal_lps(str_arr, lps)
        print(lps)

---

### 2. KMP 알고리즘
    
    def kmp_search(str_arr, sub_arr):
        # 전체 str 길이와 부분 배열 길이를 각각 선언한다.
        m = len(str_arr)
        n = len(sub_arr)
        # lps는 부분 문자열에서 가져와야 하므로 n만큼의 길이로 설정한다
        lps = [0] * n
    
        # 계산해서 lps 배열 값을 넣어준다
        cal_lps(sub_arr, lps)
    
        # i는 str_arr를 위한 index, j는 sub_arr를 위한 index이다
        i = 0
        j = 0
    
        # i가 str_arr 길이를 벗어나버리면 의미가 없어짐 (전체 문자열에 대해 검사하므로)
        while i < m:
            # pattern을 찾으면 i, j에 각 1을 더하고 반복문 한 번 더
            if str_arr[i] == sub_arr[j]:
                i += 1
                j += 1
            
            # pattern을 찾지 못한다면
            elif str_arr[i] != sub_arr[j]:
                # j가 0이 아닌경우, 짧은 lps에 대해 재검사
                if j != 0:
                    # 겹치는 부분까지 이동후, 그 뒤 문자와 현재 i랑 다시 검사한다!
                    j = lps[j - 1]
                
                # j == 0인 경우에는 일치하는 부분이 없으므로 i를 증가시킨다. (sub_arr 처음부터 다시 쭉 비교!)
                else:
                    i += 1
    
            if j == n:
                print("Found pattern at index " + str(i - j + 1))
                # 이전 인덱스의 lps값을 참조하여 계속 검색한다. (또 다른 패턴이 있을 수 있으므로!)
                j = lps[j - 1]
        
    
    if __name__ == "__main__":
        str_arr = 'ABCDABCDABE'
        sub_arr = 'ABCDABE'
        kmp_search(str_arr, sub_arr)
        
