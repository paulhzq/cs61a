from lab03 import *

def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y*10+x%10
    while x > 0:
        x, y = x//10, f()
    return y == n

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n ==1:
        return 1
    else:
        return n * skip_mul(n - 2)

def count_up(n):
    """Print out all numbers up to and including n in ascending order.

    >>> count_up(5)
    1
    2
    3
    4
    5
    """
    def counter(i):
        "*** YOUR CODE HERE ***"
        while i<n:
            print(i)
            counter(i+1)
    counter(1)

def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    if a==0 or b==0:
        return c
    elif a==1:
        return b+c
    else:
        return b+ab_plus_c(a-1,b,c)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def help(i):
        while i<n:
            if n%i ==0:
                return False
            else:
                return help(i+1)
        return True
    return help(2)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    "*** YOUR CODE HERE ***"
    def interleaved_helper(n, term0, term1, k):
        if k == n:
            return term0(k)
        return term0(k) + interleaved_helper(n, term1, term0, k+1)
    return interleaved_helper(n, odd_term, even_term, 1)

    

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def count_digit(n, digit):
        """Return how many times digit appears in n.

        >>> count_digit(55055, 5)
        4
        """
        if n == 0:
            return 0
        else:
            if n%10 == digit:
                return count_digit(n//10, digit) + 1
            else:
                return count_digit(n//10, digit)

    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count_digit(n//10, 10 - n%10)

