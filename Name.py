#https://www.hackerrank.com/challenges/whats-your-name/problem
def print_full_name(a,b):
    print("Hello" +a+" "+b+"! You just delved into python" )

if __name__ == '__main__':
    fname = input("enter first name")
    lname = input("enter last name")
    print_full_name(fname,lname)