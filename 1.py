from scipy.stats import pearsonr, spearmanr
import seaborn as sns
import numpy as np

l1=[]
l2=[]
for i in range(100):
    l1.append(i)
    l2.append(np.exp(i))

print('pearson: ',pearsonr(l1, l2)[0])
print('spearman: ',spearmanr(l1, l2)[0])
sns.scatterplot(x=l1,y=l2)

'''
pearson:  0.2520320339038703
spearman:  0.9999999999999999
'''
