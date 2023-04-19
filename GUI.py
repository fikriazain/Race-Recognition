from random import random
import tkinter as tk
from tkinter import DISABLED, END, N, NW, Frame, Label, Text, Toplevel, ttk
from tkinter import filedialog
import tkinter
from numpy import size
import numpy as np
from pyrsistent import s
import random
from keras.models import load_model
from PIL import ImageTk, Image
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import tensorflow as tf




class App():
    def __init__(self, master):
        self.master = master
        myFrame = Frame(master)
        myFrame.pack()

        self.label = Label(myFrame, text = "Race Recognition Prototype", font=('Helvatical bold',20))
        self.label.pack(pady=10)

        self.textField = tk.Entry(master, bg='white', width=50)
        self.textField.config(state='readonly')
        self.button = ttk.Button(text = "Browse A File",command = self.fileDialog)
        self.button2 = ttk.Button(text = "Go!",command = lambda: self.goButton(self.textField.get()))
        self.button.pack(side=tk.LEFT, anchor=NW)
        self.textField.pack(side=tk.TOP, anchor=NW)
        self.button2.pack(side=tk.TOP, anchor=N)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("jpeg files","*.jpg"),("all files","*.*")) )
        self.textField.config(state='normal', background='white')
        self.textField.insert(0,self.filename)
        self.textField.config(state='readonly')
    
    def goButton(self, text=None):
        self.textField.config(state='normal')
        self.textField.delete(0, END)
        self.textField.config(state='readonly')
        global myImage
        print(text)
        model = keras.models.load_model("C:/Users/Azyain/OneDrive/Documents/DS Project Jupyter/Face Detection/my_model.h5")
        img = image.load_img(text, target_size=(299,299,3))
        X = image.img_to_array(img)
        X = np.expand_dims(X, axis=0)
        images = np.vstack([X])
        pred = model.predict(images)
        print(pred)
        if(pred == 0):
            arab = ['I\'m rich', 'Sorban is my fashion', 'I have a tiger and eagle as my pets']
            newWindow = Toplevel()
            newWindow.title("Alhamdulillah Arab~")
            newWindow.geometry("400x400")
            img= (Image.open(text))
            resized_image= img.resize((299,299), Image.ANTIALIAS)
            myImage = ImageTk.PhotoImage(resized_image)
            mylabel = Label(newWindow, image=myImage).pack(fill="both")
            mylabel = Label(newWindow, text="ARAB", font=(20)).pack(fill="both", pady='10px')
            mylabel = Label(newWindow, text=random.choice(arab)).pack(fill="both", pady='5px')
        else:
            asian = ['Races that eat dogs and cats', 'Small dick, i have', 'I love rice']
            newWindow = Toplevel()
            newWindow.title("Fucking Asian")
            newWindow.geometry("400x400")
            img= (Image.open(text))
            resized_image= img.resize((299,299), Image.ANTIALIAS)
            myImage = ImageTk.PhotoImage(resized_image)
            mylabel = Label(newWindow, image=myImage).pack(fill="both")
            mylabel = Label(newWindow, text="ASIAN", font=(20)).pack(fill="both", pady='10px')
            mylabel = Label(newWindow, text=random.choice(asian)).pack(fill="both", pady='5px')



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x150")
    app = App(root)
    root.mainloop()