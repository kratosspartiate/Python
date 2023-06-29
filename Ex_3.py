def afficher_info(etudiant):
    print("Nom de l'étudiant:", etudiant["nom"])
    print("Âge de l'étudiant:", etudiant["age"])
    print("Matière préférée de l'étudiant:", etudiant["matiere_preferee"])

# Création du dictionnaire contenant les informations de l'étudiant
etudiant = {
    "nom": "John Doe",
    "age": 20,
    "matiere_preferee": "Mathématiques"
}

# Appel de la fonction pour afficher les informations de l'étudiant
afficher_info(etudiant)