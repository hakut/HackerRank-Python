def divisibleSumPairs(n, k, ar):
    counter = 0
    for i in ar:
        for j in ar:
            if i<j and k%(i+j) == 0:
                counter += 1
    return counter


if __name__ == '__main__':
    n,k = 6,3
    ar = [1,3,2,6,1,2]
    result = divisibleSumPairs(n,k,ar)
    print (result)