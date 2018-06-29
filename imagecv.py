import cv2

#loading image
img = cv2.imread('one.jpeg',0)
img1 = cv2.imread('three.jpeg')

#Printing height and width
print (img.shape)

#to display that image
cv2.imshow("Nature", img)
#cv2.imshow("Naturenew", img1)

#image window holder activation
cv2.waitKey(0)

#waitKey will destroy by pressing q
cv2.destroyAllWindows()
