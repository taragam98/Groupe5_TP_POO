#import  os
from Personne import Personne

class Controlleur(Personne):
    def __init__ (self,nom,fonction,solde,somme,montant,sommeTotal):
        Personne.__init__(nom,fonction)  #Declaration du constructeur de la super classe dans la classe fille
        self.solde = solde
        self.somme = somme
       	self.montant=montant
        self.sommeTotal=sommeTotal
           
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
    
    def verifier(sommeTotal,montant):   
        if sommeTotal == montant  :
	            print("La somme en caisse est egal au transaction")
       
        else:
                print("Le montant en caisse ne cadre pas avec la transaction journaliere.")
                # DONE BY :NGORAN ROSSINE : 18A083FS
        
 
