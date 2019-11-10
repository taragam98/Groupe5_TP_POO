
'''Fait par : TARABAI GAMBARA : 17A472FS'''

import os 
from Personne import Personne
from Compte import Compte


 #Declaration de la classe fille Guichetier
class Guichetier(Personne):
  def __init__(self,nom,fonction,solde,somme): #Declaration du constructeur de la classe fille
   Personne.__init__(nom,fonction)  #Declaration du constructeur de la super classe dans la classe fille
   self.solde = solde
   self.somme = somme
	   
 #Declaration de l'accesseur et du mutateur du solde
  def _getsolde(self):
    return self._solde
  def _setsolde(self,sol):
	  self.solde = sol 
  solde = property(_getsolde,_setsolde)
 
 #Declaration de l'accesseur et du mutateur de la somme
  def _getsomme(self):
	  return self.somme
  def _setsomme(self,som):
	  self.somme = som
  somme = property(_getsomme,_setsomme) 
 
  def versement():
   solde = 0.0
   to = ''
   type = 0
   print("\n\tDans quelle compte souhaitez vos effetuer cette operation ??? ")
   print("\t 1 : Compte d'epargne")
   print("\t 2 : Compte Courant")
   print("\t 3 : Gre a Gre")
   to = input()
   if to == '1':
    somme = int(input("\t Entrer la somme a verser : "))
    solde += somme
    print(" \n\tVotre nouveau solde est : ", solde,"FCFA")
   elif to == '2':
    somme = int(input("\t Entrer la somme a verser : "))
    solde += somme
    print("\n\t Votre nouveau solde est : ", solde,"FCFA")
   elif to == '3':
    numde = int(input("\tEntrer le numero de compte du destinataire : "))
    somme = int(input("\t Entrer la somme a deposer sur le compte : "))
    solde += somme
    print("\t Vous avez transferee ", solde,"FCFA au compte ",numde,"!!!")
   else:
    print("\tchoix invalide")
  def retrait():
   solde = 20
   somme = int(input("\tEntrer la somme a retirer : "))
   if solde < somme:
	   print("\tvous ne pouvez pas effectuer de retrait !!!")
	   print("\tVotre solde est inferieure au montant a retirer !!!")
   else:
    solde -= somme
    print("\tVotre nouveau solde est : ", solde)
   

  
  def virement():
     solde = 20
     somme = int(input("\n\tEntrer la somme a virer : "))
     if  solde < somme :	 
      print("\tVotre solde est inferieure au montant a virer !!!")
     else:
      solde -= somme
      print("\tVirement effectuee avec succes !!! ")
      print("\n\tVotre nouveau solde est de : ",solde,"FCFA")

  def operationInter():
     print("\tQuelle operation souhaitez vous effectuez a l'international??")
     print("\t1 : Versement")
     print("\t2 : Retrait")
     op = input()    
     print("Votre operation a bien ete effectuee")
 #Redefinition de la methode salutation dans la classe fille
  def salutation():
	  print("\n\tMerci pour votre fidelite \n")
	 
 #Execution de la programme principal(Ce qui s'affiche a l'ecran   
  Personne.salutation() #Appel de la methode de la super classe
  salutation()   #Appel de la methode de la classe fille
  ch = ''
  num = 0
  while ch != 5:
   print("\tQuelle operation souhaitez effectuer ??")
   print("\t1 : Versement")
   print("\t2 : Retrait")
   print("\t3 : Virement dans une autre banque")
   print("\t4 : Operation a l'international")
   print("\t Appuyez sur 5 pour Quitter !!")
   ch = input()


   if ch == '1' :
      num = int(input("\tEntrer le numero de compte : "))
      versement()
   elif ch == '2':
       num = int(input("\tEntrer le numero de compte : "))
       retrait()
   elif ch == '3':
      num = int(input("\tEntrer le numero de compte de l'expediteur : "))
      numde = int(input("\tEntrer le numero de compte du destinataire : "))
      virement()
   elif ch == '4':
     operationInter()
   elif ch == '5' :
     print("\t Merci de votre visite !!")
     break
   else :
     print("\tChoix invalide.")

   ch = input("\n\tAppuyer sur Entrer pour continuer !!!")
   
