
# https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    for word in s.split():
        s = s.replace(word,word.capitalize())
    return s
