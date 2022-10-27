import pandas as pd

df1 = pd.read_csv('Datasets/meddra_all_indications.tsv', header=None, sep='\t')

#print(df)

df1 = df1.drop([0, 2, 4, 5, 6], axis=1)
df1 = df1.drop_duplicates(subset=[1])

df1.to_csv('NewDatasets/indications.csv', header=None, index=None)

df2 = pd.read_csv('Datasets/meddra_all_se.tsv', header=None, sep='\t')

df2 = df2.drop([0,1,2,3], axis=1)
df2 = df2.drop_duplicates(subset=[4])

df1.to_csv('NewDatasets/sideEffects.csv', header=None, index=None)

print(df2)