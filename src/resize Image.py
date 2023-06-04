import cv2
# Load the image
img = cv2.imread("cat.jpg")
# Define the new dimensions for the resized image
new_width = 80
new_height = 60
# Resize the image
resize_img = cv2.resize(img, (new_width, new_height))
# Display the Original image
cv2.imshow("Original Image",img)
# Display the resized image
cv2.imshow("Resized Image",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
