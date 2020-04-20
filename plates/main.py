import pathlib

from plates.plateTools import *
import sys
import os
import tkinter as tk
from PIL import Image, ImageTk
from matplotlib.colors import rgb2hex

##arguments = sys.argv[1:]


current_folder = pathlib.Path().absolute()
images_folder = pathlib.Path.joinpath(current_folder, "images")
testImage_1 = os.path.join(images_folder, "img7.jpg")

img = openImage(testImage_1)
imgNonCv2 = Image.fromarray(img)


###place for Neural net #1

###place for neuralnet #2


'''
after nn#2 get data:
function to get gountry from csv
fun to get rows

plateInfo={
    "Country" : "",
    "has2rows": True,
    "TopRowText": "123",
    "BottomRowText": "456",
}
'''

# window
window = tk.Tk()
window.title("Detekcja tablic rejestracyjnych")
frame = tk.Frame(window)

im = Image.fromarray(img)
ph = ImageTk.PhotoImage(im)
imageLeft = tk.Label(window, image=ph)
imageLeft.grid(column=0, rowspan=10)

spacerLabel = tk.Label(text="       ")
spacerLabel.grid(column=1, row=0)

dataForRightPanel = {
    "bgColor": rgb2hex(getColorsInPlate(img)[0] / 255),
    "fgColor": rgb2hex(getColorsInPlate(img)[1] / 255),
    "country": "PL",  # TODO
    "row1": "123",  # TODO
    "row2": "456"  # TODO

}

eurobandLabel = tk.Label(text=dataForRightPanel["country"], bg="blue", fg="white")
eurobandLabel.grid(column=2, row=0)

toprowLabel = tk.Label(text=dataForRightPanel["row1"], bg=dataForRightPanel["bgColor"], fg=dataForRightPanel["fgColor"])
toprowLabel.grid(column=3, row=0)

bottomrowLabel = tk.Label(text=dataForRightPanel["row1"], bg=dataForRightPanel["bgColor"],
                          fg=dataForRightPanel["fgColor"])
bottomrowLabel.grid(column=3, row=1)

spacer2Label = tk.Label(text="       ")
spacer2Label.grid(column=4, row=0)

bgColorLabel = tk.Label(text="Kolor tła tablicy: ")
bgColorLabel.grid(column=5, row=0)

bgColorValLabel = tk.Label(text="         ", bg=dataForRightPanel["bgColor"])
bgColorValLabel.grid(column=6, row=0)

###
fgColorLabel = tk.Label(text="Kolor tekstu tablicy: ")
fgColorLabel.grid(column=5, row=1)

bgColorValLabel = tk.Label(text="         ", bg=dataForRightPanel["fgColor"])
bgColorValLabel.grid(column=6, row=1)

###

countryLabel = tk.Label(text="Kraj")
countryLabel.grid(column=5, row=2)

countryValLabel = tk.Label(text=dataForRightPanel["country"])
countryValLabel.grid(column=6, row=2)




tk.mainloop()
window.pack()
