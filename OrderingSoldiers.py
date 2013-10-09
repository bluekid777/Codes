def c(li):
    co = 0
    for i in li:
        co = co+1
    return co

def get_input():    
    x = []
    y = []
    n = int(raw_input())
    while n > 0:
        x.append(int(raw_input()))
        y.append(n)
        n = n-1
    y.reverse()
    return x,y

def evaluate(x,y):
    for i in range(0,c(x)):
        t = x[i]
        ind = 1
        while t > 0:
            y[i - ind] = y[i - ind] + 1
            t = t-1
            ind = ind + 1
        y[i] = y[i] - x[i]
    return y

def display(y):
    for i in y:
        print i

test_case = int(raw_input())

for i in range(0,test_case):
    x,y = get_input()
    y = evaluate(x,y)
    display(y)

