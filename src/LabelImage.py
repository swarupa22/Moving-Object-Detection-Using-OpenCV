import cv2
# Load the image
img = cv2.imread("cat.jpg")
# Define the text string
text = "cat"
# Specify the font properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.2
font_color = (0, 255, 0)  
thickness = 2
# Determine the position of the text
x = 100 
y = 50  
# Put the text on the image
cv2.putText(img, text, (x, y), font, font_scale, font_color, thickness)
# Display the image with the text
cv2_imshow(img)
cv2.waitKey(0)
cv2.destroyAllWindows()
