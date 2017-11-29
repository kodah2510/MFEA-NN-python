import numpy as np
def generateTestSet(N):
    dim = [int(2**N), int(N)]
    sample = np.random.rand(dim[0], dim[1])
    X = np.zeros(dim, dtype=float)
    Y = np.empty([1, dim[0]], dtype=bool)

    for i in range(0, len(X)):
        increment(X[i], i + 1)
        #print(X[i].astype(float))
    

    #print(X)
    sub_arrs = {}
    for i in range(0, N + 1):
        sub_arrs[i] = []
    for x in X:
        count = np.count_nonzero(x)
        sub_arrs[count].append(x)
    for i in sub_arrs:
        np.random.shuffle(sub_arrs[i])

    another_X = []
    for i in sub_arrs:
        for j in sub_arrs[i]:
            another_X.append(j)
    X = np.array(another_X)
    #print(X)
    #print(sub_arrs)
    
    #print(sub_arrs.astype(float))
    #np.random.shuffle(X)
    X = X.T
    for j in range(0, dim[0]):
        count = np.count_nonzero(X[::1, j])
        #print(count)
        if count % 2 == 0: 
            Y[0][j] = 0
        else:
            Y[0][j] = 1
    print('X')
    print(X.astype(float))
    print('Y')
    print(Y.astype(float))
    return X.astype(float), Y.astype(float)
    pass
def increment(X, times):
    cur_times = 0
    while cur_times != times:
        i = 0
        while i < len(X) and X[i] == 1:
            X[i] = 0
            i = i + 1
        if i < len(X):
            X[i] = 1
        cur_times += 1
    
def main():
    N = 4
    generateTestSet(N)
    pass
if __name__ == '__main__':
    main()