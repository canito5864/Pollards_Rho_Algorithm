import random
from math import gcd

def pow_dnc(a, n, MOD): #나머지, 모듈러 지수 연산
    if n == 0:
        return 1 % MOD
    u = pow_dnc(a, n // 2, MOD)
    u = (u * u) % MOD
    if n % 2 == 1:
        u = (u * a) % MOD
    return u

def miller_rabin(n, a): #소수 판별, 사이클 구하기
    if a % n == 0:
        return False
    k = n - 1
    while True:
        t = pow_dnc(a % n, k, n)
        if t == n - 1:
            return True
        if k % 2:
            return t == 1 or t == n - 1
        k //= 2

def is_prime(n): #n이 소수인 경우
    a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(len(a)):
        if n == a[i]:
            return True
        if not miller_rabin(n, a[i]):
            return False
    return True

def pollard_rho(n): #폴라드 로 알고리즘
    if is_prime(n): #소수인 경우 n
        return n
    if n == 1: #1인 경우
        return 1
    if n % 2 == 0: #짝수인 경우
        return 2

    x = y = random.randint(2, n - 2)
    c = random.randint(1, 20)
    d = 1

    while d == 1:
        x = ((x * x) % n + c) % n
        y = ((y * y) % n + c) % n
        y = ((y * y) % n + c) % n
        d = gcd(max(x, y) - min(x, y), n) #d가 1과 n사이일 경우 n의 약수

        if d == n: #다시 약수 찾기
            return pollard_rho(n)
    return pollard_rho(d)

def main(x): #입력값 받아 폴라드 로 알고리즘 반복
    res = []

    if x==1: #1인 경우
        print(1)

    # Factorize 'x' using Pollard's Rho algorithm
    while x > 1: #완전 인수분해가 될 때까지 반복
        dv = pollard_rho(x)
        res.append(dv)
        x //= dv

    # Sort and print the prime factors
    res.sort()
    for i in res:
        if i == res[-1]:
            print(i)
        else: print(i,end='*')

x= int(input('number for calculating its prime'))
main(x)
