SELECT produit, SUM(montant) AS total_ventes
FROM PRD_DWH.VENTES 
WHERE date >= '2023-01-01'
GROUP BY produit
ORDER BY total_ventes DESC;