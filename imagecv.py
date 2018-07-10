import cv2

#loading image
img = cv2.imread('image.jpg',0)
img1 = cv2.imread('image.jpg')

#Printing height and width
print (img.shape)

#to display the B&W image
cv2.imshow("Nature_B&W", img)
#to display the colored one
cv2.imshow("Nature", img1)

#image window holder activation
cv2.waitKey(0)

#waitKey will destroy by pressing q
cv2.destroyAllWindows()
