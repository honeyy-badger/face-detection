#importing libraries

import cv2


#reading images
img = cv2.imread("/home/kakashi/images/zlatan.jpeg", 1)

#resizing image
resized_image = cv2.resize(img,(500,350))


#displaying image
cv2.imshow('Zlatan',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#displaying images represented as a numpy matrix
print(img)

#type and size
print(type(img))
print(img.shape)