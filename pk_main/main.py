# PROJET PYTHON POUR DATA SCIENCE M1/IA FORGO Issouf & BAMBARA Cheick Aboubacar
from pk_gestion.gestion import Client 

# Liste pour stocker les clients
liste_client = []

# Création de 5 clients
for i in range(5):
    print(f"\nCréation du client {i + 1} :")
    nomBanque = input("Entrez le nom de la banque : ")
    siege = input("Entrez le siège de la banque : ")
    typeCompte = input("Entrez le type de compte (Ex: Épargne, Courant, bloqué) : ")
    nom = input("Entrez le nom du client : ")
    prenom = input("Entrez le prénom du client : ")
    telephone = ""
    while True:
        telephone = input("Entrez le numéro de téléphone du client : ")
        if telephone.isdigit() and len(telephone) == 8:
            break  # Sortir de la boucle si le numéro est valide
        else:
            print("Numéro invalide. Veuillez entrer un numéro de téléphone valide (8 chiffres).")

    soldeInitial = ""
    while True:
        solde_input = input("Entrez le solde initial : ")
        if solde_input.isdigit():
            soldeInitial = int(solde_input)
            break  # Sortir de la boucle si le sold est valide
        else:
            print("solde invalide. Veuillez entrer un solde valide (des chiffres).")
    
    categorie = input("Entrez la catégorie (Ex: VIP, Classique, Jeune/Etudiant) : ")

    # Création et ajout du client à la liste
    client = Client(nomBanque, siege, typeCompte, nom, prenom, telephone, soldeInitial, categorie)
    liste_client.append(client)

print("\nTous les clients ont été créés avec succès !")

# Menu pour gérer les opérations sur les clients
while True:
    print("\nMenu des opérations :")
    print("1. Effectuer un dépôt")
    print("2. Effectuer un retrait")
    print("3. Afficher le solde")
    print("4. Quitter")

    choix = input("Entrez votre choix (1/2/3/4) : ")

    if choix in ["1", "2", "3"]:
        # Sélectionner le client pour l'opération
        print("\nListe des clients disponibles :")
        for index, client in enumerate(liste_client):
            print(f"{index + 1}. {client.nom} {client.prenom}")

        client_index = int(input("Entrez le numéro du client : ")) - 1

        if 0 <= client_index < len(liste_client):
            client = liste_client[client_index]
            if choix == "1":
                montant = int(input(f"Entrez le montant à déposer pour {client.nom} {client.prenom} : "))
                client.depot(montant)
            elif choix == "2":
                montant = int(input(f"Entrez le montant à retirer pour {client.nom} {client.prenom} : "))
                client.retrait(montant)
            elif choix == "3":
                client.afficherSolde(soldeInitial)
        else:
            print("Numéro de client invalide.")
    elif choix == "4":
        print("Merci d'avoir utilisé notre application. À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
    