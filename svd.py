#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.sparse.linalg import svds
from scipy import sparse
import matplotlib.pyplot as plt

def vector_to_diagonal(vector):
	"""
	将向量放在对角矩阵的对角线上
	"""
	if(isinstance(vector, np.ndarray) and vector.ndim == 1) or isinstance(vector, list):
		length = len(vector)
		diag_matrix = np.zeros((length, length))
		np.fill_diagonal(diag_matrix, vector)
		return diag_matrix
	return None

rate_matrix = np.array(
	[[5,5,3,0,5,5],
	 [5,0,4,0,4,4],
	 [0,3,0,5,4,5],
	 [5,4,3,3,5,5]]
)

rate_matrix = rate_matrix.astype('float')
U, S, VT = svds(sparse.csr_matrix(rate_matrix), k=2, maxiter=200)
S = vector_to_diagonal(S)
print '用户主题分布：'
print U
print '物品主题分布：'
print VT
print '奇异值：'
print S
print '重建评分矩阵，并过滤已经评分物品：'
print np.dot(np.dot(U, S), VT) * (rate_matrix < 1e-6)

user_names = ['Ben','Tom','John','Fred']
zip_data = zip(user_names, U)
VT = VT.T

plt.plot(VT[:,0],VT[:,1],"r*")
plt.title(u'The distribution of users and items (SVD)')
plt.xlim((-1,1.5))
plt.ylim((0,0.8))
count = 1
for item in VT:
	plt.text(item[0],item[1],'item '+str(count),bbox=dict(facecolor='yellow',alpha=0.2),)
	count += 1

for item in zip_data:
	user_name = item[0]
	data = item[1]
	plt.plot(data[0],data[1],"r.")
	plt.text(data[0],data[1],user_name,bbox=dict(facecolor='green',alpha=0.2),)

plt.show()
