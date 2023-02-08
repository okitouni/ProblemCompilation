def sum_(a, b):
    # 101 = 5
    # 111 = 7
    # 1100= 12
    # 010 ^
    # 101<<1 = 1010 + 0010 
    # sum ^ = 010
    # remainder & = 1010
    # sum ^ = 1000
    # remainder &<1 = 0100
    # sum ^ = 1100
    # remainder 00000
    if b == 0:
        return a
    return sum_(a^b, (a&b)<<1)

print(sum_(12, 2))