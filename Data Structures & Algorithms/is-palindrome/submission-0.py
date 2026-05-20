class Solution:
    def isPalindrome(self, s: str) -> bool:
        ni= ""
        for i in s:
            if i.isalnum():
            # print(i)
                ni+=i.lower()
        if ni == ni[::-1]:
            return True
        return False