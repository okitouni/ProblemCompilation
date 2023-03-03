#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def strStr(haystack: str, needle: str) -> int:
        i = 0
        while i <= len(haystack) - len(needle):
            if haystack[i:].startswith(needle):
                return i
            i+=1
        return -1

if __name__ == "__main__":
    print(strStr("hello", "ll"))
    print(strStr("aaaaa", "bba"))
    print(strStr("aaaaa", "a"))
    print(strStr("aaaaab", "ab"))
