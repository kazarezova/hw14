import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
df = df.loc[:,['ESR1','PGR','ERBB2','MKI67','Subtype']]

sns.boxplot(data=df.loc[df['Subtype']=='Healthy']) # or 'Normal-like' or other subtypes
plt.savefig("BRCA_pam50_Healthy.pdf")
plt.close()

'''
(Q25-Q75, approximately)

Healthy:
ESR1 - 2.5-4
PGR - 1.5-3
ERBB2 - 4-5
MKI67 - 0.5-1

Normal-like:
ESR1 - 2-4
PGR - 1-3
ERBB2 - 4-5
MKI67 - 1.5-3

Triple-negative:
ESR1 - <1
PGR - ~0
ERBB2 - ~4
MKI67 - 3.5-5

Luminal A:
ESR1 - 4.5-6.5
PGR - 1.5-4.5
ERBB2 - 5-6
MKI67 - 2-3

Luminal B:
ESR1 - 5-6.5
PGR - 0.5-3.5
ERBB2 - 4.5-6
MKI67 - 3-4

HER2-enriched:
ESR1 - 0.5-2.5
PGR - ~0
ERBB2 - 6-9
MKI67 - ~4
'''
