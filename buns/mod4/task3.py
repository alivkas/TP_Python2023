def euclid_alg(a, b):
    if b == 0:
        return a
    else:
        return euclid_alg(b, a % b)
