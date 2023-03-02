# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.
from typing import List


def compress(chars: List[str]) -> int:
        if len(chars) == 1: 
            print(chars)
            return 1
        counts = 1
        prev = chars[0]
        idx = 0
        for char in chars[1:]:
            if char == prev:
                counts += 1
            else:
                chars[idx] = prev
                idx += 1
                if counts > 1:
                    for digit in str(counts):
                        chars[idx] = digit
                        idx += 1
                prev = char
                counts = 1

        chars[idx] = char
        idx += 1
        if counts > 1:
            for digit in str(counts):
                chars[idx] = digit
                idx += 1
        print(chars[:idx])
        return idx 

if __name__ == "__main__":
    print(compress(["a","a","b","b","c","c","c"]))
    print(compress(["a"]))
    print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))