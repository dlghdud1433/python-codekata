# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 이호영
# 작성일: 2026. 01. 17. 12:19:07

def solution(slice, n):
    answer = 0
    a = n // slice
    b = n % slice
    if b == 0 :
        return a
    else :
        return a + 1
   