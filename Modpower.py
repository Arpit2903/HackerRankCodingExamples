# https://www.hackerrank.com/challenges/python-power-mod-power/problem
import math
a = int(input())
b = int(input())
m = int(input())
print(a**b)
print(pow(a,b,m)) # pow(a,b,m) results in (a ** b) % m
