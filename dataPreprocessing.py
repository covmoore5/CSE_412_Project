import pandas as pd

df = pd.read_csv('Datasets/meddra_all_indications.tsv', header=None, sep='\t')

#print(df)

df = df.drop([0, 2, 4, 5, 6], axis=1)
df = df.drop_duplicates(subset=[1])

print(df)



df.to_csv('NewDatasets/indications.csv', header=None, index=None)