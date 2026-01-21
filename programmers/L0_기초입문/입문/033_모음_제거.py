# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 이호영
# 작성일: 2026. 01. 21. 09:17:55

def solution(my_string):
    qwer = ''
    answer = ["a", "e", "i", "o", "u"]
    for i in my_string :
        if i not in answer :
            qwer += i
    return qwer
        
    