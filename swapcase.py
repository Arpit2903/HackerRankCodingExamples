# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    res = s.swapcase() #swapcase() method converts all lowercase string to uppercase and vicecersa
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)