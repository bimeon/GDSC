try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = R'C:/Program Files (x86)/Tesseract-OCR/tesseract'

#print(pytesseract.image_to_string(Image.open('C:/Users/zrowx/OneDrive/바탕 화면/GitHub/GDSC/unnamed.png')))
print(pytesseract.image_to_string('C:/Users/zrowx/OneDrive/바탕 화면/GitHub/GDSC/unnamed.png'))

#print(pytesseract.get_languages(config=''))

print(pytesseract.image_to_string(Image.open('C:/Users/zrowx/OneDrive/바탕 화면/GitHub/GDSC/unnamed1.png'), lang='kor'))
