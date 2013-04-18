#Both factoring functions give the factors of n in numerical order.
#The first prints them out, the second returns a list of factors.

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


def NewFactor(n):
#never have to check more than the square root of n                                                       
    MaxNum=n**.5 + 1
    i=2
    ListOfFactors=[]
    while i < MaxNum:
        #if n is divisible by i, update n and add i to the list
        # (this will not change the user's variable n)
        #Don't need to update i, since we still need to check if there are more
        #factors of i as well as all numbers greater than i
        if n%i == 0:
            ListOfFactors.append(i)
            n=n/i
            MaxNum=(MaxNum-1)/(i**.5)+1
        else:
            #increment i
            i=i+1
    #if we get here, n is prime
    ListOfFactors.append(n)
    return ListOfFactors

