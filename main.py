from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from people import People

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        #first
        img=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\1.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
        #second
        
        img1=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\2.png")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=540,height=130)
        #third
        
        img2=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\3.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        #background
        img3=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\bgg.jpg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SORTWARE",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        #button em
        img4=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\4.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.people_details)
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bg_img,text="Personal Info",command=self.people_details,cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)
        #face button
        img5=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\4.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)
        b2_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)
        #photo button
        img6=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\4.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)
        b3_1=Button(bg_img,text="Photo",cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)
        #traindata button
        img7=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\4.jpg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)
        b4_1=Button(bg_img,text="Train Data",cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)
        #quit button
        img8=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\exit.png")
        img8=img8.resize((110,110),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=1400,y=550,width=110,height=110)
        b5_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("time new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=1100,y=800,width=110,height=20)
        
    def people_details(self):
        self.new_window=Toplevel(self.root)
        self.app=People(self.new_window)
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()