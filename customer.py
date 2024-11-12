import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow

class customerClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("ลูกค้า")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==รวมตัวตัวแปร== #
        self.var_searchby_id = StringVar()
        self.var_searchtxt_id = StringVar()
        self.var_eid_id = StringVar()
        self.var_company_id = StringVar()
        self.var_name_id = StringVar()
        self.var_contact_id = StringVar()
        self.var_email_id = StringVar()
        self.var_address_id = StringVar()

        # ==ค้นหา== #
        SearchFrame = LabelFrame(self.root, bg="white", text="ค้นหาลูกค้า", font=("th sarabun psk", 12, "bold"))
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # ==เพิ่มเติม== #
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby_id, values=("เลือก", "name", "address", "eid", "email"),
                                  state="readonly", justify=CENTER, font=("th sarabun psk", 15), cursor="hand2")
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, command=self.search, text="ค้นหา", font=("th sarabun psk", 15), bg="lightgreen", cursor="hand2").place(x=430, y=7, width=140, height=30)

        # ==หัวข้อ== #
        title = Label(self.root, text="รายละเอียดลูกค้า", font=("th sarabun psk", 15), bg="#ffa233", fg="white").place(x=50, y=100, width=1000)

         # ==ตาราง== #

        # ==แถว1== #
        lbl_customerid = Label(self.root, text="ID", font=("th sarabun psk", 15), bg="white").place(x=50, y=150)
        lbl_company = Label(self.root, text="บริษัท", font=("th sarabun psk", 15), bg="white").place(x=350, y=150)
        lbl_name = Label(self.root, text="ชื่อ", font=("th sarabun psk", 15), bg="white").place(x=650, y=150)

        txt_customerid = Entry(self.root, textvariable=self.var_eid_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=150, width=180)
        txt_company = Entry(self.root, textvariable=self.var_company_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=450, y=150, width=180)
        txt_name = Entry(self.root, textvariable=self.var_name_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=750, y=150, width=180)

        # ==แถว2== #
        lbl_contact = Label(self.root, text="ติดต่อ", font=("th sarabun psk", 15), bg="white").place(x=50, y=200)
        lbl_email = Label(self.root, text="อีเมล", font=("th sarabun psk", 15), bg="white").place(x=350, y=200)
        lbl_address = Label(self.root, text="ที่อยู่", font=("th sarabun psk", 15), bg="white").place(x=650, y=200)

        txt_contact = Entry(self.root, textvariable=self.var_contact_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=200, width=180)
        txt_email = Entry(self.root, textvariable=self.var_email_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=450, y=200, width=180)

        # ใช้ Text widget สำหรับที่อยู่ และปรับขนาดให้พอดี
        self.txt_address = Text(self.root, font=("th sarabun psk", 15), bg="lightyellow")
        self.txt_address.place(x=750, y=200, width=300, height=60)  # ปรับขนาดให้ใหญ่ขึ้นและพอดีกับหน้าจอ

        

        # ==ปุ่ม== #
        btn_add = Button(self.root, text="บันทึก", command=self.add, font=("th sarabun psk", 15), bg="lightblue", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="เพิ่ม", command=self.update, font=("th sarabun psk", 15), bg="lightgreen", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="ลบ", command=self.delete, font=("th sarabun psk", 15), bg="red", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="ล้าง", command=self.clear, font=("th sarabun psk", 15), bg="black", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)

        # ==ตารางลูกค้า== #
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.customerTable = ttk.Treeview(emp_frame, columns=("eid","company", "name", "contact", "email", "address", "supply_date"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.customerTable.xview)
        scrolly.config(command=self.customerTable.yview)

        self.customerTable.heading("eid", text="ID")
        self.customerTable.heading("company", text="บริษัท")
        self.customerTable.heading("name", text="ชื่อ")
        self.customerTable.heading("contact", text="ติดต่อ")
        self.customerTable.heading("email", text="อีเมล")
        self.customerTable.heading("address", text="ที่อยู่")

        self.customerTable["show"] = "headings"

        self.customerTable.column("eid", width=90)
        self.customerTable.column("company", width=100)
        self.customerTable.column("name", width=100)
        self.customerTable.column("contact", width=100)
        self.customerTable.column("email", width=100)
        self.customerTable.column("address", width=200)

        self.customerTable.pack(fill=BOTH, expand=1)

        self.customerTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()  # Show data in the table


    def add(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_eid_id.get() == "":  # Check for customer ID
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสลูกค้า", parent=self.root)
            else:
                cur.execute("select * from customer where eid=?", (self.var_eid_id.get(),))  # Corrected table and field name
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "มีรายการดังกล่าวแล้ว", parent=self.root)
                else:
                    cur.execute("INSERT INTO customer (eid, company, name, contact, email, address) VALUES (?, ?, ?, ?, ?, ?)", (
                        self.var_eid_id.get(),  # Correct customer ID variable
                        self.var_company_id.get(),
                        self.var_name_id.get(),
                        self.var_contact_id.get(),
                        self.var_email_id.get(),
                        self.txt_address.get("1.0", END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "บันทึกสำเร็จ", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def show(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            cur.execute("select * from customer")  # Use customer table
            rows = cur.fetchall()
            self.customerTable.delete(*self.customerTable.get_children())  # Use customerTable
            for row in rows:
                self.customerTable.insert('', END, values=row)  # Use customerTable

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.customerTable.focus()  # Corrected to use customerTable
        content = self.customerTable.item(f)  # Corrected to use customerTable
        row = content['values']
        print(row)  # แสดงค่า row เพื่อตรวจสอบ
        
        # กำหนดค่าตัวแปรตามลำดับ row[0] - row[10]
        self.var_eid_id.set(row[0])  # Corrected variable names for customer data
        self.var_company_id.set(row[1])
        self.var_name_id.set(row[2])
        self.var_contact_id.set(row[3])
        self.var_email_id.set(row[4])
        self.var_address_id.set(row[5])

    def update(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_eid_id.get() == "":
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสลูกค้า", parent=self.root)
            else:
                cur.execute("select * from customer where eid=?", (self.var_eid_id.get(),))  # Corrected to use the supplier table
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "ไม่พบข้อมูลลูกค้า", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE customer SET company=?, name=?, contact=?, email=?, address=? WHERE eid=?",  # Fixed the query
                        (
                            self.var_company_id.get(),
                            self.var_name_id.get(),
                            self.var_contact_id.get(),
                            self.var_email_id.get(),
                            self.txt_address.get("1.0", END),
                            self.var_eid_id.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "ข้อมูลลูกค้าอัพเดทสำเร็จ", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)



    

    def delete(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_eid_id.get() == "":
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสลูกค้า", parent=self.root)
            else:
                cur.execute("SELECT * FROM customer WHERE eid=?", (self.var_eid_id.get(),))  # Use customer table
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "ไม่พบข้อมูลลูกค้า", parent=self.root)
                else:
                    confirm = messagebox.askyesno("Confirm", "คุณต้องการลบข้อมูลลูกค้านี้หรือไม่?", parent=self.root)
                    if confirm:
                        cur.execute("DELETE FROM customer WHERE eid=?", (self.var_eid_id.get(),))  # Use customer table
                        con.commit()
                        messagebox.showinfo("Success", "ลบข้อมูลสำเร็จ", parent=self.root)
                        self.show()
                        self.clear_fields()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear_fields(self):
        # ฟังก์ชันนี้ล้างข้อมูลในฟิลด์ต่าง ๆ
        self.var_eid_id.set("")
        self.var_company_id.set("")
        self.var_name_id.set("")
        self.var_contact_id.set("")
        self.var_email_id.set("")
        self.txt_address.delete("1.0", END)
        self.var_searchby_id.set("เลือก")
        self.var_searchtxt_id.set("")

    def clear(self):
        self.var_eid_id.set("")
        self.var_company_id.set("")
        self.var_name_id.set("")
        self.var_contact_id.set("")
        self.var_email_id.set("")
        self.txt_address.delete("1.0", END)
        self.var_searchby_id.set("เลือก")
        self.var_searchtxt_id.set("")

    def search(self): 
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby_id.get() == "เลือก":
                messagebox.showerror("Error", "เลือกตัวเลือกในการค้นหา", parent=self.root)

            elif self.var_searchtxt_id.get() == "":
                messagebox.showerror("Error", "ป้อนข้อมูลการค้นหาก่อน", parent=self.root)
            else:
                cur.execute("select * from customer where "+self.var_searchby_id.get()+" LIKE ?", 
                            ('%' + self.var_searchtxt_id.get() + '%',))  # Use customer table
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.customerTable.delete(*self.customerTable.get_children())  # Use customerTable
                    for row in rows:
                        self.customerTable.insert('', END, values=row)  # Use customerTable
                else:
                    messagebox.showerror("Error", "ไม่พบบันทึก!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)  
  

if __name__ == "__main__":
    root = Tk()
    obj = customerClass(root)
    root.mainloop()
