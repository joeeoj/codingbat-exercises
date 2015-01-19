# ------------------------------------
# Warmup-2
# http://codingbat.com/python/Warmup-2
# ------------------------------------

# http://codingbat.com/prob/p165097
def front_times(str, n):
    if len(str) > 2:
        return str[:3] * n
    return str[:] * n

# http://codingbat.com/prob/p113152
def string_bits(str):
    return str[0::2]

# http://codingbat.com/prob/p193604
def array123(nums):
    return 1 in nums and 2 in nums and 3 in nums

# http://codingbat.com/prob/p182414
def string_match(a, b):
    match = 0
    for i in range(len(min(a, b, key=len)) - 1):
        if a[i] + a[i+1] == b[i] + b[i+1]:
            match +=1
    return match

# http://codingbat.com/prob/p145834
def last2(str):
    sub = str[-2:]
    count = 0
    for i in range(len(str) - 1):
        if str[i] + str[i+1] == sub:
            count += 1
    # subtract one if not zero
    return count - 1 if count else 0

# http://codingbat.com/prob/p110166
def array_front9(nums):
    return 9 in nums[0:4]
