"""
Write a function to check if a given string is a palindrome. 
Use 2 methods. One is using slicing and other using loops. 
Both should be written. So basically make 2 functions for each
"""


def isPalindrome1(s: str) -> bool:
    return s == s[::-1]


def isPalindrome2(s: str) -> bool:
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


string = "mom"
print(isPalindrome1(string))
print(isPalindrome2(string))
