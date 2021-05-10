import pandas as pd
import seaborn as sns
from sklearn.manifold import TSNE

df = pd.read_csv("human_coronavirus_aln_scores.tsv", sep="\t", index_col=0)
df=1/(df/5000)-1

model = TSNE(perplexity=15,metric='precomputed')
df=model.fit_transform(df)
df=pd.DataFrame(df,columns=['TSNE1','TSNE2'])
df['virus type']=['HCoV-HKU1']*20+['MERS-CoV']*20+['SARS-CoV-2']*20+['HCoV-229E']*20+['HCoV-NL63']*20+['HCoV-OC43']*20+['SARS-CoV']*20

sns.scatterplot(data=df,x='TSNE1',y='TSNE2',hue='virus type')
plt.savefig("TSNE_CoV.pdf")
plt.close()
