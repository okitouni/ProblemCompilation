# 1704. Determine if String Halves Are Alike
# You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

# Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

# Return true if a and b are alike. Otherwise, return false.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counter = 0
        for char in s[:len(s)//2]:
           if char.lower() in vowels:
               counter +=1

        for char in s[len(s)//2:]:
           if char.lower() in vowels:
               counter-=1
        
        return counter==0 

        