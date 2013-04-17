def factor(n):
#max that we'd have to check (plus one)                                         
    maxNum=int(n**.5)+1
    for k in xrange(2,maxNum):
        if n%k==0:
            print k
            factor(n/k)
            return
#if n is prime, get here                                                        
    print n
