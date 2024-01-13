import pdb


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        smallest = min(word1, word2, key=len)
        biggest = max(word1, word2, key=len)
        new_word = ""
        i = 0
        index_to_append = 0
        while len(new_word) < (len(word1) + len(word2)):
            # pdb.set_trace()
            if index_to_append < len(smallest):
                if i % 2 == 0:
                    new_word += word1[index_to_append]
                else:
                    new_word += word2[index_to_append]
                    index_to_append += 1
            else:
                new_word += biggest[index_to_append]
                index_to_append += 1
            i += 1

        return new_word


s = Solution()

test_cases = [["abc", "pqr"], ["ab", "pqrs"], ["abcd", "pq"]]

# print(s.mergeAlternately(*["abcd", "pq"]))

for tc in test_cases:
    print(f"test case = {tc}")
    print(s.mergeAlternately(*tc))
