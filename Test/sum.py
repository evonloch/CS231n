import numpy as np 



a = np.array([[ 1, 1, 1, 1, 1],
       [-23.,  21., -17., -11.,  -1.],
       [ -4.,  -5.,  16.,  -9., -14.],
       [-10.,  -6., -18.,  15.,  -8.],
       [-25.,  -2., -13.,  -7.,  24.]])


b = np.array([[ 1, 1, 1, 1, 1],
       [-23.,  21., -17., -11.,  -1.],
       [ -4.,  -5.,  16.,  -9., -14.]])



sqa = np.sum(b**2, axis = 1)
sqb = np.sum(a**2, axis = 1)

dist = sqa[:, np.newaxis] + sqb - 2 * np.dot(b, a.T)

dists = np.sqrt(dist)
print(dists)


print(a.sum(axis = 0))
print(a.sum(axis = 1))
a = a.sum(axis = 1)
print(a)