import sqlite3
from tkinter import *  # pip install tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("บริษัท ไกเซอร์ เทเลมาร์ท โปรแกรมโดย ภัทรชนน")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==รวมตัวตัวแปร== #
        self.var_searchby_id = StringVar()
        self.var_searchtxt_id = StringVar()
        self.var_emp_id = StringVar()
        self.var_gender_id = StringVar()
        self.var_contact_id = StringVar()
        self.var_name_id = StringVar()
        self.var_doj_id = StringVar()
        self.var_dob_id = StringVar()
        self.var_email_id = StringVar()
        self.var_pass_id = StringVar()
        self.var_utype_id = StringVar()
        self.var_address_id = StringVar()
        self.var_salary_id = StringVar()

        # ==ค้นหา== #
        SearchFrame = LabelFrame(self.root, bg="white", text="ค้นหาพนักงาน", font=("th sarabun psk", 12, "bold"))
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # ==เพิ่มเติม== #
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby_id, values=("เลือก", "email", "name", "contact", "eid"),
                                  state="readonly", justify=CENTER, font=("th sarabun psk", 15), cursor="hand2")
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame,command=self.search, text="ค้นหา", font=("th sarabun psk", 15), bg="lightgreen", cursor="hand2").place(x=430, y=7, width=140, height=30)

        # ==หัวข้อ== #
        title = Label(self.root, text="รายละเอียดพนักงาน", font=("th sarabun psk", 15), bg="#ffa233", fg="white").place(x=50, y=100, width=1000)

         # ==ตาราง== #

        # ==แถว1== #
        lbl_empid = Label(self.root, text="ID", font=("th sarabun psk", 15), bg="white").place(x=50, y=150)
        lbl_gender = Label(self.root, text="เพศ", font=("th sarabun psk", 15), bg="white").place(x=350, y=150)
        lbl_contact = Label(self.root, text="ติดต่อ", font=("th sarabun psk", 15), bg="white").place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender_id, values=("เลือก", "ชาย", "หญิง", "เพศทางเลือก", "ไม่ระบุ"),
                                  state="readonly", justify=CENTER, font=("th sarabun psk", 15), cursor="hand2")
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=850, y=150, width=180)

        # ==แถว2== #
        lbl_name = Label(self.root, text="ชื่อ", font=("th sarabun psk", 15), bg="white").place(x=50, y=190)
        lbl_dob = Label(self.root, text="วันเกิด", font=("th sarabun psk", 15), bg="white").place(x=350, y=190)
        lbl_doj = Label(self.root, text="เริ่มทำงาน", font=("th sarabun psk", 15), bg="white").place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=850, y=190, width=180)

        # ==แถว3== #
        lbl_email = Label(self.root, text="อีเมล", font=("th sarabun psk", 15), bg="white").place(x=50, y=230)
        lbl_pass = Label(self.root, text="รหัสผ่าน", font=("th sarabun psk", 15), bg="white").place(x=350, y=230)
        lbl_utype = Label(self.root, text="ตำแหน่ง", font=("th sarabun psk", 15), bg="white").place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype_id, values=("เลือก", "ceo", "admin", "บัญชี", "เซลล์", "แมสเซ็นเจอร์"),
                                  state="readonly", justify=CENTER, font=("th sarabun psk", 15), cursor="hand2")
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        # ==แถว4== #
        lbl_address = Label(self.root, text="ที่อยู่", font=("th sarabun psk", 15), bg="white").place(x=50, y=270)
        lbl_salary = Label(self.root, text="เงินเดือน", font=("th sarabun psk", 15), bg="white").place(x=500, y=270)

        self.txt_address = Text(self.root, font=("th sarabun psk", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=600, y=270, width=180)

        # ==ปุ่ม== #
        btn_add = Button(self.root, text="บันทึก", command=self.add, font=("th sarabun psk", 15), bg="lightblue", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="เพิ่ม", command=self.update, font=("th sarabun psk", 15), bg="lightgreen", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="ลบ", command=self.delete, font=("th sarabun psk", 15), bg="red", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="ล้าง", command=self.clear, font=("th sarabun psk", 15), bg="black", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)

        # ==ตารางพนักงาน== #
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "utype", "gender", "dob", "contact", "pass", "address", "salary", "doj"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("eid", text="ID")
        self.EmployeeTable.heading("name", text="ชื่อ")
        self.EmployeeTable.heading("email", text="อีเมล")
        self.EmployeeTable.heading("utype", text="ตำแหน่ง")
        self.EmployeeTable.heading("gender", text="เพศ")
        self.EmployeeTable.heading("dob", text="วันเกิด")
        self.EmployeeTable.heading("contact", text="ติดต่อ")
        self.EmployeeTable.heading("pass", text="รหัสผ่าน")
        self.EmployeeTable.heading("salary", text="เงินเดือน")
        self.EmployeeTable.heading("address", text="ที่อยู่")
        self.EmployeeTable.heading("doj", text="วันทำงาน")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("salary", width=100)
        self.EmployeeTable.column("address", width=200)
        self.EmployeeTable.column("doj", width=100)

        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)


        self.show()

    # Define the add method outside the __init__ method
    def add(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสพนักงาน", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","มีรายการดังกล่าวแล้ว",parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (eid, name, email, utype, gender, dob, contact, pass, address, salary, doj) VALUES(?,?,?,?,?,?,?,?,?,?,?)", (
                        self.var_emp_id.get(),
                        self.var_name_id.get(),
                        self.var_email_id.get(),
                        self.var_utype_id.get(),
                        self.var_gender_id.get(),
                        self.var_dob_id.get(),
                        self.var_contact_id.get(),
                        self.var_pass_id.get(),
                        self.txt_address.get("1.0", END),
                        self.var_salary_id.get(),
                        self.var_doj_id.get(),
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "บันทึกสำเร็จ", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)

    def show(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows = cur.fetchall()  # Corrected line: changed con.fetchall() to cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.EmployeeTable.focus()  
        content = self.EmployeeTable.item(f)  
        row = content['values']  
        print(row)  # แสดงค่า row เพื่อตรวจสอบ
    
    # กำหนดค่าตัวแปรตามลำดับ row[0] - row[10]
        self.var_emp_id.set(row[0])        # Employee ID (eid)
        self.var_name_id.set(row[1])       # Name
        self.var_email_id.set(row[2])      # Email
        self.var_utype_id.set(row[3])      # User Type (utype)
        self.var_gender_id.set(row[4])     # Gender
        self.var_dob_id.set(row[5])        # Date of Birth (dob)
        self.var_contact_id.set(row[6])    # Contact
        self.var_pass_id.set(row[7])       # Password        
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[8])  # Address
        self.var_salary_id.set(row[9])     # Salary
        self.var_doj_id.set(row[10])       # Date of Joining (doj)

    def update(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสพนักงาน", parent=self.root)
            else:
                cur.execute("select * from employee where eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "ไม่พบข้อมูลพนักงาน", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE employee SET name=?, email=?, utype=?, gender=?, dob=?, contact=?, pass=?, address=?, salary=?, doj=? WHERE eid=?", 
                        (
                            self.var_name_id.get(),
                            self.var_email_id.get(),
                            self.var_utype_id.get(),
                            self.var_gender_id.get(),
                            self.var_dob_id.get(),
                            self.var_contact_id.get(),
                            self.var_pass_id.get(),
                            self.txt_address.get("1.0", END),
                            self.var_salary_id.get(),
                            self.var_doj_id.get(),  # Date of Joining
                            self.var_emp_id.get()  # Employee ID for WHERE condition
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "บันทึกใหม่สำเร็จ", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    

    def delete(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสพนักงาน", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "ไม่พบข้อมูลพนักงาน", parent=self.root)
                else:
                    confirm = messagebox.askyesno("Confirm", "คุณต้องการลบข้อมูลพนักงานนี้หรือไม่?", parent=self.root)
                    if confirm:
                        cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success", "ลบข้อมูลสำเร็จ", parent=self.root)
                        self.show()
                        # ล้างข้อมูลในฟิลด์หลังจากลบเสร็จ
                        self.clear_fields()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    def clear_fields(self):
        # ฟังก์ชันนี้ล้างข้อมูลในฟิลด์ต่าง ๆ
        self.var_emp_id.set("")
        self.var_name_id.set("")
        self.var_email_id.set("")
        self.var_utype_id.set("")
        self.var_gender_id.set("")
        self.var_dob_id.set("")
        self.var_contact_id.set("")
        self.var_pass_id.set("")
        self.txt_address.delete("1.0", END)
        self.var_salary_id.set("")
        self.var_doj_id.set("")

    def clear(self):
        self.var_emp_id.set("")        # Employee ID (eid)
        self.var_name_id.set("")       # Name
        self.var_email_id.set("")      # Email
        self.var_utype_id.set("เลือก")      # User Type (utype)
        self.var_gender_id.set("เลือก")     # Gender
        self.var_dob_id.set("")        # Date of Birth (dob)
        self.var_pass_id.set("")       # Password
        self.var_contact_id.set("")    # Contact
        self.txt_address.delete("1.0", END)
        self.var_salary_id.set("")     # Salary
        self.var_doj_id.set("")       # Date of Joining (doj)
        self.var_searchby_id.set("เลือก")
        self.var_searchtxt_id.set("")
        self.show()

    def search(self): 
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby_id.get()=="เลือก":
                messagebox.showerror("Error", "เลือกตัวเลือกในการค้นหา", parent=self.root)

            elif self.var_searchtxt_id.get()=="":
                messagebox.showerror("Error", "ป้อนข้อมูลการค้นหาก่อน", parent=self.root)
                cur.execute("select * from employee")

            else:
                cur.execute("select * from employee where "+self.var_searchby_id.get()+" LIKE '%"+self.var_searchtxt_id.get()+"%'")
                rows = cur.fetchall()  # Corrected line: changed con.fetchall() to cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "ไม่พบบันทึก!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)  

        
        

if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()