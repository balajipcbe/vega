def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
        print(result)
    return result

print(parity(0xFF))
print(bin(0xFF))
