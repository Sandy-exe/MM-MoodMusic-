
import cv2
import os
from fer import FER
import webbrowser
import tkinter as tk                 
from tkinter import *
from tkinter import ttk
from pandas import DataFrame

from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog


Scaffold1=tk.Tk()
Scaffold1.geometry('1000x580')
frame1=tk.Frame(Scaffold1,bg='gray')
frame1.place(relwidth=1,relheight=1)


#emotion analysis
def emotion(file):
    img = cv2.imread(file)
    detector = FER(mtcnn=True)
    emotion, score = detector.top_emotion(img)
    print(emotion)

    ac_emotions=['happy','sad','neutral','fear']

    if emotion not in ac_emotions:
      print("Beep bop complex emotions we can't sugguest a playlist for ",emotion," yet")
    music_choice(emotion)  

print("ok")
i=0

def webcam():
    global file
    def takephoto():
        global i
        global frame1
        i=1
        img=show_frames()
        def retake():
            button14.destroy()
            button12.destroy()
            frame2.destroy()
            label3.destroy()
            button123.destroy()
            global i
            i=0
            webcam()
        def ok():
            button14.destroy()
            button12.destroy()
            frame2.destroy()
            label3.destroy()
            button123.destroy()
            global i
            i=0
            d='test.png'
            img.save(d)
            emotion(d)
            os.remove('test.png')
        label3=Label(frame1,text='PREVIEW', font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
        label3.place(relwidth=0.087, relheight=0.05,relx=0.7,rely=0.01)
        button12=tk.Button(frame1,text='RETAKE',command=retake, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
        button12.place(relwidth=0.087, relheight=0.05,relx=0.5,rely=0.8)
        button123=tk.Button(frame1,text='Ok',command=ok, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
        button123.place(relwidth=0.087, relheight=0.05,relx=0.6,rely=0.8)
    cam = cv2.VideoCapture(0)
    global frame1
    frame2=tk.Frame(frame1,bg='red')
    frame2.place(relwidth=0.58, relheight=0.63,relx=0.4,rely=0.08)
    label=Label(frame2,bg='yellow')
    label.place(relwidth=1,relheight=1)
    cap= cv2.VideoCapture(0)
    button14=tk.Button(frame1,text='TakePhoto',command=takephoto, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
    button14.place(relwidth=0.087, relheight=0.05,relx=0.5,rely=0.8)
    def show_frames():
        global i
        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)# Get the latest frame and convert into Image
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        if i==0:
            label.imgtk = imgtk
            label.configure(image=imgtk)
            label.after(20, show_frames)
        elif i==1:
            label.imgtk = imgtk
            label.configure(image=imgtk)
            return img
    show_frames()
def inp():
    sfile= tk.Tk()
    sfile.withdraw()
    Link=filedialog.askopenfilename(parent=sfile,initialdir=os.getcwd(),title="Please select a file:")
    img=Link
    emotion(img)
    
button1=tk.Button(frame1,text='OpenCAM',command=webcam, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
button1.place(relwidth=0.087, relheight=0.05,relx=0.2,rely=0.3)
button2=tk.Button(frame1,text='Attachfile',command=inp, font=('Times',13,'bold'),fg='snow', relief=RAISED, bd=4, bg='SpringGreen4')
button2.place(relwidth=0.087, relheight=0.05,relx=0.2,rely=0.4)

#function that links emotion to playlist
def music_choice(mood):
   if mood=='sad':
     print("You seem sad,remember \nEvery life has a measure of sorrow, and sometimes this is what awakens us.")
     webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx?si=_eIzJt8aQ12GhNf4QCmKTg")
   if mood=='neutral':
     print("You don't seem to happy,let's see a smile in that face.")
     webbrowser.open("https://open.spotify.com/playlist/6uTuhSs7qiEPfCI3QDHXsL")
   if mood=='happy':
      print("Now that is a happy face.")   
      webbrowser.open("https://open.spotify.com/playlist/1w5U47CbmVgcGqIHMxyIgE?si=wNTj68pDQOGWPLsz-LTowg&nd=1") 
   if mood=='fear':
      print("Wow you seem worried,remember\n Don't let the fear of striking out hold you back")
      webbrowser.open('https://open.spotify.com/playlist/7sjKKhdrYAG8w7Krapq6pK')  

Scaffold1.mainloop()