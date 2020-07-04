#https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(s):
    # your code goes here
    kevin = 0
    stuart = 0
    for i in range(len(s)):
        if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
            kevin = kevin + len(s) - i # vowels added in kevin's score and removed the position of the vowel which was founded.
        else:
            stuart = stuart + len(s) - i
    if(kevin == stuart):
        print("Drawed")
    elif kevin > stuart:
        print("Kevin "+str(kevin))
    else:
        print("Stuart "+str(stuart))

if __name__ == '__main__':
    s = input()
    minion_game(s)