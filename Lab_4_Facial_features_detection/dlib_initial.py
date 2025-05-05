import numpy as np
import dlib
import cv2
import matplotlib.pyplot as plt
import pdb
 
def rect_to_bb(rect):
	# ia un dreptunghi prezis de dlib si il converteste intr-un format
    # acceptat de opencv (x,y,w,h)
	x = rect.left()
	y = rect.top()
	w = rect.right() - x
	h = rect.bottom() - y
#	pdb.set_trace()
	# returneaza un tuplu (x, y, w, h)
	return (x, y, w, h)

def shape_to_np(shape, dtype="int"):
	# initializeaza o lista pt cele 68 de coordonate
	coords = np.zeros((68, 2), dtype=dtype)
 
	# parcurge toate cele 68 de landmarkuri
    # shape este un obiect dlib, part este metoda care acceseaza fiecare punct
    # shape.part(i) acceseaza fiecare pereche(i) din care acceseaza atat coord x cat si y
	for i in range(0, 68):
		coords[i] = [shape.part(i).x, shape.part(i).y]
 
	# returneaza coordonatele sub forma unei matrici 68 x 2
    # prima coloana reprezinta coloana iar cea de-a doua linia
	return coords

    
# initializeaza detectorul de fete din dlib si predictoul punctelor faciale
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('C:\\Users\\Andrei\\Desktop\\IVOM_LAB\\lab_4_face_landmarks\\shape_predictor_68_face_landmarks.dat')

# incarca imaginea si o transforma in grayscale
image = cv2.imread('C:\\Users\\Andrei\\Desktop\\IVOM_LAB\\labIVOMS\\Images\\BioID_F1_1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# foloseste detectorul initializat anterior sa gaseasca toate fetele din imagine
rects = detector(gray, 1)

# parcurge toate fetele din imagine(i pozitie,rect fata propriu-zisa)
for (i, rect) in enumerate(rects):
	# determina coordonatele faciale pentru fiecare fata detectata
	# foloseste functia shape_to_np sa converteasca perechile de coord (x,y) in numpy array
	shape = predictor(gray, rect)
	shape = shape_to_np(shape)
 
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
cv2.imshow("Output", cv2.resize(image,(600,600)))
cv2.namedWindow("Output", cv2.WINDOW_NORMAL)
cv2.waitKey(1000)  

