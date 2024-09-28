from math import sqrt

def is_prime(n: int):
    f = 0
    for x in range(1, n+1, 1):
        if (n%x == 0):
            f += 1
            
    return True if f == 2 else False

def prime_factorization(n: int):
    """
    Returns two dimensional list containg all the prime factors of n, along with their exponents.
    
    Ex: if n=36, returns [[2, 2], [3,2]]
    
    """
    
    prime_factors = []
    
    k = 1
    while (k<sqrt(n)):
        if (n%k) == 0 and is_prime(k):
            i = 0
            for j in range(1, n+1, 1):
                if n%(k**j) == 0:
                    i += 1
                    
            prime_factors.append([k, i])
        k+=1
    return prime_factors

def count_divsors(n: int):
    """
    Returns the total number of divors for n
    """
    
    factors = prime_factorization(n)
    count = 1
    
    for i in factors:
        count *= i[1] + 1
        
    return count

def sum_of_divisors(n: int):
    """
    Returns the sum of all possible divisors of n
    """
    
    factors = prime_factorization(n)
    sum = 1
    
    for i in factors:
        p = i[0]
        a = i[1]
        
        sum *= (p**(a+1) - 1)/(p-1)
    
    return int(sum)

if __name__ == "__main__":
    print(is_prime(7))
    print(prime_factorization(100), count_divsors(100), sum_of_divisors(100))