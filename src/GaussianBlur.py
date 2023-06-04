import cv2
# Load the image
img = cv2.imread("cat.jpg")
# Apply Gaussian blur with a specified kernel size and standard deviation
ksize = (5, 5)
sigma = 0  
blurred_img = cv2.GaussianBlur(img, ksize, sigma)
# Display the original and blurred images
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
