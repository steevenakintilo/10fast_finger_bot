import pyautogui
import time

from PIL import Image
from pytesseract import pytesseract
import sys

def take_screen():
    im1 = pyautogui.screenshot()  # return an image object
    im2 = pyautogui.screenshot('my_screenshot.png' , region = (200,220,1200,250))  # image name will be as per parameter

def pic_to_text():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"my_screenshot.png"
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(img)
    main_text = text[:-1]
    return (main_text)
    #print(main_text)

def slow_bot(time_to_sleep):
    time.sleep(5)
    take_screen()
    text = pic_to_text()
    t = text.split(" ")
    print(t)
    print(len(t),len(text))
    #time.sleep(1000)
    for j in range(10):
        for i in range(len(text)):
            if text[i].isalpha() == True:
                pyautogui.write(text[i])
                time.sleep(time_to_sleep)
            else:
                pyautogui.press('space')
            if i == len(text) - 1:
                pyautogui.press('space')
                take_screen()
                text = pic_to_text()
                print(text)
            if "Result" in text:
                quit()
def fast_bot(time_to_sleep):
    time.sleep(5)
    take_screen()
    text = pic_to_text()
    text = text.replace('\n',' ')
    t = text.split(" ")
    print(t)
    print(len(t),len(text))
    #time.sleep(1000)
    for j in range(15):
        for i in range(len(t)):
            pyautogui.write(t[i])
            pyautogui.press('space')
            time.sleep(time_to_sleep)
            if i == len(t) - 1:
                #time.sleep(0.01)
                pyautogui.press('space')
                take_screen()
                text = pic_to_text()
                text = text.replace('\n',' ')
                t = text.split(" ")
                print(text)
            if "Result" in t:
                    quit()
fast_bot(0)