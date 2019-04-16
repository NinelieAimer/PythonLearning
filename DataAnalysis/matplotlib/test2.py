import numpy as np
from scipy.spatial.distance import pdist

array1=np.array([22,1,42,10])
array2=np.array([20,0,36,8])

#欧几里得距离
dist1 = np.linalg.norm(array2 - array1)
print(dist1)

#曼哈顿距离
dist2=np.sum(np.abs(array2-array1))
print(dist2)

# 闵氏距离
X=np.vstack([array1,array2])
dist3=pdist(X,'minkowski',3)
print(dist3)


Y=np.vstack([array1,array2])
dist3=pdist(Y,'minkowski',float('inf'))
print(dist3)