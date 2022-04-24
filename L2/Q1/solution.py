import numpy

def get_z(n, b):
    k = len(n)
    y = sorted(n)
    x = sorted(n, reverse=True)
    x = int(''.join(x), b)
    y = int(''.join(y), b)
    z = x - y
    z = numpy.base_repr(z, base=b)
    z = str(z)
    z = (k-len(z))*'0' + z
        
    return z


def solution(n, b):
    l = []
    while 1:
        z = get_z(n, b)
        if z not in l:
            l.append(z)
            n = z
        else:
            return len(l)-l.index(z)

# solution('210022', 3)
