 import os
from Compte import Compte

class CompteEpargne(Compte):
    def __init__(self,numero,typ,solde,nom):
        Compte.__init__(self,numero,typ,solde)
        
    def _getnom(self):
        return self.nom
    def _setnom(self,nouveauNom):
        self.nom = nouveauNom
    nom = property(_getnom,_setnom)
      
    #Appel de la methode depot de a classe mere          
    Compte.depot() 
    #Appel de la methode retrait de la classe mere 
    Compte.retrait()     
# representé par : MAHAMAT OUSMAN AMADOU : 18B233FS
