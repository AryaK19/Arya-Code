import numpy as np
import cv2 as cv 
import mediapipe as mp
from Function import *

holy_drawing = mp.solutions.drawing_utils
holy_drawing_styles = mp.solutions.drawing_styles
holy_hands = mp.solutions.hands
#holy_shit


cap = cv.VideoCapture(0)
with holy_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
   while cap.isOpened():
     success, image = cap.read()
     if not success:
       print("Ignoring empty camera frame.")
       continue

     # To improve performance, optionally mark the image as not writeable to
     # pass by reference.
     image.flags.writeable = False
     image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
     results = hands.process(image)

     # Draw the hand annotations on the image.
     image.flags.writeable = True
     image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
     # Images shape
     imgH,imgW=image.shape[:2]
     if results.multi_hand_landmarks:
       for hand_landmarks in results.multi_hand_landmarks:
         # Get cordinates
         hand_cordinate=[]
         for ids , landmark in enumerate(hand_landmarks.landmark):
            x_cordinate , y_cordinate = int(landmark.x*imgW) , int(landmark.y*imgH)
            hand_cordinate.append([ids,x_cordinate,y_cordinate])
         '''
         holy_drawing.draw_landmarks(
            image,
            hand_landmarks,
            holy_hands.HAND_CONNECTIONS,
            holy_drawing_styles.get_default_hand_landmarks_style(),
            holy_drawing_styles.get_default_hand_connections_style())
         '''
         string=persons_input(hand_cordinate)
         image=get_fram(image,hand_cordinate,string)
     # Flip the image horizontally for a selfie-view display.
     cv.imshow('MediaPipe Hands', cv.flip(image,1))

     if cv.waitKey(5) & 0xFF == ord('x'):
       break
cap.release()
