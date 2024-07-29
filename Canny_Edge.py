import cv2
import numpy as np

# capture frames from a camera
cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     return

# loop runs if capturing has been initialized
while(1):
    # reads frames from a camera
    ret, frame = cap.read()
    if not ret: 
            print('Image not captured') #Debugging
            break
    
    # Display an original image
    cv2.imshow('Original',frame)

    # finds edges in the input image and marks them in the output map edges
    # 100 and 200 are the bounds of change in gradients that qualify as edges
    edges = cv2.Canny(frame,100,200)

    # Display edges in a frame
    cv2.imshow('Edges',edges)

    # Press Esc key to exit
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close the window
cap.release()
cv2.destroyAllWindows()