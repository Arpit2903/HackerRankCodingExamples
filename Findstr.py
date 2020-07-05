#https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    mainstr = len(string)
    substr = len(sub_string)
    counter = 0
    for i in range(mainstr - substr + 1):
        if (string[i:(i + substr)] == sub_string):
            counter = counter + 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)