# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:43:14 2021

@author: leoro
"""

import femm
import matplotlib.pyplot as plt
import numpy as np


## Modélisation avec FEMM

femm.openfemm(1)
femm.newdocument(0)
femm.mi_addnode(0,0)
femm.mi_addnode(0,120)
femm.mi_addsegment(0,0,0,120)
femm.mi_drawrectangle(0,0,110,40)
femm.mi_drawrectangle(0,70.2,110,110.2)
femm.mi_drawrectangle(40,40,100,70)
femm.mi_drawrectangle(70,45,80,70)
femm.mi_drawrectangle(0,0,120,120)
femm.mi_probdef(0,'millimeters','axi',10**(-8),0,30,(0))
# définition du courant I
I=1
femm.mi_addcircprop('I',I,1)
femm.mi_addmaterial('RECTANGLE',1000,1000,0,0,0,0,0,0,0,0,0,0,0,0)
femm.mi_addmaterial('CUBE',1,1,0,0,0,0,0,0,0,0,0,0,0,0)

# sélection des blocs
femm.mi_addblocklabel(1,1) # on sélectionne un bloc en prenant un point lui appartenant
femm.mi_addblocklabel(1,80)
femm.mi_selectlabel(1,1)
femm.mi_selectlabel(1,80)
# affectation des propriétés aux blocs
femm.mi_setblockprop('RECTANGLE',1,0,0,0,0,0)
femm.mi_clearselected()
# 
femm.mi_addblocklabel(75,60)
femm.mi_selectlabel(75,60)
femm.mi_setblockprop('CUBE',1,0,'I',0,0,88)
femm.mi_clearselected()
# 
femm.mi_addblocklabel(41,41)
femm.mi_selectlabel(41,41)
femm.mi_setblockprop('RECTANGLE',1,0,0,0,0,0)
femm.mi_clearselected()
#
femm.mi_addblocklabel(105,50)
femm.mi_selectlabel(105,50)
femm.mi_setblockprop('CUBE',0,0,0,0,0,0)
femm.mi_clearselected()


# Euler implicite : calcul de i(t)

# initialisation
t = 0.01
dt = 0.01
i = 0
L = 0.2
ip = [i] 

while t < 1 :
    i = i + dt/L*(24 - 6*i) 
    femm.mi_setcurrent('I',i) # actualisation de la valeur du courant
    femm.mi_saveas('M1CS.fem')
    femm.mi_analyze()
    femm.mi_loadsolution()
    L = femm.mo_getcircuitproperties('I')[2] 
    t += dt
    ip.append(i) # stockage des valeurs
        
ip2 = np.array(ip)
X = np.linspace(0,20,100)
plt.plot(X,ip2)
plt.show()


## Cas non-linéaire

femm.openfemm(1)
femm.newdocument(0)
femm.mi_addnode(0,0)
femm.mi_addnode(0,120)
femm.mi_addsegment(0,0,0,120)
femm.mi_drawrectangle(0,0,110,40)
femm.mi_drawrectangle(0,70.2,110,110.2)
femm.mi_drawrectangle(40,40,100,70)
femm.mi_drawrectangle(70,45,80,70)
femm.mi_drawrectangle(0,0,120,120)
femm.mi_probdef(0,'millimeters','axi',10**(-8),0,30,(0))
# courant I
I=1
femm.mi_addcircprop('I',I,1)
femm.mi_getmaterial('Pure Iron')
femm.mi_addmaterial('CUBE',1,1,0,0,0,0,0,0,0,0,0,0,0,0)

# sélection des blocs
femm.mi_addblocklabel(1,1)
femm.mi_addblocklabel(1,80)
femm.mi_selectlabel(1,1)
femm.mi_selectlabel(1,80)
# affectation des propriétés aux blocs
femm.mi_setblockprop('Pure Iron',1,0,0,0,0,0)
femm.mi_clearselected()
# 
femm.mi_addblocklabel(75,60)
femm.mi_selectlabel(75,60)
femm.mi_setblockprop('CUBE',1,0,'I',0,0,88)
femm.mi_clearselected()
# 
femm.mi_addblocklabel(41,41)
femm.mi_selectlabel(41,41)
femm.mi_setblockprop('Pure Iron',1,0,0,0,0,0)
femm.mi_clearselected()
#
femm.mi_addblocklabel(105,50)
femm.mi_selectlabel(105,50)
femm.mi_setblockprop('CUBE',0,0,0,0,0,0)
femm.mi_clearselected()

t = 0.01
dt = 0.01
i = 0
L = 0.2
ip3 = [i]

while t < 1 :
    i = i + dt/L*(24 - 6*i) 
    femm.mi_setcurrent('I',i) 
    femm.mi_saveas('M1CS.fem')
    femm.mi_analyze()
    femm.mi_loadsolution()
    L = femm.mo_getcircuitproperties('I')[2]
    ip3.append(i)
    t += dt
    
    
## Graphique
    
ip4 = np.array(ip3)
X = np.linspace(0,20,100)

plt.plot(X,ip2,'red',label='Linéaire')
plt.plot(X,ip4,'--k',label='Non linéaire')
plt.legend()
plt.show()
