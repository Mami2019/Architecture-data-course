import pandas as pd
df = pd.read_csv("absenteisme_rh.csv")
resultats = df.groupby(['departement', 'motif_absence'])['duree_jours'].sum().reset_index()
resultats.to_csv("resultats_absenteisme.csv", index=False)
result = pd.read_csv("resultats_absenteisme.csv")
print(result)