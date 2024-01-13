class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        smallest = min(str1, str2, key=len)
        biggest = str1 if str1 != smallest else str2
        divisor = ""
        for i in range((len(smallest)), -1, -1):
            prefix = smallest[0:i]
            test = biggest[0:i]
            # __import__("pdb").set_trace()
            if prefix == test and len(prefix) != 0:
                if (len(str1) % len(prefix) == 0) and (len(str2) % len(prefix) == 0):
                    if self.count(str1, prefix) * len(prefix) == len(
                        str1
                    ) and self.count(str2, prefix) * len(prefix) == len(str2):
                        divisor = prefix
                        break

        return divisor

    def count(self, string: str, prefix: str) -> int:
        c = 0
        for i in range(len(prefix), len(string) + 1, len(prefix)):
            start = i - len(prefix)
            pt = string[start:i]
            if pt == prefix:
                c += 1

        return c


s = Solution()

print(s.gcdOfStrings("ABCABC", "ABC"))
print(s.gcdOfStrings("ABABAB", "ABAB"))
print(s.gcdOfStrings("ABCDEF", "ABC"))
print(s.gcdOfStrings("LEET", "CODE"))
