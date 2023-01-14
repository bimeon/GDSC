from PIL import Image
import pytesseract

img_eng = Image.open('unnamed_eng.png')
img_kor = Image.open('unnamed_kor.jpeg')

text_eng = pytesseract.image_to_string(img_eng)
text_kor = pytesseract.image_to_string(img_kor, lang='kor')

print(text_eng)
print(text_kor)
