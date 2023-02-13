# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
def count_odds(low: int, high: int) -> int:
    return (high // 2 + high % 2) - low // 2


print(count_odds(0, 10))
