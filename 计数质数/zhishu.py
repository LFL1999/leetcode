class Solution:
    def countPrimes(self, n):
        def isPrime(x):
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1
            return True

        count = 0
        for j in range(n-1):
            if isPrime(j+2):
                count += 1
        return count
