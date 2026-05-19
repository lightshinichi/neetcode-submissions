class Solution:

    def encode(self, strs: List[str]) -> str:
        op =""
        for i in strs:
             op +=  i+"~"
        return op

    def decode(self, s: str) -> List[str]:
        ls = []
        ot = ""
        for i in s:
            if i == "~":
                ls.append(ot)
                ot= ''
            else:
                ot +=i
        return ls
