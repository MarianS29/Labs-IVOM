import numpy as np
from skimage import io,color
from skimage.transform.integral import integral_image
import os
import matplotlib.pyplot as plt

#########################
#######  Part 1  ########
########################

#Nu uitati ca aveti nevoie si de functiile de img_intgralas si suma_dreptunghi
#calcul trasaturi HAAR(1,2,3,4)
#CONVENTIE : zonele albe(+),zonele negre(-) 
 
def haar_unu():
    
    # [zn]
    # [za]
    
    #PARAMETERS: pozitia pixelului din coltul st-sus (l,c), dim dreptunghiului(h,w), img_integ
    # RETURN (zonele negre,zonele albe, catacteristica propriu-zisa)
    zona_neagra=
    zona_alba=
    H1=
    
    return()

def haar_doi():
    
    # [za] [zn]
    
    #PARAMETERS: pozitia pixelului din coltul st-sus (l,c), dim dreptunghiului(h,w), img_integ
    # RETURN (zonele negre,zonele albe, catacteristica propriu-zisa)
    zona_neagra=
    zona_alba=
    H2=
    
    return()
    
def haar_trei(l,c,h,w,img_integ):
    
    # [zn] [za] [zn]
    
    #PARAMETERS: pozitia pixelului din coltul st-sus (l,c), dim dreptunghiului(h,w), img_integ
    # RETURN (zonele negre,zonele albe, catacteristica propriu-zisa)
    zona_neagra_1=
    zona_neagra_2=
    zona_alba=
    H3=
    
    return()
    
def haar_patru():
    
    # [za] [zn] 
    # [zn] [za] 
    
    #PARAMETERS: pozitia pixelului din coltul st-sus (l,c), dim dreptunghiului(h,w), img_integ
    # RETURN (zonele negre,zonele albe, catacteristica propriu-zisa)
    
    zona_neagra_1=
    zona_neagra_2=
    zona_alba_1=
    zona_alba_2=
    H4=
  
    return()


# pentru mat b haar 1   
# zn,za,haar1=haar_unu(0,0,2,2,img_integ)
# print(zn,za,haar1)

# pentru mat a haar 2  
# zn,za,haar2=haar_doi(0,0,4,4,img_integ2)
# print(zn,za,haar2)

# pentru mat b haar 3 
# za1,za2,zn1,haar3=haar_trei(0,0,2,3,img_integ)
# print(za1,za2,zn1,haar3) 

# pentru mat a haar 4 
# zn1,zn2,za1,za2,haar4=haar_patru(0,0,4,4,img_integ2)
# print(zn1,zn2,za1,za2,haar4)


#########################
#######  Part 2  ########
########################


#functie pentru caluclul performnatei tp,tn,fp,fn
def performanta(pred_haar, ref):
    
    #Parameters : etichete_referinta, trasaturi_haar, nr_poze
    tp= np.logical_and(pred_haar==1, ref==1).sum()/10
    fn= 
    tn=
    fp=
    print(tp,fn,tn,fp)

#creeaza liste nume poze (sugestie os.listdir)
poze=

#creeaza o lista pt trasaturile haar
lista_haar=[]

#parcurge pozele
for 
    #citeste imagine si transforma in gray
    im=io.imread()
    im = color.rgb2gray(im)
    #calculeaza imaginea integrala pt fiecare poza
    ii=integral_image()
    
    #calculeaza 2 variuante de trasaturi haar 
    # zn1,za1,gg,haar3=haar_trei(0,0,6,24,ii)
    # zn1,za1,haar3=haar_doi(0,6,12,12,ii)
    
    #adauga in lista valoarea trasaturii pt fiec poza
    
            
#transforma lista de valori Haar in array       
lista_haar_2=np.asarray()

# creeaza a doua axa pentru figura
y= 

#ploteaza intr-o figura valorile haar pt fete cu verde si non-fete cu rosu
plt.figure() 
plt.scatter(, color='g')
plt.scatter(, color='r')

#initializeaza referintele

#alegeti pragul aastfel incat Tp max FP min
#folositi sintaxa m[conditie]=
T=
#apelati fct de performanta 
performanta()



