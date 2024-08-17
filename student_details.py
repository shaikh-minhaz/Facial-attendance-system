#file_name- student_details.py
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import cv2
import os


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.title("FACIAL ATTENDANCE RECOGNITION SYSTEM")
        self.cap = cv2.VideoCapture(0)


        # ===================variables=============
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_phone=StringVar()
        self.var_bat=StringVar()
        self.var_com_search=StringVar()
        self.var_search_input = StringVar()
        self.var_search_combo = StringVar()


        # img1
        img1 = Image.open(r"C:\Users\Macbook Air\Anti Spoofing\imgs\ss.jpg")
        img1 = img1.resize((1440, 400), Image.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=-280, width=1440, height=400)


        # backgroundimage
        bgimg = Image.open(r"C:\Users\Macbook Air\Anti Spoofing\imgs\ib1.jpg")
        bgimg = bgimg.resize((1440, 800), Image.BICUBIC)
        self.photobgimg = ImageTk.PhotoImage(bgimg)

        bg_img = Label(self.root, image=self.photobgimg)
        bg_img.place(x=0, y=120, width=1430, height=800)

        # title
        heading = Label(bg_img, text="CLASS DETAILS", font=("Exotc350 DmBd BT", 35, "bold"), bg="black", fg="white")
        heading.place(x=-5, y=-2, width=1450, height=70)


#frame
        main_frame=Frame(bg_img, bd=2, bg="BLACK")
        main_frame.place(x=5, y=100, width=1418, height=600)

    #leftframe(student information)
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE, text="STUDENT MANAGEMENT",font=("verdana",20,"bold"),bg="PURPLE",fg="white")
        left_frame.place(x=10, y=10, width=680, height=580)

        #current course frame
        curr_course=LabelFrame(left_frame,bd=2,relief=RIDGE,text="CURRENT COURSE",font=("verdana",14,"bold"), bg="ORANGE", fg="blue")
        curr_course.place(x=10, y=20, width=600, height=130)

            #Department
        dep_label = Label(curr_course,text="DEPARTMENT", font=("times new roman", 12, "bold"), bg="orange")
        dep_label.grid(row=0, column=0, padx=5)

        dep_combo = ttk.Combobox(curr_course,textvariable=self.var_dep,font=("times new roman",8,"bold"),width=17,state="readonly")
        dep_combo["values"] = ("SELECT DEPT", "Computer", "IT", "Civil", "Mechanical", "IOT", "AIML")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=(1, 30), pady=10, sticky=W)




            # Year
        year_label = Label(curr_course, text="YEAR", font=("times new roman", 12, "bold"), bg="orange")
        year_label.grid(row=1, column=0, padx=5,sticky=W)

        year_combo = ttk.Combobox(curr_course,textvariable=self.var_year, font=("times new roman", 9,"bold"), width=17, state="readonly")
        year_combo["values"] = ("SELECT YEAR", "First Year", "Second Year", "Third Year", "Final Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=(1,30), pady=10,sticky=E)

            # Semester
        sem_label = Label(curr_course, text="SEMESTER", font=("times new roman", 12,"bold"),bg="orange")
        sem_label.grid(row=1, column=2, padx=5, sticky=W)


        sem_combo = ttk.Combobox(curr_course,textvariable=self.var_semester, font=("times new roman", 8,"bold"), width=18, state="readonly")
        sem_combo["values"] = ("SELECT SEMESTER", "I", "II", "III", "IV", "V", "VI", "VII", "VII")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=(1, 30), pady=10, sticky=W)



        # Student Detials frame
        stud_details = LabelFrame(left_frame, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=("verdana", 14, "bold"), bg="ORANGE", fg="blue")
        stud_details.place(x=10, y=180, width=600, height=130)

            #studentID
        studID=Label(stud_details,text="Roll No:",font=("times new roman",13,"bold"),bg="orange")
        studID.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        studID_input=ttk.Entry(stud_details,textvariable=self.var_std_id,width=10,font=("times new roman",13,"bold"))
        studID_input.grid(row=0, column=1, padx=(1,30), pady=5, sticky=W)

            # studentname
        studname = Label(stud_details, text="Student Name:", font=("times new roman", 13, "bold"),bg="orange")
        studname.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        studname_input = ttk.Entry(stud_details,textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studname_input.grid(row=0, column=3, padx=(1,15), pady=5, sticky=W)

            # gender
        studgender = Label(stud_details, text="Gender:", font=("times new roman", 13, "bold"), bg="orange")
        studgender.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(stud_details, textvariable=self.var_gender, font=("times new roman", 13), width=10, state="readonly")
        gender_combo["values"] = ("SELECT", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=(1, 30), pady=5, sticky=W)

            # DOB
        studdob = Label(stud_details, text="DOB:", font=("times new roman", 13, "bold"), bg="orange")
        studdob.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        studdob_input = ttk.Entry(stud_details, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        studdob_input.grid(row=1, column=3, padx=(1, 15), pady=5, sticky=W)

            # phoneNo
        studphone = Label(stud_details, text="Phone No:", font=("times new roman", 13, "bold"), bg="orange")
        studphone.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        studphone_input = ttk.Entry(stud_details, textvariable=self.var_phone, width=15, font=("times new roman", 13, "bold"))
        studphone_input.grid(row=2, column=1, padx=(1, 15), pady=5, sticky=W)

            # batch
        studbat = Label(stud_details, text="Batch:", font=("times new roman", 13, "bold"), bg="orange")
        studbat.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        bat_combo = ttk.Combobox(stud_details, textvariable=self.var_bat, font=("times new roman", 8, "bold"), width=18, state="readonly")
        bat_combo["values"] = ("SELECT BATCH", "A", "B", "C")
        bat_combo.current(0)
        bat_combo.grid(row=2, column=3, padx=(1, 30), pady=10, sticky=W)



    # radiobutton
        self.var_rb1 = StringVar()
        rb1 = ttk.Radiobutton(main_frame, variable=self.var_rb1, text="TAKE PHOTO ", value="Yes")
        rb1.place(x=20, y=400)
        rb2 = ttk.Radiobutton(main_frame, variable=self.var_rb1, text="DON'T TAKE PHOTO", value="No")
        rb2.place(x=120, y=400)

        # bbuttons frame 1
        button_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="orange")
        button_frame.place(x=10, y=400, width=600, height=70)

        #     #save Button
        save = Button(button_frame, text="SAVE", command=self.add_data, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save.grid(row=0, column=0)
        #     # update Button
        update = Button(button_frame, text="UPDATE", command=self.update_data, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update.grid(row=0, column=1)
        #     # delete Button
        delete = Button(button_frame, text="DELETE", command=self.delete_data,width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete.grid(row=0, column=2)
        #     # reset Button
        reset = Button(button_frame, text="RESET", command=self.reset_data, width=14, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset.grid(row=0, column=3)
        #
        #button frame 2
        button_frame_2 = Frame(button_frame, bd=2, relief=RIDGE, bg="white")
        button_frame_2.place(x=-1, y=30, width=600, height=35)

            # take photo sample
        take_photo = Button(button_frame_2, command=self.generate_dataset, text="TAKE PHOTO", width=29, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo.grid(row=0, column=0)
            # update photo sample
        back_frame = Button(button_frame_2, command=self.end_program, text="BACK", width=29, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        back_frame.grid(row=0, column=1)






    # rightframe
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="STUDENT INFORMATION",font=("verdana", 20, "bold"), bg="PURPLE", fg="white")
        right_frame.place(x=700, y=10, width=720, height=580)

        # search frame
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="SEARCH", font=("verdana", 14, "bold"),bg="ORANGE", fg="blue")
        search_frame.place(x=30, y=20, width=600, height=130)
        self.search_input = Entry(search_frame, textvariable=self.var_search_input, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)

            #search lable
        search_lbl=Label(search_frame,text="Search By:", font=("times new roman",13,"bold"),bg="ORANGE",fg="BLACK")
        search_lbl.grid(row=0, column=0, padx=(80, 5), pady=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=10, state="readonly")
        search_combo["values"] = ("SELECT", "ROLL NO", "NAME")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)

            #type search
        search_lbl = Label(search_frame, text="Type Here:", font=("times new roman", 13, "bold"), bg="ORANGE", fg="BLACK")
        search_lbl.grid(row=0, column=2, padx=(20, 5), pady=10, sticky=W)
        search_input = ttk.Entry(search_frame, font=("times new roman", 15, "bold"), width=10)
        search_input.grid(row=0, column=3, padx=5, pady=10, sticky=W)

            # search Button
        search_button = Button(search_frame, text="SEARCH", command=self.search_data, width=10, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        search_button.place(x=160, y=50)
            #showall Button
        showall_button = Button(search_frame, text="SHOWALL", command=self.show_all_data, width=10, font=("times new roman", 13, "bold"), bg="blue",fg="white")
        showall_button.place(x=280, y=50)
        self.search_combo = ttk.Combobox(search_frame, textvariable=self.var_search_combo, font=("times new roman", 12, "bold"), width=10, state="readonly")


        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)#TEXT="SEARCH SYSTEM",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=170,width=710,height=375)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame, column=("roll","nam","dep","yr","sem","bat","gen","dob","ph","ps") , xscrollcommand=scroll_x.set , yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_x.config(command=self.student_table.xview)



        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("nam", text="Name")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("yr", text="Year")
        self.student_table.heading("sem", text="Sem")
        self.student_table.heading("bat", text="Batch")
        self.student_table.heading("gen", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("ph", text="Phone")
        self.student_table.heading("ps", text="Photo Sample")

        self.student_table["show"] = "headings"

        self.student_table.column("roll", width=160)
        self.student_table.column("nam", width=160)
        self.student_table.column("dep", width=160)
        self.student_table.column("yr", width=160)
        self.student_table.column("sem", width=160)
        self.student_table.column("bat", width=160)
        self.student_table.column("gen", width=160)
        self.student_table.column("dob", width=160)
        self.student_table.column("ph", width=160)
        self.student_table.column("ps", width=160)



        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


# ==========================function declaration===============

    def add_data(self):
        if self.var_dep.get() == "SELECT DEPT" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", password="root", database="face_recognizers")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                self.var_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_dep.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.var_bat.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_rb1.get()
                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

#
# # =======================fetch data===============
    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", password="root", database="face_recognizers")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()
#
#     # ==================get cursor ================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[2]),
        self.var_year.set(data[3]),
        self.var_semester.set(data[4]),
        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_phone.set(data[8]),
        self.var_bat.set(data[5]),
        self.var_rb1.set(data[9])

#
# # ===========update func=========
#
    def update_data(self):
        if self.var_dep.get()=="SELECT DEPT" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn = pymysql.connect(host="localhost", user="root", password="root",database="face_recognizers")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set name=%s,dept=%s,year=%s,sem=%s,batch=%s,gender=%s,dob=%s,phone=%s,photosample=%s where rollno=%s",(
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_bat.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_rb1.get(),
                                                                                                                                                                self.var_std_id.get()

                                                                                                                                                              ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

#  # =====delete func=========
#
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student",parent=self.root)
                if delete > 0:
                    conn = pymysql.connect(host="localhost", user="root", password="root",database="face_recognizers")
                    my_cursor = conn.cursor()
                    sql = "delete from student where rollno=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted students details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}",parent=self.root)

#
#     # =======reset func==========
    def reset_data(self):
        self.var_dep.set("SELECT DEPT"),
        self.var_year.set("SELECT YEAR"),
        self.var_semester.set("SELECT SEMESTER"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_gender.set("SELECT"),
        self.var_dob.set(""),
        self.var_bat.set(""),
        self.var_phone.set(""),
        self.var_rb1.set("")

#         # ============generate data set or take photo sample========
    def generate_dataset(self):
        if self.var_dep.get() == "SELECT DEPT" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                DATA_DIR = './Database'
                if not os.path.exists(DATA_DIR):
                    os.makedirs(DATA_DIR)

                # Function to fetch folder names from SQL database
                def fetch_folder_names():
                    conn = pymysql.connect(host="localhost", user="root", password="root", database="face_recognizers")
                    cursor = conn.cursor()
                    cursor.execute("select rollno, name from student where rollno = %s", (self.var_std_id.get()))


                    folder_names = [f"{row[0]}-{row[1]}" for row in cursor.fetchall()]
                    conn.close()
                    return folder_names
                dataset_size = 50
                # Capture images for each folder
                for folder_name in fetch_folder_names():
                    folder_path = os.path.join(DATA_DIR, folder_name)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)

                    print('Collecting data for folder {}'.format(folder_name))

                    done = False
                    while True:
                        ret, frame = self.cap.read()
                        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                                    cv2.LINE_AA)

                        cv2.imshow('frame', frame)
                        if cv2.waitKey(25) == ord('q'):
                            break

                    counter = 0
                    while counter < dataset_size:
                        ret, frame = self.cap.read()
                        cv2.imshow('frame', frame)
                        cv2.waitKey(25)
                        cv2.imwrite(os.path.join(folder_path, '{}.jpg'.format(counter)), frame)

                        counter += 1

                # cap.release()
                # cv2.destroyAllWindows()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)


    #=======================Search code========================

# Add these methods inside the student class

    def search_data(self):
       # ============search data======================
        if self.var_com_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select option")
        else:
            try:
                conn = pymysql.connect(host="localhost", username="root", password="shaikhsql",database="shaikhdb")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where "+str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                rows = my_cursor.fetchall()

                if len(rows)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to {str(es)}", parent=self.root)

    def show_all_data(self):
       pass

#==================================back====================================
    def end_program(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.root.destroy()


# Call this function whenever you want to end the program



if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
