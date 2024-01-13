import tkinter as tk
from tkinter import BOTTOM, filedialog

from PIL import Image, ImageTk
import os
def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetype=(("JPG File",".jpg"),("PNG File","*.png")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
root = tk.Tk()
fram = tk.Frame(root)
fram.pack(side=BOTTOM,padx=15,pady=15)
lbl = tk.Label(root)
lbl.pack()
btn = tk.Button(fram, text ="Select Image", command=showimage)
btn.pack(side = tk.LEFT)
btn_2 = tk.Button(fram, text ="Exit", command = lambda:exit())
btn_2.pack(side=tk.LEFT,padx=12)

root.title("Image Viewer")
root.geometry("500x520")
root.mainloop()