import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image and convert it to grayscale
img = Image.open(os.path.join('images', "Screenshot 2023-03-17 223042.png")).convert('L')

# get width and height of image
width, height = img.size
tile_width = width/4
tile_height = height/4
text = ""

# Use pytesseract to extract the text from the image
for i in range(4):
    for j in range(4):
        text += pytesseract.image_to_string(
            img.crop((i*tile_width, j*tile_height, (i + 1)*tile_width, (j + 1)*tile_height)), config='--psm 10')

# print(text)

# Remove all non-letter characters from the text and convert to lowercase
letters = ''.join(filter(str.isalpha, text)).lower()

#     print(letters)
