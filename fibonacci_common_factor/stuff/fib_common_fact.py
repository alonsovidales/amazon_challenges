#!/usr/bin/env python
# -*- coding: utf-8 -*- 

__author__ = "Alonso Vidales"
__email__ = "alonso.vidales@tras2.es"
__date__ = "2013-11-11"

class Fibonacci:
    def gcd_iter(self, u, v):
        while v:
            u, v = v, u % v
        return abs(u)

    def gcd(self, m, n):
        z = abs(m - n)
        if (m - n) == 0:
            return n
        else:
            return self.gcd(z, min(m, n))

    def smallest_common_fact(self, i, k):
        gcd = self.gcd_iter(i, k)
        if gcd == 1:
            return 1
        return i / gcd

    def resolve(self, num):
        """ Returns a string with the fibonnaci number and the common factor
        with the given one
        Uses a memory cache to store the last generated fibonaccy numbers in
        order to don't need to regenerate them for future calculations
        """

        # Check the numbers on the cache
        for fib_num in self.__cache[2:]:
            common_fact = self.smallest_common_fact(num, fib_num)
            if common_fact != 1:
                return "%d %d" % (fib_num, common_fact)

        # We don't have a number with a common factor in the cache of fibonacci
        # numbers, generate more fibonacci number and fill the cache
        prev = self.__cache[len(self.__cache) - 2]
        value = self.__cache[len(self.__cache) - 1]

        while True:
            prev_value = prev
            prev = value
            value += prev_value
            self.__cache.append(value)

            common_fact = self.smallest_common_fact(num, value)
            if common_fact != 1:
                return "%d %d" % (value, common_fact)

    def __init__(self):
        self.__cache = [1, 1]

if __name__ == "__main__":
    problems = int(raw_input())
    fib = Fibonacci()

    for problem in range(0, problems):
        print fib.resolve(int(raw_input()))
