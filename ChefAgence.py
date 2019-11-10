import os
class ChefAgence:

 def immobilier():
   nature = str(input("\tEntrez la nature du bien immobilier a acheter : "))
   valeur = int(input("\tEntrez la valeur d'acquisition  :"))
   print("Vous venez d\'effecetuer l\'achat de", nature, "d\'une valeur de", valeur, "FCFA"  ) 
   
 def marketing():
     nature = str(input("\tProjet marketing a financer : "))
     valeur = int(input("\tSomme investi  :"))
     print("Vous venez de financer le projet marketing", nature, "d\'une valeur de", valeur, "FCFA"  )
	 
 def materiels():
   nature = str(input("\tMateriels a acheter : "))
   valeur = int(input("\tEntrez la valeur d'acquisition  :"))
   print("Vous venez d\'effecetuer l\'achat de", nature, "d\'une valeur de", valeur, "FCFA"  ) 
 
 choice = ''
 while choice != 4:
   print("\t\t\t>>>ACHAT DES CONSOMMABLES \n")
   print("\tBien vouloir choisir l\'operation que vous souhaitez effectuer :\n")
   print("\t\t1 : immobilier")
   print("\t\t2 : marketing")
   print("\t\t3 : Materiels et Communications \n")
   print("\t Appuyez sur 4 pour Quitter !")
   choice = input()


   if choice == '1' :
      immobilier()
   elif choice == '2':
      marketing()
   elif choice == '3':
       materiels()
   elif choice == '4' :
     break
   else :
     print("Le Choix est invalide")

   choice = input("Entrer votre choix : ")
   #Travail réalisé par BAYANG NYOMO VINCENT 17A681FS
