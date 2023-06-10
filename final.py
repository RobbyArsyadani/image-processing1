from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from PIL import Image, ImageTk
import cv2 as cv
import numpy as np

class GUI (Frame):
    img = None
    img_is_found = False

    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.label1 = Label(image=None,width=200,height=200)
        self.label = Label(image=None,width=400,height=40)
        self.file = Button(self, width=13, text="Upload image", command=self.choose)
        self.low_contrast =Button(self, width=13, text='low contrast', command=self.lowContrast)
        self.negative_trans = Button(self, width=13, text='Negative Trans', command=self.negativeTrans)
        self.flip_image_verti = Button(self, width=13, text='flip vertically', command=self.flip_verti)
        self.flip_image_hori = Button(self, width=13, text='flip horizontally', command=self.flip_hori)
        self.rotate_image = Button(self, width=13, text='rotate', command=self.rotate)
        self.scaling_image = Button(self, width=13, text='scaling', command=self.scaling)
        self.sharp_image = Button(self, width=13, text='sharpen', command=self.sharpen)
        self.grayscale_image = Button(self, width=13, text='grayscale', command=self.grayscale)
        self.denoise_image = Button(self, width=13, text='denoise', command=self.denoise)
        self.reset_image = Button(self, width=13, text='reset', command=self.reset)
        self.save_file = Button(self, width=13, text='save', command=self.save)
    
        self.place()
        self.grid()
        self.file.grid(row=1,column=1, pady=(20,5), padx=20)
        self.low_contrast.grid(row=2,column=1, pady=5, padx=20)    
        self.negative_trans.grid(row=3,column=1, pady=5, padx=20)    
        self.flip_image_verti.grid(row=4,column=1, pady=5, padx=20)
        self.flip_image_hori.grid(row=5,column=1, pady=5, padx=20)
        self.grayscale_image.grid(row=6,column=1, pady=5, padx=20)
        self.denoise_image.grid(row=7,column=1, pady=5, padx=20)
        self.rotate_image.grid(row=8,column=1, pady=5, padx=20)
        self.scaling_image.grid(row=9,column=1, pady=5, padx=20)
        self.sharp_image.grid(row=10,column=1, pady=5, padx=20)
        self.reset_image.grid(row=11,column=1, pady=5, padx=20)
        self.save_file.grid(row=12,column=1, pady=5, padx=20)
        self.label1.place(x=400, y=150)
        self.label.place(x=600, y= 50)


    def choose(self):
        f_types = [('Jpeg Files', '*.jpeg'),('PNG Files','*.png'),('Jpg Files', '*.jpg')]
        ifile = filedialog. askopenfile(parent=self, filetypes=f_types, title='choose file',mode='rb')
        if ifile:
            path = Image.open(ifile)
            path = path.resize((200,200))
            self.image2 = ImageTk.PhotoImage(path)
            self.label1.configure(image=self.image2)
            self.label.configure(image=self.image2)
            self.label1.image = self.image2
            self.label.image = self.image2
            self.img = np.array(path)
            self.img = self.img
            self.img_is_found = True

    def lowContrast(self):
        if self.img_is_found:
            img_after = change_contrast(self.img, 0.5, 10)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
   
    def negativeTrans(self):
        if self.img_is_found:
            img_after = negative_trans(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def flip_verti(self):
        if self.img_is_found:
            img_after = flip_verti(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def flip_hori(self):
        if self.img_is_found:
            img_after = flip_hori(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def rotate(self):
        if self.img_is_found:
            img_after = rotate_trans(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
   
    def scaling(self):
        if self.img_is_found:
            img_after = scaling_trans(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    
    def sharpen(self):
        if self.img_is_found:
            img_after = sharpen_image(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def grayscale(self):
        if self.img_is_found:
            img_after = grayscale_image(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def denoise(self):
        if self.img_is_found:
            img_after = denoise_image(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after
    
    def reset(self):
        if self.img_is_found:
            img_after = reset_img(self.img)
            img_after = ImageTk.PhotoImage(Image.fromarray(img_after))
            self.label.configure(image=img_after)
            self.label.image = img_after

    def save(self):
            
             a = Image.open(self.img)
             c = Image.fromarray(a)
             c = ImageTk.PhotoImage(c)
             f_types = [('Jpeg Files', '*.jpeg'),('PNG Files','*.png'),('Jpg Files', '*.jpg')] 
             filename = filedialog.asksaveasfile(mode = 'w',filetypes = f_types, defaultextension = f_types)
             if not filename:
                return
             c.save(filename)
             

def reset_img(img):
    
    reset = img

    return reset

def negative_trans(img):
    height, width, _ = img.shape
  
    for i in range(0, height - 1):
        for j in range(0, width - 1):
            pixel = img[i, j]
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
            img[i, j] = pixel      
    return img
    

def change_contrast(img, alpha, beta):  
    for y in range (img.shape[0]):
        for x in range(img.shape[1]):
            for c in range(img.shape[2]):
                img[y, x, c] = np.clip(alpha * img[y, x, c] * beta, 0, 255)
    return img           

def flip_verti(img):
    img = cv.flip(img,0)
    
    return img

def flip_hori(img):
    img = cv.flip(img,1)
    
    return img

def rotate_trans(img):
    
    rows, cols, _ = img.shape

    D = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
    dsa = cv.warpAffine(img,D,(cols,rows))
    return dsa

def scaling_trans(img):
    res = cv.resize (img,None, fx = 2, fy = 2, interpolation=cv. INTER_CUBIC)
    return res

def sharpen_image(img):
    kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    image_sharp = cv.filter2D(src=img, depth=-1, kernel=kernel)
    return image_sharp

def grayscale_image(img):
    grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return grayscale

def denoise_image(img):
    dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    return dst

def save_file(img):
    i = cv.imread(img)
    return i






root = Tk() 
root.title("Image Processing")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+8" % (w, h))

gui = GUI(root)
gui.mainloop() 