import numpy as np
array1=np.array([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
array2=np.array([0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0])
array3=np.array([0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0])
array4=np.array([0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1])

#构造两个循环分别输出
array_first=[array2,array3,array4]
array_second=[array3,array4]

#输出array1和其他三个的余弦
for array in array_first:
    cos = np.dot(array1, array) / (np.linalg.norm(array1) * (np.linalg.norm(array)))
    print(cos)

#输出array2和其他两个余弦
for arraytest in array_second:
    cos2=np.dot(array2, arraytest) / (np.linalg.norm(array2) * (np.linalg.norm(arraytest)))
    print(cos2)

#输出array3和最后一个余弦
cos3=np.dot(array3, array4) / (np.linalg.norm(array3) * (np.linalg.norm(array4)))
print(cos3)