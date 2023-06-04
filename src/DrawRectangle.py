import cv2
# Load the image
img = cv2.imread("cat.jpg")
# Define the rectangle parameters
x = 40
y = 20
w = 150
h = 200 
# Draw the rectangle on the image
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# Display the image with the rectangle
cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
