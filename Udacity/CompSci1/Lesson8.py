def s_union(a, b):
    return list(set(a) | set(b))

def union(a, b):
    res = s_union(a, b)
    for e in res:
        if e not in a:
            a.append(e)