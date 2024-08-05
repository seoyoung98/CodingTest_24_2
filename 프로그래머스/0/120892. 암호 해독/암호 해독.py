def solution(cipher, code):
    answer = ''
    idx = 0
    for i in range(len(cipher)):
        idx += 1
        if idx == code:
            answer += cipher[i]
            idx = 0
    return answer