from ChefAgence import ChefAgence
from Guichetier import Guichetier
from Gestionnaire import Gestionnaire
from Controlleur import Controlleur

class Banque(ChefAgence,Guichetier,Gestionnaire,Controlleur): 
	#Declaraion du constructeur
    def __init__(self,nom,guichetier,controlleur,gestionnaire,chefAgence):
	    self.nom = nom 
	    self.guichetier = guichetier
	    self.controlleur = controlleur
	    self.gestionnaire = gestionnaire
	    self.chefAgence = chefAgence
	 
	#Declaration des accesseurs et mutateurs des attributs
    def _getguichetier(self):
	    return self.guichetier
    def _setguichetier(self,gui):
     self.guichetier = gui
    guichetier = property(_getguichetier,_setguichetier)
    
    def _getcontrolleur(self):
	    return self.controlleur
    def _setcontrolleur(self,con):
     self.controlleur = con
    controlleur = property(_getcontrolleur,_setcontrolleur) 

    def _getgestionnaire(self):
	    return self.gestionnaire
    def _setgestionnaire(self,ges):
     self.gestionnaire = ges
    gestionnaire = property(_getgestionnaire,_setgestionnaire)	 
	 
    def _getchefAgence(self):
	    return self.chefAgence
    def _setchefAgence(self,chef):
      self.chefAgence = chefAgence
    chefAgence = property(_getchefAgence,_setchefAgence) 

 #Done by Ngeh Hermann
