import pandas as pd
df = pd.read_csv("sample.csv")
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].fillna(df['Score'].mean())

df = df.drop_duplicates()

df_filtered = df[df['Age'] > 25]

print("Cleaned Data:")
print(df_filtered)

df_filtered.to_csv("Cleaned-data csv", index=False)
