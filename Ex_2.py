# Créer une liste de 5 pays
liste_pays = ['France', 'Espagne', 'Italie', 'Allemagne', 'Royaume-Uni']

# Ajouter un sixième pays à la liste
liste_pays.append('Canada')

# Ajouter le 3ème pays de la liste
liste_pays.append(liste_pays[2])

# Remplacer le deuxième pays par un nouveau
liste_pays[1] = 'Australie'

# Supprimer le 4ème pays
del liste_pays[3]

# Afficher la liste finale des pays
print(liste_pays)