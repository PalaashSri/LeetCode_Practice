#Given an integer n, count the total number of digit 1 appearing in all non-negative
#integers less than or equal to n.

def countDigitOne(n):
    '''
    Naive Implementation
    :param n:
    :return:
    '''
    num_of_digit=0
    for i in range(n+1):
        while i>=10:
            val = i//10
            if val==1:
                num_of_digit+=1
            i = i%10

        if i==1:
            num_of_digit+=1

    return (num_of_digit)

print(countDigitOne(111111111))