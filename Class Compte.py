import os

class Compte :
 def __init__(self,numero,typ,solde):
	 self.numero = numero
	 self.typ = typ
	 self.solde = 0
 def _getnumero(self):
	 return self.numero
 def _setnumero(self,n):
     self.numero = n
 numero = property(_getnumero,_setnumero)
 
 def _gettyp(self):
	 return self.typ
 def _settyp(self,t):
     self.typ = t
 typ = property(_gettyp,_settyp)
 
 def _getsolde(self):
	 return self.solde
 def _setsolde(self,s):
     self.solde = s
 solde = property(_getsolde,_setsolde)
 
 def depot():
   solde += somme
   return solde

 def retrait():
	 solde -= somme
