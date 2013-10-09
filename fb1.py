def get_input(N):
    master = []
    while(N > 0):
        n = int(raw_input())
        l = []
        while(n > 0):
            temp = int(raw_input())
            l.append(temp)
            n = n-1
        master.append(l)
        N = N-1
    return master

def count(T):
    c = 0
    for i in T:
        c = c+1
    return c

def create_list(M):
    X = []
    for li in M:
        for element in li:
            X.append(element)
    X.sort()
    return X

def find_set(M,x):
    for l in M:
        if l.count(x) > 0:
            return l
    return -1

def in_same_set(M,x,y):
    s = find_set(M,x)
    if s.count(y) > 0:
        return True
    else:
        return False

def process_list(M,N,K):
    Master = create_list(M)
    min_index = 0
    for i in Master:
        if(min_index == K-1):
            break
        if not in_same_set(M,i,Master[Master.index(i) + 1]):
            min_index = min_index + 1       
    mini = i
    print mini
    min_index = 0
    Master.reverse()
    for j in Master:
        if(min_index == N-K):
            break
        if not in_same_set(M,j,Master[Master.index(j) + 1]):
            min_index = min_index + 1
    maxi = j
    print maxi
    c = abs(Master.index(mini) - Master.index(maxi)) + 1
    return c

test_cases = int(raw_input())
while test_cases > 0:
    N = int(raw_input())
    K = int(raw_input())
    if N >= K:
        master = get_input(N)
        print master
        print process_list(master,N,K)
    test_cases = test_cases - 1 

