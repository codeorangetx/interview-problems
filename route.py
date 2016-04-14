'''
A company is considering installing new wireless routers in their complex. 
The plan is to install the n routers in a straight line along the main street that crosses the complex. 
The locations for the n routers and the distances of these locations from the start of the main street, 
are in feet and in increasing order, d1, d2, . . . , dn. The installation process should proceed under two constraints:
    At each location, the company can install at most one router. 
    The expected number of users for the router at location i is pi, where pi > 0 for i = 1,2,...,n.
    Any two routers should be at least m feet apart, where m is a positive integer.
Maximize the number of users
'''
from random import randint

n = 15
m = 8
D = [randint(1,100) for _ in xrange(n)]
D.sort()

P = [randint(1,100) for _ in xrange(n)]

print "m = {}".format(m)
print "D = {}".format(D)
print "P = {}".format(P)


def max_users_b(D,P,n,m):
    A = [0]*n # optimal set
    T = [0]*n # last index that's far enough from i

    if len(P) == 2:
        return sum(P) if D[1] - D[0] >= m else max(P)

    T[1] = 0
    A[0] = P[0]
    for i in range(1,n):
        if D[i] - D[i-1] >= m:
            T[i] = i - 1
        else:
            T[i] = T[i-1]

    for i in range(2,n):
        A[i] = max(P[i] + A[T[i]], A[i-1])

    print "T = {}".format(T)
    print "A = {}".format(A)
    return A[n-1]

print max_users_b(D,P,n,m)


