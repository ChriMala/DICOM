import tkinter as tk
from tkinter import filedialog
import pydicom 
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os
from vedo import load,show

class Data:

    ind = 0

#passa all'immagine prima (se è la prima immagine, salta all'ultima)

    def prev(self, event):
        if not self.ind:
            self.ind = len(files) - 1
        else:
            self.ind -= 1
        self.openImage()

#passa all'immagine dopo (se è l'ultima immagine, salta alla prima)

    def next(self, event):
        if self.ind == len(files) - 1:
                self.ind = 0
        else:
            self.ind += 1
        self.openImage()

#scelta cartella con le immagini

    def chooseFolder(self, event):
        plt.close()
        self.ind = 0 
        global dir 
        dir = filedialog.askdirectory(initialdir = os.path.dirname(__file__) + "\\Pseudo-PHI-DICOM-Data")
        global files 
        files = os.listdir(dir)

    #creazione pulsanti

        axprev = plt.axes([0.850, 0.870, 0.140, 0.075])
        axnext = plt.axes([0.850, 0.785, 0.140, 0.075])
        axfold = plt.axes([0.850, 0.700, 0.140, 0.075])
        ax3d   = plt.axes([0.850, 0.615, 0.140, 0.075])
        axexit = plt.axes([0.850, 0.530, 0.140, 0.075])

        bprev = Button(axprev,"Precedente")
        bnext = Button(axnext,"Successiva")
        bfold = Button(axfold,"Cartella")
        b3d   = Button(ax3d,"3D")
        bexit = Button(axexit,"Esci")

    #associazione funzione ad ogni pulsante

        bprev.on_clicked(self.prev)
        bnext.on_clicked(self.next)
        bfold.on_clicked(self.chooseFolder)
        b3d.on_clicked(self.plot3D)
        bexit.on_clicked(self.exit)

        self.openImage()

#apre l'immagine

    def openImage(self):
        image = pydicom.dcmread(dir + "\\" + files[self.ind])

        plt.axes([0.05,0.1,0.75,0.75])
        plt.imshow(image.pixel_array, cmap = plt.cm.bone)
    
        plt.show()
        
#crea un volume 3d da una cartella di immagini

    def plot3D(self, event): 
        plt.close()
        show(load(dir), bg = 'white')
        
#termina l'esecuzione

    def exit(self, event): 
        plt.close()
        exit()

indice = Data()

root = tk.Tk()
root.withdraw() #cancella la finestra di dialogo iniziale
indice.chooseFolder(1)