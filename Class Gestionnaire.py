
'''Declaration de la super class  du class Guichetier''' 
class Personne:
 def __init__(self,nom,fonction): #Declaration du constructeur de la super classe
    self._nom = nom
    self._fonction = fonction
    
 #Declaration de l'accesseur et du mutateur de nom
 def _getnom(self):
    return self._age
 def _setnom(self,nouveauNom):
	 self.nom = nouveauNom 
 nom = property(_getnom,_setnom)
 
 #Declaration de l'accesseur et du mutateur de fonction
 def _getfonction(self):
	 return self.fonction
 def _setfonction(self,f):
	 self.fonction = f
 fonction = property(_getfonction,_setfonction)
	 
 #Declaration d'une methode qui est commun a toute les classes filles	 
 def salutation():   
    nom = input("\n\tSaisir votre nom : ")
    print("\n\tBonjour Monsieur ",nom)
    print("\n\tBienvenue dans notre banque !!!")

class Gestionnaire(Personne):
	
  
    def __init__(self,nom,fonction,solde,somme):
     Personne.__init__(nom,fonction)  #Declaration du constructeur de la super classe dans la classe fille
     self._solde = solde
     self._somme = somme
       	   
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
    
    def emprunt(): 
     dette = 0
     taux = 15
     if dette == 0 :	
         dette = int(input("\n\tSaisir la somme que vous souhaitez emprunter :"))
         print("\n\tEmprunt effectuee !!!")
      
         dette += (dette // taux)
         print("\n\t",dette," seront deduit de votre compte lors du remboursement.")
     else:
         print("\n\tVous ne pouvez pas effectuer d'emprunt, vous avez une dette non remboursee")
	 
    def ajouter():
       nom = input("\tSaisir votre nom : ")
       solde = int(input("\n\tSaisir le montant initial : "))
       print("\n\tVotre compte a ete cree avec succes")
       print("\n\tVous disposez de ",solde,"FCFA dans votre compte")
    def supprimer():
       nom = input("\n\tSaisir votre nom : ")
       num = int(input("\tEntrer le numero de compte : "))
       print("\n\tLe compte numero ",num,"a ete supprimee avec succes.")
    def modifier():
        nom = input("\tSaisir votre nom : ")
        nouveauNom = input("\n\tSaisir le nouveau nom de votre compte : ")
        print("\n\tVotre compte a ete modifiee avec succes.")
        print("\n\tVotre nouveau nom est {} ".format(nouveauNom))
        
    co = ''
    num = 0
    while co != 5:
       print("\tQuelle operation souhaitez effectuer ??")
       print("\t1 : Effectuer un emprunt")
       print("\t2 : Ajouter un compte")
       print("\t3 : Supprimer un compte")
       print("\t4 : Modifier un compte")
       print("\t Appuyez sur 5 pour Quitter !!")
       co = input()    
       if co == '1' :
        num = int(input("\tEntrer le numero de compte : "))
        emprunt()
       elif co == '2':
        num = int(input("\tEntrer le numero de compte : "))
        ajouter()
       elif co == '3':
        supprimer()
       elif co == '4':
        num = int(input("\tEntrer le numero de compte : "))
        modifier()
       elif co == '5' :
        print("\t Merci de votre visite !!")
        break
       else :
        print("\tChoix invalide.")
        
       co = input("\n\tAppuyer sur Entrer pour continuer !!!")

    
