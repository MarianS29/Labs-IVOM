import numpy as np
from skimage import io,color
import matplotlib.pyplot as plt
import os
import math
from lbp_descriptor import lbp_optimizat

def eucdist():
    
    #PARAMETERS: cei 2 vectori
    #RETURN: distanta
    
    return
    
lbp_mask=np.array( [[2,1,1,1,1,1,2],
                    [2,4,4,1,4,4,2],
                    [1,1,1,0,1,1,1],
                    [0,1,1,0,1,1,0],
                    [0,1,1,1,1,1,0],
                    [0,1,1,2,1,1,0],
                    [0,1,1,1,1,1,0]])

#extrage poze cu os.listdir('path')

#initializarea matricii de descriptori
descriptori_lbp=np.zeros([])

#parcurge pozele rand pe rand
#citeste,tranf in gray

#initializez lista in care calculez descritorii
#calculez pasul pt impartirea in 7x7 ferestre
    lista_histograma_fereastra=[]
    val=math.ceil(im.shape[0]/7)
    
    #parcurg imaginea pe blocuri(7x7)
    
            #decupez fiecare ferastra din cele 49
            fereastra=im[]
            
            #aplic LBP pe fereastra curenta
            
            #calculez histograma ferestrei curente si o inmultesc cu masca
            #folositi np.histogram 256 de bins
            
            #pun histograma in lista
            lista_histograma_fereastra.append(   )
    
    #transform lista de histograme in array
    
    #pun hostogramele concatenate pe linia corespunzatoare imaginii in
    #descriptori_lbp, cel mai simplu este sa folositi flatten() decat 
    #functii de concatenare propriu zise      
    descriptori_lbp[]=

#initializez matrica de distante    
distante=np.zeros([12,12])

#calculez dist euclidiana intre toti descritorii asociati imaginilor
#inclusiv intre aceeasi descriptori
#treb sa obtin o mat care are pe diag principala 0
for k in range():
    for l in range():
        distante[]=eucdist()


nr_fete=0

#vreau sa calculez cate fete imi recunoaste
#logica=> intre descritorii asociati pozelor care tin de aceeasi persoana
#ar trebui sa am distentele cele mai mici
#folosind matricea de distante treb sa scriu un cod care calculeaza
#cate fete imi recunoaste

#HINT: np.sort(),np.argsort()

        
print('Nr de fete este ',  )
