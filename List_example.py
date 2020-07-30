if __name__ =='__main__':
    N=int(input())
    empty_list = []
    for x in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'append':
            empty_list.append(int(x[1]))
        if command == 'print':
            print(empty_list)
        if command == 'insert':
            empty_list.insert(int(x[1]),int(x[2]))
        if command == 'reverse':
            empty_list = empty_list[::-1]
        if command == 'pop':
            empty_list.pop()
        if command == 'sort':
            empty_list.sort()
        if command == 'remove':
            empty_list.remove(int(x[1]))