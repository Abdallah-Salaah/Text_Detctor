import cv2
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\Tesseract.exe'
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

img = cv2.imread("jcr_content1.jpg")

#Extract text from image
text = pytesseract.image_to_string(img)
print(text)

# create a text file
file = open("output.txt", "w+")
file.write("")
file.close()

# Open the file in append mode
file = open("output.txt", "a")
# Appending the text into file
file.write(text)
file.write("\n")
# Close the file
file.close