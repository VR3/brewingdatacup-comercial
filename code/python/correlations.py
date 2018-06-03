import pandas as pd

df = pd.read_csv('../../data/output/ventas_full.csv')

print(df['Hectolitros'].corr(df['Turismo']))
