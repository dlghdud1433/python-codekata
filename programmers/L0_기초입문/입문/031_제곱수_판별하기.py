# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 이호영
# 작성일: 2026. 01. 21. 08:28:04

def solution(n):
    answer = 0
    for i in range(1, n) :
        if n == i * i :
            return 1
    return 2
        