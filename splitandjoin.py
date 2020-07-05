#https://www.hackerrank.com/challenges/python-string-split-and-join/problem
def split_and_join(line):
    # write your code here
    sp = line.split() # split() returns a list of seperated string
    con = "-".join(sp) #join() merges the string with original string
    return con

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)