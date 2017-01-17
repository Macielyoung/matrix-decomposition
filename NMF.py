#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt

rate_matrix = np.array(
	[[5,5,3,0,5,5],
	 [5,0,4,0,4,4],
	 [0,3,0,5,4,5],
	 [5,4,3,3,5,5]]
)

nmf = NMF(n_components=2)
users = nmf.fit_transform(rate_matrix)
items = nmf.components_

print '用户主题分布：'
print users
print '物品主题分布：'
print items

plt.figure('fig1')
items = items.T
plt.plot(items[:,0],items[:,1],"b*")
plt.xlim((-1,3))
plt.ylim((-1,3))

plt.title(u'The distribution of items (NMF)')
count = 1
for item in items:
	plt.text(item[0],item[1],'item '+str(count),bbox=dict(facecolor='red',alpha=0.2),)
	count += 1

plt.figure('fig2')
user_names = ['Ben','Tom','John','Fred']
zip_data = zip(user_names,users)

plt.title(u'The distribution of users (NMF)')
plt.xlim((-1,3))
plt.ylim((-1,4))
for item in zip_data:
	user_name = item[0]
	data = item[1]
	plt.plot(data[0],data[1],"b*")
	plt.text(data[0],data[1],user_name,bbox=dict(facecolor='red',alpha=0.2),)

plt.show()
