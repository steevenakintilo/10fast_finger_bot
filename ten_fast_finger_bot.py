import pyautogui
import time

from PIL import Image
from pytesseract import pytesseract

def take_screen():
    im1 = pyautogui.screenshot()  # return an image object
    im2 = pyautogui.screenshot('my_screenshot.png' , region = (300,350,1220,150))  # image name will be as per parameter

def pic_to_text():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"my_screenshot.png"
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    main_text = text[:-1]
    return (main_text)
    #print(main_text)

time.sleep(5)
take_screen()
text = pic_to_text()

for j in range(10):
    for i in range(len(text)):
        if text[i].isalpha() == True:
            pyautogui.write(text[i])
        else:
            pyautogui.press('space')
        if i == len(text) - 1:
            pyautogui.press('space')
            take_screen()
            text = pic_to_text()
            print(text)