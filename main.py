import tkinter as tk
from tkinter import filedialog
import pydicom 
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os
from vedo import load,show

class Data:
    ind = 0

    def prev(self, event):
        if not self.ind:
            self.ind = len(files) - 1
        else:
            self.ind -= 1
        self.openImage()

    def next(self, event):
        if self.ind == len(files) - 1:
                self.ind = 0
        else:
            self.ind += 1
        self.openImage()

    def chooseFolder(self, event):
        plt.close()
        self.ind = 0 
        global dir 
        dir = filedialog.askdirectory(initialdir = "https://github.com/ChriMala/DICOM/tree/main/Pseudo-PHI-DICOM-Data")
        global files 
        files = os.listdir(dir)

        axprev = plt.axes([0.850, 0.870, 0.140, 0.075])
        axnext = plt.axes([0.850, 0.785, 0.140, 0.075])
        axsel  = plt.axes([0.850, 0.700, 0.140, 0.075])
        axfold = plt.axes([0.850, 0.615, 0.140, 0.075])
        ax3d   = plt.axes([0.850, 0.530, 0.140, 0.075])
        axexit = plt.axes([0.850, 0.445, 0.140, 0.075])

        bprev = Button(axprev,"Precedente")
        bnext = Button(axnext,"Successiva")
        bsel  = Button(axsel,"Seleziona")
        bfold = Button(axfold,"Cartella")
        b3d   = Button(ax3d,"3D")
        bexit = Button(axexit,"Esci")

        bprev.on_clicked(self.prev)
        bnext.on_clicked(self.next)
        bfold.on_clicked(self.chooseFolder)
        b3d.on_clicked(self.plot3D)
        bexit.on_clicked(self.exit)

        self.openImage()
        
    def openImage(self):
        image = pydicom.dcmread(dir + "\\" + files[self.ind])

        plt.axes([0.05,0.1,0.75,0.75])
        plt.imshow(image.pixel_array, cmap = plt.cm.bone)
    
        plt.show()

    def exit(self, event):
        plt.close()
        exit()

    def plot3D(self, event):
        plt.close()
        show(load(dir), bg = 'white')


indice = Data()

root = tk.Tk()
root.withdraw()

#dir = filedialog.askdirectory(initialdir = "C:\\Users\\chrim\\Desktop\\dicom\\Pseudo-PHI-DICOM-Data")
#files = os.listdir(dir)


indice.chooseFolder(1)
