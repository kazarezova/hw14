from scipy.stats import pearsonr, spearmanr
import math
import numpy as np

l1=[]
l2=[]
for i in range(20):
    l1.append((-1)*i)
    l2.append(i)
for i in range(20,100):
    l1.append((-1)*i+1000)
    l2.append(i+1000)

print('pearson: ',pearsonr(l1, l2)[0])
print('spearman: ',spearmanr(l1, l2)[0])
sns.scatterplot(x=l1,y=l2)

'''
pearson:  0.9945720403136884
spearman:  -0.0399039903990399
'''
