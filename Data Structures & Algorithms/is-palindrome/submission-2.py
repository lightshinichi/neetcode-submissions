class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []

        for c in s:
            if c.isalnum():
                arr.append(c.lower())

        ni = "".join(arr)

        return ni == ni[::-1]