''' 
Note: this algorithm generates partitions of a group of n elements; however, it is
not useful for the tiling problem, as it is recursive, and reaches the stack limit before 
the permutation method gets impossibly slow.
'''

def getPartitions(n):
    ''' Algorithm H (Restricted growth strings in lexicographic order) from Knuth 4a, p.416'''
    
    # H1. Initialize.
    a = [0 for i in range(n)]
    b = [1 for i in range(n)]
    m = 1
    allParts = []
    
    return visitParts(allParts, a, b, m, n)

def visitParts(allParts, a, b, m, n):
    # H2. Visit.
    while a[n-1] != m+1:
        allParts.append([x for x in a])
        # H3. Increase a_n
        a[n-1] += 1
    return changeDigit(allParts, a, b, m, n)

def changeDigit(allParts, a, b, m, n):
    # H4. Find j.
    j = n-1
    while a[j-1] == b[j-1]:
        j -= 1

    # H5. Increase a_j
    if j == 1:
        return allParts
    a[j-1] += 1

    # H6. Zero out a_j+1 ... a_n
    m = b[j-1]
    if a[j-1] == b[j-1]:
        m += 1
    j += 1
    while j < n:
        a[j-1] = 0
        b[j-1] = m
        j += 1
    a[n-1] = 0

    return visitParts(allParts, a, b, m, n)
