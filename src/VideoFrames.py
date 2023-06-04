#Define a function to resize 
def resize(img):
 return cv2.resize(img,(512,512))    
#Load Frames 
import cv2
# Open the video file
vs = cv2.VideoCapture('video.mp4')
while True: 
    # Read the next frame
    ret, frame = vs.read()
    # Display the frame
    cv2.imshow(resize(frame))
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the video file and close all windows
vs.release()
cv2.destroyAllWindows()
