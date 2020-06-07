import os

import PIL
from PIL import Image, ImageTk
from tkinter import *
from tkinter import filedialog

from PredictCharacters import predict_license_plate_number
from TrainRecognizeCharacters import train

dir_name = 'output'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
else:
    filelist = [f for f in os.listdir(dir_name) if f.endswith(".png")]
    for f in filelist:
        os.remove(os.path.join(dir_name, f))

if not os.path.exists('finalized_model.sav'):
    train()

def nove_dimenzije(dimenzije):
    sirina = dimenzije[0]
    visina = dimenzije[1]
    zeljena_sirina = 250
    t = (zeljena_sirina, int((visina / sirina) * zeljena_sirina))
    print(t)
    return t


def clicked():

    filelist = [f for f in os.listdir('output') if f.endswith(".png")]
    for f in filelist:
        os.remove(os.path.join('output', f))

    file = filedialog.askopenfilename(initialdir=f"{__file__}/samples/", filetypes=(("JPG", "*.jpg"), ("PNG", "*.png")))
    plate_string, rightplate_string = predict_license_plate_number(file)
    images = next(os.walk('output'))[2]
    lbl1 = Label(window, text=F"Pronađeni karakteri su: {plate_string}")
    lbl2 = Label(window, text=F"Pravilno poredani karakteri su: {rightplate_string}")
    lbl1.grid(column=0, row=3)
    lbl2.grid(column=0, row=6)
    x_coord = 180
    y_coord = 290
    for i, image in enumerate(images):
        img = PIL.Image.open(f"output/output_{i}.png")
        img = img.resize(nove_dimenzije(img.size))
        img = ImageTk.PhotoImage(img)
        panel = Label(window, image=img)
        panel.image = img
        panel.place(x=x_coord, y=y_coord, anchor=CENTER)
        if i % 2 == 0:
            x_coord = x_coord + 270
        else:
            y_coord = y_coord + 270
            x_coord = 180


window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('800x1000')

lbl = Label(window, text="Odaberite sliku sa koje želite prepoznati registracijsku oznaku ")

lbl.grid(column=0, row=0)

btn = Button(window, text="Click Me", command=clicked)

btn.grid(column=1, row=0)

window.mainloop()
