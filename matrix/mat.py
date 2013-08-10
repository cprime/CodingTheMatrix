from vec import Vec

def getitem(M, k):
    "Returns the value of entry k in M.  The value of k should be a pair."
    assert k[0] in M.D[0] and k[1] in M.D[1]
    return M.f[k] if k in M.f else 0

def setitem(M, k, val):
    "Sets the element of v with label k to be val.  The value of k should be a pair"
    assert k[0] in M.D[0] and k[1] in M.D[1]
    M.f[k] = val

def add(A, B):
    "Returns the sum of A and B"
    assert A.D == B.D
    newF = {}
    for r in A.D[0]:
        for c in A.D[1]:
            value = (A.f[(r,c)] if (r,c) in A.f else 0) + (B.f[(r,c)] if (r,c) in B.f else 0)
            if value != 0:
                newF[(r,c)] = value
    return Mat(A.D,newF)

def scalar_mul(M, alpha):
    "Returns the product of scalar alpha with M" 
    newF = {}
    for r in M.D[0]:
        for c in M.D[1]:
            value = (M.f[(r,c)] if (r,c) in M.f else 0) * alpha
            if value != 0:
                newF[(r,c)] = value
    return Mat(M.D,newF)

def equal(A, B):
    "Returns true iff A is equal to B"
    assert A.D == B.D
    return {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]} == {row:Vec(B.D[1], {col:B[row,col] for col in B.D[1]}) for row in B.D[0]}

def transpose(M):
    "Returns the transpose of M"
    return Mat((M.D[1], M.D[0]), {(c,r):value for (r,c),value in M.f.items()})

def vector_matrix_mul(v, M):
    "Returns the product of vector v and matrix M"
    assert M.D[0] == v.D
    columnDict = {col:Vec(M.D[0], {row:M[row,col] for row in M.D[0]}) for col in M.D[1]}
    return Vec(M.D[1], {key:value*v for key,value in columnDict.items()})

def matrix_vector_mul(M, v):
    "Returns the product of matrix M and vector v"
    assert M.D[1] == v.D
    rowDict = {row:Vec(M.D[1], {col:M[row,col] for col in M.D[1]}) for row in M.D[0]}
    return Vec(M.D[0], {key:value*v for key,value in rowDict.items()})

def matrix_matrix_mul(A, B):
    "Returns the product of A and B"
    assert A.D[1] == B.D[0]
    aRowDict = {row:Vec(A.D[1], {col:A[row,col] for col in A.D[1]}) for row in A.D[0]}
    bColDict = {col:Vec(B.D[0], {row:B[row,col] for row in B.D[0]}) for col in B.D[1]}
    return Mat((A.D[0],B.D[1]), {(r,c):row*column for r,row in aRowDict.items() for c,column in bColDict.items()})

################################################################################

class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    __getitem__ = getitem
    __setitem__ = setitem
    transpose = transpose

    def __neg__(self):
        return (-1)*self

    def __mul__(self,other):
        if Mat == type(other):
            return matrix_matrix_mul(self,other)
        elif Vec == type(other):
            return matrix_vector_mul(self,other)
        else:
            return scalar_mul(self,other)
            #this will only be used if other is scalar (or not-supported). mat and vec both have __mul__ implemented

    def __rmul__(self, other):
        if Vec == type(other):
            return vector_matrix_mul(other, self)
        else:  # Assume scalar
            return scalar_mul(self, other)

    __add__ = add

    def __sub__(a,b):
        return a+(-b)

    __eq__ = equal

    def copy(self):
        return Mat(self.D, self.f.copy())

    def __str__(M, rows=None, cols=None):
        "string representation for print()"
        if rows == None:
            try:
                rows = sorted(M.D[0])
            except TypeError:
                rows = sorted(M.D[0], key=hash)
        if cols == None:
            try:
                cols = sorted(M.D[1])
            except TypeError:
                cols = sorted(M.D[1], key=hash)
        separator = ' | '
        numdec = 3
        pre = 1+max([len(str(r)) for r in rows])
        colw = {col:(1+max([len(str(col))] + [len('{0:.{1}G}'.format(M[row,col],numdec)) if isinstance(M[row,col], int) or isinstance(M[row,col], float) else len(str(M[row,col])) for row in rows])) for col in cols}
        s1 = ' '*(1+ pre + len(separator))
        s2 = ''.join(['{0:>{1}}'.format(c,colw[c]) for c in cols])
        s3 = ' '*(pre+len(separator)) + '-'*(sum(list(colw.values())) + 1)
        s4 = ''.join(['{0:>{1}} {2}'.format(r, pre,separator)+''.join(['{0:>{1}.{2}G}'.format(M[r,c],colw[c],numdec) if isinstance(M[r,c], int) or isinstance(M[r,c], float) else '{0:>{1}}'.format(M[r,c], colw[c]) for c in cols])+'\n' for r in rows])
        return '\n' + s1 + s2 + '\n' + s3 + '\n' + s4

    def pp(self, rows, cols):
        print(self.__str__(rows, cols))

    def __repr__(self):
        "evaluatable representation"
        return "Mat(" + str(self.D) +", " + str(self.f) + ")"
