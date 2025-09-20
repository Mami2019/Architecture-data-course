import pandas as pd

# Charger le fichier CSV
df = pd.read_csv("ventes_ecommerce.csv", parse_dates=["date"])

# Ajouter la colonne 'mois'
df['mois'] = df['date'].dt.to_period('M')

# Agrégation
agg = df.groupby(['mois', 'catégorie'])['montant'].sum().reset_index()

# Fonction de test
def test_aggregation(df_original, df_agg):
    test = df_original.copy()
    test['mois'] = test['date'].dt.to_period('M')  # Assure que 'mois' existe
    expected = test.groupby(['mois', 'catégorie'])['montant'].sum().reset_index()
    pd.testing.assert_frame_equal(
        df_agg.sort_values(['mois', 'catégorie']).reset_index(drop=True),
        expected.sort_values(['mois', 'catégorie']).reset_index(drop=True)
    )
    print("✅ Test d'agrégation réussi : les résultats sont corrects.")

# Appel de la fonction de test
test_aggregation(df, agg)