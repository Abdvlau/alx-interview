#!/usr/bin/env phyton
""" In a text file, there is initially a single character 'H'.
Your text editor supports only two operations on this file:
"Copy All" and "Paste". Given an integer n, write a function
to determine the minimum number of operations required
to achieve exactly n 'H' characters in the file.
"""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    in the file"""
    process = 2
    operation = 0
    while n > 1:
        while n % process == 0:
            operation += process
            n /= process
        process += 1
    return operation
