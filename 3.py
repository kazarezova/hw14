import pandas as pd
from scipy.stats import pearsonr, spearmanr

df = pd.read_csv("healthy_breast.tsv", sep="\t", index_col=0)
df = df.T
coexp={}
for i in df.columns:
    sr=spearmanr(df['SPI1'],df[i])[0]
    if sr>=0.8:
        coexp[i]=sr
    
print('с транскрипционным фактором SPI1 в клетках молочной железы коэспрессированы',len(coexp),'генов (spearmanr>=0.8)')
for i in coexp:
    print(i,coexp[i])
    
'''
C1Q - serum complement system
C3a - anaphylatoxin released during activation of the complement system
CCR1 - chemokine receptor
CD14 - surface antigen preferentially expressed on monocytes/macrophages
CD300L - cell surface glycoproteins with a single IgV-like extracellular domain, involved in the regulation of immune response
CD4 - membrane glycoprotein of T lymphocytes. The CD4 antigen acts as a coreceptor with the T-cell receptor on the T lymphocyte to recognize antigens displayed by an antigen presenting cell in the context of class II MHC molecules
LILR - leukocyte immunoglobulin like receptor
NCF - neutrophil cytosolic factor

=> SPI1 is responsible for immune cell differentiation
verification from ncbi: transcription factor that activates gene expression during myeloid and B-lymphoid cell development
'''
