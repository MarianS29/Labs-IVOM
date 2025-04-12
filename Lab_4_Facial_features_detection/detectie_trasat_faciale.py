#Pt conectarea driveului la COLAB
#fisierele voastre se afla la /content/gdrive/My Drive/

#from google.colab import drive
#
#drive.mount('/content/gdrive')


import pdb
import numpy as np
import dlib
import cv2
import matplotlib.pyplot as plt


def rect_to_bb(rect):
	# ia un dreptunghi prezis de dlib si il converteste intr-un format
    # acceptat de opencv (x,y,w,h)
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
 
	# returneaza un tuplu (x, y, w, h)
	return (x, y, w, h)

def shape_to_np(shape, dtype="int"):
	# initializeaza o lista pt cele 68 de coordonate
	coords = np.zeros((68, 2), dtype=dtype)
 
	# parcurge toate cele 68 de landmarkuri
    # shape este un obiect dlib, part este metoda care acceseaza fiecare punct
    # shape.part(i) acceseaza fiecare pereche din care acceseaza atat coord x cat si y
	for i in range(0, 68):
		coords[i] = [shape.part(i).x, shape.part(i).y]
 
	# returneaza coordonatele sub forma unei matrici 68 x 2
    # prima coloana reprezinta coloana iar cea de-a doua linia
	return coords

def decupeaza_ochi_gura():
    
    #PARAMETERS : imaginea gray,imaginea color, coordonatele componentei faciale(ochi_st,ochi_dr,gura)
    #RETURN : portiunea din imaginea gray asociata fiecarei trasaturi faciale
    
    #ca sa desenez dreptunghiul pt ochi si gura am nevoie de un colt st-sus si dr-jos
    #ma folosesc de vectorul de coordonate asociat fiecarei componente faciale pt a determina
    #punctele relevante pentru dreptunghiul de incadrare
    # NU UITATI ca pe coloana 1 avem coordonatele coloanelor, iar pe coloana 2 coord liniilor
   


    # deseneaza dreptunghi, pozitia colturilor este de tipul (coloana,linie) si nu (linie,coloana)
    # primul param este imaginea color pt ca pe ea vreau sa marchez ochii si gura
    # cele 2 tupluri sunt asociate pt coltul din st_sus si dr_jos
    #foloseste culoarea rosie(BGR), iar linia are grosime 3
    cv2.rectangle(   ,  (),  (),(0,0,255),3)
    
    #returneaza decupajul ochilor si al gurii folosind imaginea grayscale
    return 


def detecteaza_irisi():
    
    
    #PARAMETERS: img_gray,img_color,coordonate pt fiecare ochi,portiunea decupata pt fiec trasatura din img initiala
    
    
    # ca sa scalez la intreaga imagine am nevoie de coltul din stanga sus al dreptunghiului
    # care imi contine toate punctele faciale asociate trasaturii curente
    min_linii = 
    min_coloane = 
    
    #proiectiile integrale pe H si V cu np.sum() pe img gray
    suma_coloane=
    suma_linii=   
    
    #
    dim=
    capat=int(np.floor(dim/2))
    suma_coloane_new=np.zeros()
    suma_linii_new=np.zeros()
    
    #filtrare temporala folosin np.mean() pt fereastra respectiva
    for i in range(capat,len(suma_coloane)-capat):
        
    for i in range(capat,len(suma_linii)-capat)
  
    # calculeaza pozitia punctului minim din dreptinghi(prob iris)
    #folosim np.where care primeste ca parametru o conditie
    #rezultatul va fi pozitia pe care se afla valoarea minima
    linie_iris=np.where()
    coloana_iris=np.where()
  
    #decide unde se uita persoana in functie de proiectia pe V
    
    
    
    #deseneaza cu albastru irisul in imaginea color  
    #in tuplu treb specificata poz irisului calculata
    #NU UITATI ca trebuie sa scalati la dim imaginii originale, deci la pozitia determinata trebuie adunata
    #pozitia coltului din st-sus pt vectorul de coordonate
    cv2.circle(   ,   (),3, (255,0,0),2)
    
    #plotez proiectiile pe H si pe V
    plt.figure()
    plt.title('Proiectie orizontala')
    plt.scatter(    ,   )
    plt.figure()
    plt.title('Proiectie verticala')
    plt.scatter(     ,     )

  
    
# initializeaza detectorul de fete din dlib si predictoul punctelor faciale
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('C:\\Users\\Andrei\\Desktop\\IVOM_LAB\\lab_4_face_landmarks\\shape_predictor_68_face_landmarks.dat')

# incarca imaginea si o transforma in grayscale
#image = cv2.imread('C:\\Users\\Andrei\\Desktop\\IVOM_LAB\\labIVOMS\\Images\\BioID_F1_1.jpg')
image = cv2.imread('face2.png')
#image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# foloseste detectorul initializat anterior sa gaseasca toate fetele din imagine
rects = detector(gray, 1)

# parcurge toate fetele din imagine(i pozitie,rect fata propriu-zisa)
for (i, rect) in enumerate(rects):
	# determina coordonatele faciale pentru fiecare fata detectata
	# foloseste functia shape_to_np sa converteasca perechile de coord (x,y) in numpy array
	shape = predictor(gray, rect)
	shape = shape_to_np(shape)
    
    #Decupez din shape portiunile aferente ochilor si gurii
    #Trebuie sa va uitati la ordinea punctelor din platforma si sa selectati landmarkurile
    #corespunzatoare pt fiecare componenta faciala
	ochi_st= 
	ochi_dr=
	gura=
    
    #foloseste fctia de detectie pentru componentele faciale folosind parametrii corespunzatori
	os=decupeaza_ochi_gura(       )
	od=decupeaza_ochi_gura(           )
	g=decupeaza_ochi_gura(         )
    
    #apeleaza fctia de detectie de iris cu param coresp
    # trebuie sa folositi si marimile calcutate mai sus (os si od)
	detecteaza_irisi(         )
	detecteaza_irisi(           )
 
	# converteste dreptunghiul detectata intr-un format convenabil opencv
	(x, y, w, h) = rect_to_bb(rect)
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
 
	# arata numarul fetei detectate
	cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
 
	# deseneaza punctele faciale pentru fiecare fata
	for (x, y) in shape:
		cv2.circle(image, (x, y), 1, (0, 0, 255), -1)
 
# afiseaza imgainea cu fetele detectate si punctele faciale aferente

#pt COLAB    
# cv2_imshow(cv2.resize(image,(600,600)))
        
cv2.imshow("Output", cv2.resize(image,(600,600)))
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.waitKey(1000)  
#cv2.destroyAllWindows()

