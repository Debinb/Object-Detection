import cv2
import numpy as np 
import torch
from ultralytics import YOLO
import os
   
def main(): 
    # Open the default webcam  
    cap = cv2.VideoCapture(0) 
      
    while True: 
        # Read a frame from the webcam 
        ret, frame = cap.read() 
        if not ret: 
            print('Image not captured') 
            break
          
        # Perform Canny edge detection on the frame 
        blurred, edges = canny_edge_detection(frame) 
          
        # Display the original frame and the edge-detected frame 
        #cv2.imshow("Original", frame) 
        cv2.imshow("Blurred", blurred) 
        cv2.imshow("Edges", edges) 
          
        # Exit the loop when 'q' key is pressed 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
      
    # Release the webcam and close the windows 
    cap.release() 
    cv2.destroyAllWindows()