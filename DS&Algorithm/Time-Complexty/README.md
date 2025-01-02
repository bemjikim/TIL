# Preview of time-complexity.py 

  ### 1. $O(1)$ 예시, 배열을 받아 첫 번째 index가 0인지 아닌지 판별하는 함수
    def t_o1(arr):
        if arr[0] == 0:
            return 0 
        else:
            return -1
  ---
  ### 2. $O(n)$ 예시, 배열을 받아 모든 index를 출력하는 함수  
    def t_on(arr):
        for i in (arr):
            print('elements in arr: ', i)
  ---    
  ### 3. $O(logn)$ 예시, binary search를 하는 함수
    def t_ologn(arr, key):
        start = 0
        end = len(arr)-1
  
      while start <= end:
          m = (start + end) / 2
  
          if m == key:
              print('Find it!')
              return
          
          elif m < key:
              start = m + 1
          
          else:
              end = m - 1
  ---
  ### 4. $O(n^2)$ 예시, 2차원 배열을 받아 모든 index를 출력하는 함수
      def t_on2(arr):
          for i in arr:
              for j in i:
                  print(j)
---
  ### 5. $O(2^n)$ 예시, 피보나치 수열을 출력하는 함수
    def t_2n(fibo_num):
        if fibo_num == 0:
            return 0
      
      elif fibo_num == 1:
          return 1
      
      else:
          return t_2n(fibo_num-1) + t_2n(fibo_num-2)
