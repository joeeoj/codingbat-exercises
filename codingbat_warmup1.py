# ------------------------------------
# Warm-up 1
# http://codingbat.com/python/Warmup-1
# ------------------------------------

# http://codingbat.com/prob/p162058
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return (a > 0 and b < 0) or (a < 0 and b > 0)

# http://codingbat.com/prob/p189441
def not_string(str):
    if str[0:3] == 'not':
        return str
    return 'not ' + str

# http://codingbat.com/prob/p197466
def diff21(n):
    diff = lambda a: abs(21 - a)
    if n > 21:
        return diff(n) * 2
    return diff(n)

# http://codingbat.com/prob/p141905
def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    return a + b

# http://codingbat.com/prob/p149524
def missing_char(str, n):
    return str[0:n] + str[n+1:]

# http://codingbat.com/prob/p166884
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    return False

# http://codingbat.com/prob/p173401
def sleep_in(weekday, vacation):
    return not weekday or vacation

# http://codingbat.com/prob/p147920
def front3(str):
    if len(str) > 2:
        return str[:3] * 3
    return str[:] * 3

# http://codingbat.com/prob/p120546
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

# http://codingbat.com/prob/p153599
def front_back(str):
    if len(str) > 1:
        return str[-1] + str[1:-1] + str[0]
    return str

# http://codingbat.com/prob/p124676
def near_hundred(n):
    near = lambda a: min(abs(200 - n), abs(100 - n))
    return near(n) <= 10 and near(n) >= 0

# alt for near_hundred
def near_hundred_alt(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)

# http://codingbat.com/prob/p124984
def makes10(a, b):
    if (a == 10 or b == 10) or (a+b == 10):
        return True
    return False
