
'''Declaration de la super class  du class Guichetier''' 
class Personne:
 def __init__(self,nom,fonction): #Declaration du constructeur de la super classe
    self.nom = nom
    self.fonction = fonction
    
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
    
