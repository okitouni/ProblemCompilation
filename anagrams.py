from collections import defaultdict

def are_anagrams(str1, str2):
    if len(str1) != len(str2): return False
    str1 = str1.lower()
    str2 = str2.lower()
    char_counts = defaultdict(int)
    for char in str1:
        char_counts[char] += 1
    for char in str2:
        char_counts[char] -= 1
        if char_counts[char] < 0:
            return False
    return True

str1 = "abc"
str2 = "caz"
print(str1, str2, are_anagrams(str1, str2))