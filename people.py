from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
class People:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #====variables===
        self.var_dep=StringVar()
        self.var_tickets=StringVar()
        self.var_service_pype=StringVar()
        self.var_flight_time=StringVar()
        self.var_peopleID=StringVar()
        self.var_people_name=StringVar()
        self.var_people_old=StringVar()
        self.var_people_sex=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_time_flight=StringVar()
        
        
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
        
        
        title_lbl=Label(bg_img,text="MANAGEMENT SYSTEM",font=("time new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=12,y=55,width=1500,height=650)
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="People Details",font=("time new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=720,height=580)
        
        
        img_left=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\3.jpg")
        img_left=img_left.resize((720,140),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=0,y=0,width=720,height=150)  
        
        #current course
        Current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course infomation",font=("time new roman",12,"bold"))
        Current_course_frame.place(x=10,y=135,width=720,height=150)
        
        #deparment
        dep_label=Label(Current_course_frame,text="Deparmnet",font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        search_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_dep,font=("time new roman",12,"bold"),width=17,state="readonly")
        search_combo["values"]=("Select Deparment","Inland","International")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #Select tickets
        tickets_label=Label(Current_course_frame,text="Tickets",font=("time new roman",12,"bold"),bg="white")
        tickets_label.grid(row=1,column=0,padx=10,sticky=W)
        
        tickets_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_tickets,font=("time new roman",12,"bold"),width=17,state="readonly")
        tickets_combo["values"]=("Select Tickets","Round Trip","One-way Trip")
        tickets_combo.current(0)
        tickets_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
       
        #Select service type
        service_label=Label(Current_course_frame,text="Service",font=("time new roman",12,"bold"),bg="white")
        service_label.grid(row=0,column=2,padx=10,sticky=W)
        
        service_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_service_pype,font=("time new roman",12,"bold"),width=17,state="readonly")
        service_combo["values"]=("Select Service","General Ticket","Business Ticket")
        service_combo.current(0)
        service_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
       
        #Select flight time
        flight_label=Label(Current_course_frame,text="Flight Time",font=("time new roman",12,"bold"),bg="white")
        flight_label.grid(row=1,column=2,padx=10,sticky=W)
        
        flight_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_flight_time,font=("time new roman",12,"bold"),width=17,state="readonly")
        flight_combo["values"]=("Select Flight Time","Morning","Afternoon","Evening")
        flight_combo.current(0)
        flight_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        #class people infomation
        class_people_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class People Infomation",font=("time new roman",12,"bold"))
        class_people_frame.place(x=10,y=260,width=720,height=300)
        #peopleID
        peopleID_label=Label(class_people_frame,text="PeopleID:",font=("time new roman",12,"bold"),bg="white")
        peopleID_label.grid(row=0,column=0,padx=10,sticky=W)
        
        peopleID_entry=ttk.Entry(class_people_frame,textvariable=self.var_peopleID,width=20,font=("time new roman",12,"bold"))
        peopleID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        #people name
        people_name_label=Label(class_people_frame,text="People Name:",font=("time new roman",12,"bold"),bg="white")
        people_name_label.grid(row=0,column=2,padx=10,sticky=W)
        
        people_name_entry=ttk.Entry(class_people_frame,textvariable=self.var_people_name,width=20,font=("time new roman",12,"bold"))
        people_name_entry.grid(row=0,column=3,padx=10,sticky=W)
        
        #people old
        people_old_label=Label(class_people_frame,text="People Old:",font=("time new roman",12,"bold"),bg="white")
        people_old_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        people_old_entry=ttk.Entry(class_people_frame,textvariable=self.var_people_old,width=20,font=("time new roman",12,"bold"))
        people_old_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        
        #people sex
        people_sex_label=Label(class_people_frame,text="People Sex:",font=("time new roman",12,"bold"),bg="white")
        people_sex_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)
        
        people_sex_combo=ttk.Combobox(class_people_frame,textvariable=self.var_people_sex,font=("time new roman",12,"bold"),width=17,state="readonly")
        people_sex_combo["values"]=("Select People Sex","Man","Women")
        people_sex_combo.current(0)
        people_sex_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        
        #email
        email_label=Label(class_people_frame,text="Email:",font=("time new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        email_entry=ttk.Entry(class_people_frame,textvariable=self.var_email,width=20,font=("time new roman",12,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
        
        #phone
        phone_label=Label(class_people_frame,text="Phone:",font=("time new roman",12,"bold"),bg="white")
        phone_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        
        phone_entry=ttk.Entry(class_people_frame,textvariable=self.var_phone,width=20,font=("time new roman",12,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)
        
        #address
        address_label=Label(class_people_frame,text="Address:",font=("time new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        
        address_entry=ttk.Entry(class_people_frame,textvariable=self.var_address,width=20,font=("time new roman",12,"bold"))
        address_entry.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        #time flight
        people_sex_label=Label(class_people_frame,text="Time Flight:",font=("time new roman",12,"bold"),bg="white")
        people_sex_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        
        people_sex_combo=ttk.Combobox(class_people_frame,textvariable=self.var_time_flight,font=("time new roman",12,"bold"),width=17,state="readonly")
        people_sex_combo["values"]=("Select Time Flight","0-4h","4-8h","8-12h","12-16h","16-20h","20-24h")
        people_sex_combo.current(0)
        people_sex_combo.grid(row=3,column=3,padx=10,pady=10,sticky=W)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_people_frame,textvariable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_people_frame,textvariable=self.var_radio2,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        #button frame
        btn_frame=Frame(class_people_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)       
        
        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)       
        
        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)       
        
        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)       
        
        
        btn_frame1=Frame(class_people_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=45)
        
        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)       
        
        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)       
        
         
        
        
        
        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="People Details",font=("time new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=720,height=580)
        
        
        img_right=Image.open(r"E:\linh\pythoncoban\MiAI_FaceRecog_3-main\Icon\images\4.jpg")
        img_right=img_right.resize((700,130),Image.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=8,y=0,width=700,height=130) 
        
        #search system
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        Search_frame.place(x=3,y=135,width=710,height=70)
        
        search_label=Label(Search_frame,text="Search By:",font=("time new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("time new roman",12,"bold"),width=10,state="readonly")
        search_combo["values"]=("Select","Id","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=20,font=("time new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)       
        
        showAL_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAL_btn.grid(row=0,column=4)  
        
        #=======table frame=======
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=210,width=710,height=250)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.people_table=ttk.Treeview(table_frame,columns=("dep","tickets","service_pype","flight_time","peopleID","people_name","people_old","people_sex","email","phone","address","time_flight"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.people_table.xview)
        
        scroll_y.config(command=self.people_table.yview)
        self.people_table.heading("dep",text="Department")
        self.people_table.heading("tickets",text="Tickets")
        self.people_table.heading("service_pype",text="Service")
        self.people_table.heading("flight_time",text="Flight Time")
        self.people_table.heading("peopleID",text="PeopleID")
        self.people_table.heading("people_name",text="People Name:")
        self.people_table.heading("people_old",text="People Old:")
        self.people_table.heading("people_sex",text="People Sex:")
        self.people_table.heading("email",text="Email:")
        self.people_table.heading("phone",text="Phone:")
        self.people_table.heading("address",text="Address:")
        self.people_table.heading("time_flight",text="Time Flight:")
      
        
        
        self.people_table["show"]="headings"
        
        self.people_table.column("dep",width=100)
        self.people_table.column("tickets",width=100)
        self.people_table.column("service_pype",width=100)
        self.people_table.column("flight_time",width=100)
        self.people_table.column("peopleID",width=100)
        self.people_table.column("people_name",width=100)
        self.people_table.column("people_old",width=100)
        self.people_table.column("people_sex",width=100)
        self.people_table.column("email",width=100)
        self.people_table.column("phone",width=100)
        self.people_table.column("address",width=100)
        self.people_table.column("time_flight",width=100)
        
        self.people_table.pack(fill=BOTH,expand=1)
        
        
    #=====function decration
    
    def add_data(self):
        if self.var_dep.get()=="Select Deparment" or self.var_people_name.get()=="" or self.var_peopleID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            messagebox.showinfo("success","Welcome ray mais botws")
if __name__=="__main__":
    root=Tk()
    obj=People(root)
    root.mainloop()