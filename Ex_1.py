# Demande à l'utilisateur de donner les deux nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Calcule la somme des deux nombres
somme = nombre1 + nombre2
print("La somme des deux nombres est :", somme)

# Calcule la différence entre le premier nombre et le deuxième nombre
difference = nombre1 - nombre2
print("La différence entre les deux nombres est :", difference)

# Calcule le produit des deux nombres
produit = nombre1 * nombre2
print("Le produit des deux nombres est :", produit)

# Calcule le quotient du premier nombre divisé par le deuxième nombre
if nombre2 != 0:
    quotient = nombre1 / nombre2
    print("Le quotient du premier nombre divisé par le deuxième nombre est :", quotient)
else:
    print("Erreur : division par zéro.")