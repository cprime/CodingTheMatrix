# Please fill out this stencil and submit using the provided submission script.

from GF2 import one



## Problem 1
p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [v+u for u,v in zip(p1_u,p1_v)]
p1_v_minus_u = [v-u for u,v in zip(p1_u,p1_v)]
p1_three_v_minus_two_u = [(3*v)-(2*u) for u,v in zip(p1_u,p1_v)]



## Problem 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [v+u for u,v in zip(p2_u,p2_v)]
p2_v_minus_u = [v-u for u,v in zip(p2_u,p2_v)]
p2_two_v_minus_u = [(2*v)-(u) for u,v in zip(p2_u,p2_v)]
p2_v_plus_two_u = [(v)+(2*u) for u,v in zip(p2_u,p2_v)]



## Problem 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [v+u for u,v in zip([one, one, one],[0, one, one])]
p3_vector_sum_2 = [v+u+u for u,v in zip([one, one, one],[0, one, one])]



## Problem 4
# Please express your solution as a set of the letters corresponding to the solutions.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# Leave an empty set if it cannot be expressed in terms of the other vectors.
f_4 = {
'a':[one,one,0,0,0,0,0],
'b':[0,one,one,0,0,0,0],
'c':[0,0,one,one,0,0,0],
'd':[0,0,0,one,one,0,0],
'e':[0,0,0,0,one,one,0],
'f':[0,0,0,0,0,one,one],
}
u_0010010 = {'c','d','e'}
u_0100010 = {'b','c','d','e'}



## Problem 5
# Use the same format as the previous problem
#def add_them(keys,functions):
#    ret = [0,0,0,0,0,0,0]
#    for key in keys:
#        for i,v in enumerate(functions[key]):
#            ret[i] += v
#    return ret
#
#def find_it(functions):
#    fields = list(functions.keys())
#    fields += [None]
#    for i in fields:
#        for j in fields:
#            for k in fields:
#                for l in fields:
#                    for m in fields:
#                        for n in fields:
#                            go = set()
#                            go.update({i}) if i != None else None
#                            go.update({j}) if j != None else None
#                            go.update({k}) if k != None else None
#                            go.update({l}) if l != None else None
#                            go.update({m}) if m != None else None
#                            go.update({n}) if n != None else None
#                            if set() == go:
#                                continue
#                            sum = add_them(go,functions)
#                            if sum == [0,1,0,0,0,1,0]:
#                                print("===================================>",go)


f_5 = {
'a':[one,one,one,0,0,0,0],
'b':[0,one,one,one,0,0,0],
'c':[0,0,one,one,one,0,0],
'd':[0,0,0,one,one,one,0],
'e':[0,0,0,0,one,one,one],
'f':[0,0,0,0,0,one,one],
}
v_0010010 = {'c','d'}
v_0100010 = set()

#print(add_them({'b','c','d','e','f'}, f_5))


## Problem 6
uv_a = sum([v*u for u,v in zip([1,0],[5,4321])])
uv_b = sum([v*u for u,v in zip([0,1],[12345,6])])
uv_c = sum([v*u for u,v in zip([-1,3],[5,7])])
uv_d = sum([v*u for u,v in zip([-(2**.5/2),(2**.5/2)],[(2**.5/2),-(2**.5/2)])])



## Problem 7
# use 'one' instead of '1'
x_gf2 = [one,0,0,0]



## Problem 8
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]

