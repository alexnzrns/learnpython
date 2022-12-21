def s2hms(s):
    h = s // 3600
    m = (s//60) % 60
    s = s%60
    return h,m,s

def lt(mylist):
    first = tuple
    second = tuple
    first = mylist[0]
    second = mylist[-1]
    return first, second