
def generate_matrix(x, y, f):
    m = []
    for iy in range(y):
        l = []
        for ix in range(x):
            l.append(f)
        m.append(l)
    return m

def add(v1, v2):
    v = []
    for x, y in zip(v1, v2):
        v.append(x+y)
    return v

def dot(v1, v2):
    d = 0
    for x, y in zip(v1, v2):
        d += x*y
    return d

def m_v_mult(m, v):
    nv = []
    for r in m:
        nv.append(dot(r, v))
    return nv

def el_func(v, func):
    nv = []
    for i in v:
        nv.append(func(i))
    return nv