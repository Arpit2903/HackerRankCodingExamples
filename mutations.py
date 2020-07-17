# https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string  # Converting the string into list and then adding the values.

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print (s_new)