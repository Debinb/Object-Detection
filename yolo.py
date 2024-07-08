import cv2
import numpy as np 
import torch
from ultralytics import YOLO
import os

print(torch.backends.mps.is_available())
model = YOLO("yolov8m.pt")

video_dir = '/workspaces/Object-Detection/'
video_path = '/workspaces/Object-Detection/test.mp4' 