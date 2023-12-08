from ultralytics import YOLO
from torchvision import transforms
import cv2
import os
import math
import torch
import numpy as np


os.environ['KMP_DUPLICATE_LIB_OK']='True'

CONFIDENCE_THRESHOLD = 0.6
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

model = YOLO('yolov8n-pose.pt')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:        
        
        detection = model(frame)[0]

        for data in detection.boxes.data.tolist(): # data : [xmin, ymin, xmax, ymax, confidence_score, class_id]
            confidence = float(data[4])
            if confidence < CONFIDENCE_THRESHOLD:
                continue
            
            

            xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            label = int(data[5])
            
            left_shoulder_x, left_shoulder_y = detection.keypoints.xy[0][5]
            right_shoulder_x, right_shoulder_y = detection.keypoints.xy[0][6]
            left_hip_x, left_hip_y = detection.keypoints.xy[0][11]
            right_hip_x, right_hip_x = detection.keypoints.xy[0][12]
            left_ankle_x, left_ankle_y = detection.keypoints.xy[0][15]
            right_ankle_x, right_ankle_y = detection.keypoints.xy[0][16]
            
            len_factor = math.sqrt(((left_shoulder_y - left_hip_y)**2 + (left_shoulder_x - left_hip_x)**2 ))
            if left_shoulder_x > 0 and right_shoulder_x > 0 and left_hip_x > 0 and right_hip_x > 0 :
            
                if left_shoulder_y > left_ankle_y - len_factor and left_hip_y > left_ankle_y - (len_factor / 2) and left_shoulder_y > left_hip_y - (len_factor / 2):
                #Plotting key points on Image
                    cv2.rectangle(frame,(int(xmin), int(ymin)),(int(xmax), int(ymax)),color=(0, 0, 255),
                        thickness=5,lineType=cv2.LINE_AA)
                    cv2.putText(frame, 'Person Fell down', (11, 100), 0, 1, [0, 0, 2550], thickness=3, lineType=cv2.LINE_AA)
                    fall_detected = True


        cv2.imshow('frame', frame)

    # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()