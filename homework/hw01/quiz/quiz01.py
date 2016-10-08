def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    for i in range(a,a*b+1):
        if i%a==0 and i%b==0:
            return i

            
                
def has_digit(n,k):
    while n!=0:
        if n%10 == k:
            return True
        n = n//10
    return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    """loop the digit from 0 to 9,count how many times True return in total"""
    count = 0
    for i in range(0,10):
        if has_digit(n,i):
            count +=1
    return count
