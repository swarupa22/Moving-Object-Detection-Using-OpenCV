import cv2
# Load the image 
img = cv2.imread("cat.jpg")
#Convert to gray Image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Apply thresholding with a specified threshold value
threshold_value = 127  
max_value = 255  
_, threshold_img = cv2.threshold(grayImg, threshold_value, max_value, cv2.THRESH_BINARY)
# Display the original,gray and threshold images
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image",gray_img)
cv2.imshow("Thresholded Image", threshold_img)
cv2.waitKey(0)
