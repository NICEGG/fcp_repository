import numpy as np           # numpyの別名はnpが慣習
A = np.array([[1,2],[3,4]])  # 行列Aの定義
B = np.array([[5,6],[7,8]])  # 行列Bの定義
print('行列の和')
print(A+B)
print('行列の積') 
print(np.dot(A,B))