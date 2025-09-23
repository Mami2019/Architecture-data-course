import pandas as pd
def verif_aggregation_absenteisme(df_original, df_agg):
    attendu = df_original.groupby(['departement', 'motif_absence'])['duree_jours'].sum().reset_index()
    pd.testing.assert_frame_equal(
        df_agg.sort_values(['departement', 'motif_absence']).reset_index(drop=True),
        attendu.sort_values(['departement', 'motif_absence']).reset_index(drop=True)
    )
    print("✅ Test d'agrégation RH réussi : les résultats sont corrects.")

if __name__== "__main__":
    df_original = pd.read_csv("absenteisme_rh.csv")
    df_agg = pd.read_csv("resultats_absenteisme.csv")
    verif_aggregation_absenteisme(df_original, df_agg)

