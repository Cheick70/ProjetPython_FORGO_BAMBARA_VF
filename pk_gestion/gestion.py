# PROJET PYTHON POUR DATA SCIENCE M1/IA FORGO Issouf & BAMBARA Cheick Aboubacar
from datetime import datetime
import os
class Banque :
    def __init__(self,nomBanque,siege,typeCompte):
        self.nomBanque=nomBanque # Attribut
        self.siege=siege
        self.typeCompte=typeCompte
        super().__init__()
    
class Client(Banque) :
    def __init__(self,nomBanque,siege,typeCompte,nom,prenom,telephone,soldeInitial,categorie):
        self.nom= nom # Attribut
        self.prenom=prenom
        self.telephone=telephone
        self.soldeInitial=soldeInitial
        #self.categorie=categorie
        self.categorie=self.get_categorie_client(soldeInitial)
        super().__init__(nomBanque,siege,typeCompte)

    def get_categorie_client(self, solde):
        if solde >= 100000000:
            return "VIP"
        elif solde >= 10000000:
            return"Classique"
        else:
            return "Jeune/Etudiant"
            
    # Pour mettre à jours la categorie en fontion des opérations
    def update_categorie(self) :
        categorie1= self.categorie
        self.categorie = self.get_categorie_client(self.soldeInitial)

    # Enregistrement des operation dans le fichier rapport.txt
    def enregistrer_operation(self, operation, montant="N/A"):
        """ Enregistre chaque opération dans `rapport.txt` """
        chemin_rapport = os.path.join(os.path.dirname(__file__), "..", "rapport.txt")  # Fichier situé à la racine du projet
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(chemin_rapport, "a", encoding="utf-8") as fichier:
            fichier.write(f"[{timestamp}] Opération: {operation} | Montant: {montant} | Client: {self.nom} {self.prenom}\n")

    # methode pour depot d'argent
    def depot(self,montant): # Méthode
        if montant> 1000:
           self.soldeInitial+= montant
           # nouveau
           self.enregistrer_operation("Dépôt", montant)
           self.update_categorie()
           print(f"Dépôt de {montant} sur le compte de {self.nom} {self.prenom} reussi ! ")
        else : 
            print("Le montant doit être superieur à 1000 CFA")

    def retrait(self,montantRetire): # Méthode
        if montantRetire< self.soldeInitial:
           self.soldeInitial-= montantRetire
           # nouveau
           self.enregistrer_operation("Retrait", montantRetire)
           self.update_categorie()
           print(f"Retrait de {montantRetire} sur le compte de {self.nom} {self.prenom} reussi !")
        else : 
            print(f"Le montant doit être inferieur à {self.soldeInitial}")
    
    def afficherSolde(self,soldeInitial): # Méthode
        print(f"votre solde et de {self.soldeInitial} FCFA Et votre categorie : {self.categorie} ")
        self.enregistrer_operation("Consultation du solde", self.soldeInitial)
    