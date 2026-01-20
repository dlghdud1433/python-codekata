# 아이스 아메리카노
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 알고리즘: 기초
# 작성자: 이호영
# 작성일: 2026. 01. 20. 15:19:50

def solution(money):
    answer = []
    c = money // 5500
    r = money % 5500
    return c, r