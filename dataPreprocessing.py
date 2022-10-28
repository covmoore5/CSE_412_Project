import pandas as pd

df1 = pd.read_csv('Datasets/meddra_all_indications.tsv', header=None, sep='\t')

#print(df)

df1 = df1.drop([0, 2, 4, 5, 6], axis=1)
df1 = df1.drop_duplicates(subset=[1])

df1.to_csv('NewDatasets/indications.csv', header=None, index=None)

df2 = pd.read_csv('Datasets/meddra_all_se.tsv', header=None, sep='\t')

df2 = df2.drop([0,1,2,3], axis=1)
df2 = df2.drop_duplicates(subset=[4])
df2 = df2.rename(columns={4:0, 5:1})
#print(df2)
sideEffect = df2.to_dict()
#print(df2)
#print(sideEffect)
df2.to_csv('NewDatasets/sideEffects.csv', header=None, index=None)

#print(df2)

df3 = pd.read_csv('Datasets/meddra_all_indications.tsv', header=None, sep='\t')

df3 = df3.drop([2,3,4,5,6], axis=1)
df3 = df3.drop_duplicates()
df4 = pd.read_csv('Datasets/drug_names.tsv', header=None, sep='\t')

df4 = df4.drop([0], axis=1)
drugs = df4.to_dict()
df3.to_csv('NewDatasets/treats.csv', header=None, index=None)

df5 = pd.read_csv('Datasets/meddra_all_se.tsv', header=None, sep='\t')
df5 = df5.drop([1,3,4,5], axis=1)
#print(df5)
temp = {'drugId': [], 'seId': []}
for i in range(len(df5)):
    #print(df5.iloc[i, 2])
    if df5.iloc[i, 1] in sideEffect[0].values():
        #print(df5.iloc[i, 0], df5.iloc[i, 1])
        temp['drugId'].append(str(df5.iloc[i, 0]))
        temp['seId'].append(str(df5.iloc[i, 1]))

#print(temp)

df6 = pd.DataFrame(temp, index=None)
df6 = df6.drop_duplicates()
        
#print(df6)
        
df6.to_csv('NewDatasets/drug_se.csv', header=None, index=None)

if 'C0002418' in sideEffect[0].values():
     print("true")
#print(sideEffect[0])