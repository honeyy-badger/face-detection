#importing libraries
import cv2


#cascade classifier
face_cascade = cv2.CascadeClassifier("/home/kakashi/cascade_files/haarcascade_frontalface_default.xml")

#reading images
img = cv2.imread("/home/kakashi/images/cric3.jpeg", 1)

#coverting image into grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#searching co-ordinates of image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)


#resizing image
resize = cv2.resize(img,(550,250))


#displaying the image
cv2.imshow('Ronaldo',resize)
cv2.waitKey(0)
cv2.destroyAllWindows()