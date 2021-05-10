import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
df = df.loc[:,['ESR1','PGR','ERBB2','MKI67','Subtype']]

sns.boxplot(data=df.loc[df['Subtype']=='Healthy']) # or 'Normal-like' or other subtypes
plt.savefig("BRCA_pam50_Healthy.pdf")
plt.close()
