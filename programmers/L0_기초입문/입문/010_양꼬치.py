# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 이호영
# 작성일: 2026. 01. 16. 20:33:04


2
3
4
def solution(n, k):
    answer = 12000*n + 2000*k - 2000*(n//10)
    return answer