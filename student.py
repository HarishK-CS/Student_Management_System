from tkinter import *
from tkinter import ttk, messagebox
from db import Database

class Student:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")
        self.root.config(bg="#2c3e50")
        self.root.state("zoomed")
        self.db = Database("student.db")

        # variables
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_yr = StringVar()
        self.var_quota = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_sec = StringVar()
        self.var_reg = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_stud_no = StringVar()
        self.var_parent_no = StringVar()
        self.var_address = StringVar()
        self.var_blood_grp = StringVar()
        self.var_combo_search = StringVar()
        self.var_search = StringVar()

        lbl_title = Label(root, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 37, "bold"), fg="blue", bg="white")
        lbl_title.place(x=0, y=0, width=1450, height=50)

        # Whole Frame
        manage_frame = Frame(root, bd=2,relief=RIDGE, bg="white")
        manage_frame.place(x=10, y=60, width=1346, height=630)

        # Left Frame
        data_left_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information", font=("times new roman", 12, "bold"), fg="red", bg="white")
        data_left_frame.place(x=10, y=10, width=550, height=540)

        # Left Frame - Top
        current_course_frame = LabelFrame(data_left_frame, bd=2, relief=RIDGE, padx=2, text="Current Course Information", font=("times new roman", 12, "bold"), fg="green", bg="white")
        current_course_frame.place(x=0, y=0, width=540, height=115)

        lbl_dept = Label(current_course_frame, text="Department", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_dept.grid(row=0, column=0, padx=2, pady=7, sticky=W)
        combo_dept = ttk.Combobox(current_course_frame, textvariable=self.var_dept, font=("arial", 9, "bold"), width=17, state="readonly")
        combo_dept["value"] = ("Select Department", "CSE", "IT", "ECE", "EEE", "CIVIL", "MECH")
        combo_dept.current(0)
        combo_dept.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        lbl_course = Label(current_course_frame, text="Course", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_course.grid(row=0, column=2, padx=2, pady=7, sticky=W)
        combo_course = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("arial", 9, "bold"), width=17, state="readonly")
        combo_course["value"] = ("Select Course", "B.TECH", "MBA", "MCA")
        combo_course.current(0)
        combo_course.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        lbl_yr = Label(current_course_frame, text="Year", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_yr.grid(row=1, column=0, padx=2, pady=7, sticky=W)
        combo_yr = ttk.Combobox(current_course_frame, textvariable=self.var_yr, font=("arial", 9, "bold"), width=17, state="readonly")
        combo_yr["value"] = ("Select Year", "I", "II", "III", "IV")
        combo_yr.current(0)
        combo_yr.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        lbl_quota = Label(current_course_frame, text="Quota", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_quota.grid(row=1, column=2, padx=2, pady=7, sticky=W)
        combo_quota = ttk.Combobox(current_course_frame, textvariable=self.var_quota, font=("arial", 9, "bold"), width=17, state="readonly")
        combo_quota["value"] = ("Select Quota", "CENTAC", "MANAGEMENT")
        combo_quota.current(0)
        combo_quota.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Left Frame - Bottom
        student_personal_frame = LabelFrame(data_left_frame, bd=2, relief=RIDGE, padx=2, text="Student Personal Information", font=("times new roman", 12, "bold"), fg="green", bg="white")
        student_personal_frame.place(x=0, y=120, width=540, height=255)

        lbl_id = Label(student_personal_frame, text="ID No", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_id.grid(row=0, column=0, padx=2, pady=7, sticky=W)
        id_entry = ttk.Entry(student_personal_frame, textvariable=self.var_id, font=("arial", 10, "bold"), width=22)
        id_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        lbl_name = Label(student_personal_frame, text="Name", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_name.grid(row=0, column=2, padx=2, pady=7, sticky=W)
        name_entry = ttk.Entry(student_personal_frame, textvariable=self.var_name, font=("arial", 10, "bold"), width=22)
        name_entry.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        lbl_sec = Label(student_personal_frame, text="Section", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_sec.grid(row=1, column=0, padx=2, pady=7, sticky=W)
        combo_sec = ttk.Combobox(student_personal_frame, textvariable=self.var_sec, font=("arial", 9, "bold"), width=17, state="readonly")
        combo_sec["value"] = ("Select Section", "A", "B", "C", "D")
        combo_sec.current(0)
        combo_sec.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        lbl_reg = Label(student_personal_frame, text="Reg No", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_reg.grid(row=1, column=2, padx=2, pady=7, sticky=W)
        reg_entry = ttk.Entry(student_personal_frame, textvariable=self.var_reg, font=("arial", 10, "bold"), width=22)
        reg_entry.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        lbl_gender = Label(student_personal_frame, text="Gender", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_gender.grid(row=2, column=0, padx=2, pady=7, sticky=W)
        combo_gender = ttk.Combobox(student_personal_frame, textvariable=self.var_gender, font=("arial", 9, "bold"), width=17, state="readonly")
        combo_gender["value"] = ("Select Section", "MALE", "FEMALE")
        combo_gender.current(0)
        combo_gender.grid(row=2, column=1, padx=2, pady=10, sticky=W)

        lbl_dob = Label(student_personal_frame, text="DOB", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_dob.grid(row=2, column=2, padx=2, pady=7, sticky=W)
        dob_entry = ttk.Entry(student_personal_frame, textvariable=self.var_dob, font=("arial", 10, "bold"), width=22)
        dob_entry.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        lbl_email = Label(student_personal_frame, text="Email", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)
        email_entry = ttk.Entry(student_personal_frame, textvariable=self.var_email, font=("arial", 10, "bold"), width=22)
        email_entry.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        lbl_student_phone_no = Label(student_personal_frame, text="Student'S Ph No", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_student_phone_no.grid(row=3, column=2, padx=2, pady=7, sticky=W)
        student_phone_no_entry = ttk.Entry(student_personal_frame, textvariable=self.var_stud_no, font=("arial", 10, "bold"), width=22)
        student_phone_no_entry.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        lbl_address = Label(student_personal_frame, text="Address", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_address.grid(row=4, column=0, padx=2, pady=7, sticky=W)
        address_entry = ttk.Entry(student_personal_frame, textvariable=self.var_address, font=("arial", 10, "bold"), width=22)
        address_entry.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        lbl_parent_ph_no = Label(student_personal_frame, text="Parent'S Ph No", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_parent_ph_no.grid(row=4, column=2, padx=2, pady=7, sticky=W)
        parent_ph_no_entry = ttk.Entry(student_personal_frame, textvariable=self.var_parent_no, font=("arial", 10, "bold"), width=22)
        parent_ph_no_entry.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        lbl_blood_group = Label(student_personal_frame, text="Blood Group", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_blood_group.grid(row=5, column=0, padx=2, pady=7, sticky=W)
        combo_blood_group = ttk.Combobox(student_personal_frame, textvariable=self.var_blood_grp, font=("arial", 9, "bold"), width=17, state="readonly")
        combo_blood_group['values'] = ('Select Blood', 'A+', 'A-', 'B+', 'B-', 'O+', 'O-')
        combo_blood_group.current(0)
        combo_blood_group.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Button Frame
        button_frame = Frame(data_left_frame, relief=RIDGE, bg="white")
        button_frame.place(x=0, y=470, width=540, height=38)

        btn_add = Button(button_frame, text="SAVE",command=self.add_student, font=("arial", 10, "bold"), width=15, bg="#16a085", fg="white")
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(button_frame, text="UPDATE",command=self.update_student, font=("arial", 10, "bold"), width=15, bg="#2980b9", fg="white")
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(button_frame, text="DELETE",command=self.delete_student, font=("arial", 10, "bold"), width=15, bg="#FF4500", fg="white")
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(button_frame, text="RESET",command=self.clear_all, font=("arial", 10, "bold"), width=15, bg="#f39c12", fg="white")
        btn_reset.grid(row=0, column=3, padx=1)

        # Right Frame
        data_right_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Details", font=("times new roman", 12, "bold"), fg="red", bg="white")
        data_right_frame.place(x=580, y=10, width=880, height=540)

        # search frame
        search_frame = LabelFrame(data_right_frame, bd=4, relief=RIDGE, padx=2, text="Search Information", font=("times new roman", 12, "bold"), fg="green", bg="white")
        search_frame.place(x=0, y=0, width=750, height=70)

        lbl_search_by = Label(search_frame, text="Search By: ", font=("arial", 10, "bold"), fg="Black", bg="white")
        lbl_search_by.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        combo_search = ttk.Combobox(search_frame, textvariable=self.var_combo_search, font=("arial", 9, "bold"), width=17, state="readonly")
        combo_search["value"] = ("Select Option", "Reg No", "ID", "Year", "Quota", "Blood Group")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, font=("arial", 10, "bold"), width=22)
        txt_search.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        btn_search = Button(search_frame, text="Search", command=self.search_data, font=("arial", 10, "bold"), width=15, bg="#2980b9", fg="white")
        btn_search.grid(row=0, column=3, padx=5)

        btn_show_all = Button(search_frame, text="Show All",command=self.display_all,  font=("arial", 10, "bold"), width=15, bg="#FF4500", fg="white")
        btn_show_all.grid(row=0, column=4, padx=5)

        # Table frames
        table_frame = Frame(data_right_frame, bd=4, relief=RIDGE)
        table_frame.place(x=0, y=70, width=750, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("ID", "RegNo", "name", "course", "dept", "year", "div", "quota", "gender", "dob", "bloodGroup", "email", "studentPh", "parentPh", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="ID")
        self.student_table.heading("RegNo", text="Reg No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("dept", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("div", text="Sec")
        self.student_table.heading("quota", text="Quota")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("bloodGroup", text="Blood Group")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("studentPh", text="Student Ph No")
        self.student_table.heading("parentPh", text="Parent Ph No")
        self.student_table.heading("address", text="Address")

        self.student_table["show"] = "headings"

        self.student_table.column("ID", width=100)
        self.student_table.column("RegNo", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("dept", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("quota", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("bloodGroup", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("studentPh", width=100)
        self.student_table.column("parentPh", width=100)
        self.student_table.column("address", width=100)
        self.student_table.bind("<ButtonRelease-1>", self.get_data)
        self.display_all()

        self.student_table.pack(fill=BOTH, expand=1)
        # self.display_all()

    def display_all(self):
        self.student_table.delete(*self.student_table.get_children())
        for row in self.db.fetch():
            self.student_table.insert("", END, values=row)

    def get_data(self,event):
        selected_row = self.student_table.focus()
        global data
        data = self.student_table.item(selected_row)
        global row
        row = data['values']
        print(row)
        self.var_id.set(row[0])
        self.var_reg.set(row[1])
        self.var_name.set(row[2])
        self.var_course.set(row[3])
        self.var_dept.set(row[4])
        self.var_yr.set(row[5])
        self.var_sec.set(row[6])
        self.var_quota.set(row[7])
        self.var_gender.set(row[8])
        self.var_dob.set(row[9])
        self.var_blood_grp.set(row[10])
        self.var_email.set(row[11])
        self.var_stud_no.set(row[12])
        self.var_parent_no.set(row[13])
        self.var_address.set(row[14])

    def add_student(self):
        if self.var_dept.get() == "" or self.var_course.get() == "" or self.var_quota.get() == "" or self.var_yr.get() == "" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_sec.get() == "" or self.var_reg.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_stud_no.get() == "" or self.var_parent_no.get()=="" or self.var_address.get() == "" or self.var_blood_grp.get() == "":
            messagebox.showerror("Error in Input", "Please Fill all the details !")
        else:
            self.db.insert(self.var_id.get(), self.var_reg.get(), self.var_name.get(), self.var_course.get(), self.var_dept.get(), self.var_yr.get(), self.var_sec.get(), self.var_quota.get(), self.var_gender.get(), self.var_dob.get(), self.var_blood_grp.get(), self.var_email.get(), self.var_stud_no.get(), self.var_parent_no.get(), self.var_address.get())
        self.clear_all()
        self.display_all()

    def update_student(self):
        if self.var_dept.get() == "" or self.var_course.get() == "" or self.var_quota.get() == "" or self.var_yr.get() == "" or self.var_id.get() == "" or self.var_name.get() == "" or self.var_sec.get() == "" or self.var_reg.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_stud_no.get() == "" or self.var_parent_no.get()=="" or self.var_address.get() == "" or self.var_blood_grp.get() == "":
            messagebox.showerror("Error in Input", "Please Fill all the details !")
        else:
            self.db.update(self.var_id.get(), self.var_reg.get(), self.var_name.get(), self.var_course.get(),
                           self.var_dept.get(), self.var_yr.get(), self.var_id.get(), self.var_quota.get(),
                           self.var_gender.get(), self.var_dob.get(), self.var_blood_grp.get(), self.var_email.get(),
                           self.var_stud_no.get(), self.var_parent_no.get(), self.var_address.get())
            messagebox.showinfo("Success", "Record Updated")
        self.clear_all()
        self.display_all()

    def delete_student(self):
        self.db.remove(row[0])
        self.clear_all()
        self.display_all()

    def clear_all(self):
        self.var_id.set("")
        self.var_reg.set("")
        self.var_name.set("")
        self.var_course.set("Select Course")
        self.var_dept.set("Select Department")
        self.var_yr.set("Select Year")
        self.var_sec.set("Select Section")
        self.var_quota.set("Select Quota")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_blood_grp.set("Select Blood Group")
        self.var_email.set("")
        self.var_stud_no.set("")
        self.var_parent_no.set("")
        self.var_address.set("")

    def search_data(self):
        try:
            if self.var_search.get() == "" or self.var_combo_search.get() == "":
                messagebox.showerror("Error", "Please Select Option")
            else:
                data = self.db.search(self.var_combo_search.get(), self.var_search.get())
                # for i in data:
                #     if len(data) != 0:
                #         self.student_table("", END, values=i)
                #     self.db.con.commit()
                # self.db.con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Due to: {ex}")









if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
