import pytesseract
import cv2
import os
from PIL import Image
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt


path = "/content/drive/MyDrive/ML_data/picture01.PNG"

if os.path.exists(path):
     img = cv2.imread(path)
else:
     print("Path does not exist:", path)

#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


text = pytesseract.image_to_string(img, lang = 'eng')
