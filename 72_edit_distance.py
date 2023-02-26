# 72. edit distance 
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character

# abcd
# abc

# def edit_distance(word1: str, word2: str) -> int:
#     dp = [[0] * len(word1) for _ in range(len(word2))]
#     i, j = 0, 0
#     while i < len(word1) or j < len(word2):
#         if i == len(word1) or j == len(word2):
#             dp[-1][-1] = abs(i-j)
#             break
#         if word1[i] == word2[j]:
#             dp[i][j] = dp[i-1][j-1]
#             i += 1
#             j += 1
#         else:
#             dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#     return dp[-1][-1]
from functools import cache

@cache
def edit_distance(word1: str, word2: str) -> int:
    if not word2 or not word1:
        return max(len(word1), len(word2))
    if word1[-1] == word2[-1]:
        return edit_distance(word1[:-1], word2[:-1])
    else:
        return min(edit_distance(word1[:-1], word2),
                  edit_distance(word1, word2[:-1]), 
                  edit_distance(word1[:-1], word2[:-1])
        ) + 1
    


print(edit_distance("abc", "abcd"))
