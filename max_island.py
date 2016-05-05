# !/usr/bin/python


def findMaxIsland(A):
    maxIslandValue = 0
    B = A
    n = len(A)
    m = len(A[0])
    for i in xrange(n):
        for j in xrange(m):
            if B[i][j] != 0:
                islandValue = findIslandValue(B,i,j,n,m)
                print islandValue
                maxIslandValue = max(maxIslandValue, islandValue)
    return maxIslandValue

def findIslandValue(A,i,j,n,m):
    value = A[i][j]
    A[i][j] = 0

    if j-1 > 0 and A[i][j-1] != 0:
        value += findIslandValue(A,i,j-1,n,m)
    if j+1 < m and A[i][j+1] != 0:
        value += findIslandValue(A,i,j+1,n,m)
    if i-1 > 0 and A[i-1][j] != 0:
        value += findIslandValue(A,i-1,j,n,m)
    if i+1 < n and A[i+1][j] != 0:
        value += findIslandValue(A,i+1,j,n,m)

    return value

A = [[0,1,0,3,0],
     [0,0,3,0,0],
     [0,5,0,1,0],
     [0,5,0,1,0]]

print findMaxIsland(A)
