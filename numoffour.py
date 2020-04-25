#code to find number of 4's in a number
#code 1
numbers = list()
try :
    T = input()
    t = int(T)
except :
    quit()

while t > 0 :
    num = input()
    n = int(num)
    l = len(num)
    while l > 0 :
        r = n % 10
        n = int(n/10)
        numbers.append(r)
        l = l-1
    print(numbers.count(4))
    t = t-1
        
#code 2 

try :
    T = input()
    t = int(T)
except :
    quit()

while t > 0 :
    N = input()
    c=0
    for i in range(len(N)):
        if int(N[i]) == 4:
            c+=1
    t = t-1
    print(c)
