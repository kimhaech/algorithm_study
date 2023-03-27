def solution(s):
    answer = True
    sum = 0
    
    if s[0] == ')' or s[-1] == '(': # 각 끝에서 false 체크 
        return False
    else: # 그 외 경우
        for i in range(len(s)):
            if s[i] == '(': # 열린 괄호는 +1
                sum += 1
            else:
                if sum <= 0: # 열린 괄호가 모두 닫힌 상태에서 닫힌 괄호가 나온 경우
                    return False
                else: # 닫힌 괄호는 -1
                    sum -= 1
    if sum == 0:
        return True
    else:
        return False
