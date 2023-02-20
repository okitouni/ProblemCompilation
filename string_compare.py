from timeit import timeit


def is_prefix(pref: str, s: str) -> bool:
    """Checks whether pref is prefix of s using string compare.

    Args:
        pref (str): String prefix.
        s (str): String to check

    Returns:
        bool: Whether pref is a prefix of s.
    """
    if pref == s[: len(pref)]:
        return True
    return False


def is_prefix2(pref: str, s: str) -> bool:
    """Checks whether pref is prefix of s. Using for loop

    Args:
        pref (str): String prefix.
        s (str): String to check

    Returns:
        bool: Whether pref is a prefix of s.
    """
    for i in range(len(pref)):
        if pref[i] != s[i]:
            return False
    return True


n = 10000
pref = "i" * n
s = "i" * (n + 1)

string_time = timeit("is_prefix(pref,s)", number=100, globals=globals())
loop_time = timeit("is_prefix2(pref,s)", number=100, globals=globals())

print(f"string compare time {string_time}")
print(f"for loop time {loop_time}")
