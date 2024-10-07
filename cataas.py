from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

from pygame.examples.sprite_texture import load_img
from будильник import window, label

window = Tk()
window.title("Cats")
window.geometry("600x480")

label = Label()
label.pack()

url = "http://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
