import pandas as pd
# charger les fichiers
df = pd.read_csv("ventes_ecommerce.csv", parse_dates=["date"])
agg = pd.read_csv("resultats_aggregation.csv")

# Ajouter la colonne 'mois'
df['mois'] = df['date'].dt.to_period('M')

# Aggregation: totatl des vents par mois et par catégorie
agg = df.groupby(['mois','catégorie'])['montant'].sum().reset_index()
# Sauvegarde du resultat dans un nouveau fichier CSV
agg.to_csv("resultats_aggregation.csv", index=False)

