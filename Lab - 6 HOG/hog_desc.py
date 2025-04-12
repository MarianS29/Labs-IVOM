import numpy as np
from skimage import io,color
import matplotlib.pyplot as plt
import math
import pdb
import scipy.signal as sig


def hog():

    #PARAMTERS: imagine,tip_nucleu, threshhold
    #RETURN: GV,GH,histograma gradientilor orientati
    
    # calculul gradientilor Gh si GV in functie de fiecare nucleu
     
    # calcul magnitudine si orientare folosind Gh si Gv
    # puteti folosi math.sqrt si math.atan
    # daca folositi math.atan trebuie sa treceti din [-pi/2,i/2] in [0,pi]

    
    #vectorizare magnitudine si gradienti
    
    #anularea orientarilor pentru care magnitudinea este mai mica ca pragul ales
    # altfel spus vreau sa raman in vectorul de orientari doar cu pozitile valorilor
    # pentru care magnitudinea este mai mica decat T
  
    #calculez histograma de orientari pt 9 bins cu np.histogram
    
    #normez histograma la suma elementelor si adun si un epsilon ca sa
    #evit situatia in care impart la 0 (blocul contine o regiune uniforma)
  
    return  

#citesc o imagine     
im=io.imread(')
#transf in gray
im = color.rgb2gray()

#verificare pt Sobel 
Gv,Gh,img_hog=hog()
a=np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,1,1,1]])
gv=np.array([[8,8],[6,6]])
gh=np.array([[ 0,0],[-4,-8]])
print(gv==Gv,gh==Gh)

#calculez gradientii pe nert si horiz si dupa HOG
Gv,Gh,img_hog=hog()

#plotez cum arata Gh si Gv
plt.figure(),plt.imshow(  ,cmap='gray')
plt.figure(),plt.imshow(  ,cmap='gray')

