import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow

class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("ผู้จัดจำหน่าย")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==รวมตัวตัวแปร== #
        self.var_searchby_id = StringVar()
        self.var_searchtxt_id = StringVar()
        self.var_eid_id = StringVar()
        self.var_name_id = StringVar()
        self.var_contact_id = StringVar()
        self.var_email_id = StringVar()
        self.var_address_id = StringVar()
        self.var_product_id = StringVar()
        self.var_supply_date_id = StringVar()

        # ==ค้นหา== #
        SearchFrame = LabelFrame(self.root, bg="white", text="ค้นหาผู้จัดจำหน่าย", font=("th sarabun psk", 12, "bold"))
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # ==เพิ่มเติม== #
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby_id, values=("เลือก", "name", "address", "eid", "email"),
                                  state="readonly", justify=CENTER, font=("th sarabun psk", 15), cursor="hand2")
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, command=self.search, text="ค้นหา", font=("th sarabun psk", 15), bg="lightgreen", cursor="hand2").place(x=430, y=7, width=140, height=30)

        # ==หัวข้อ== #
        title = Label(self.root, text="รายละเอียดผู้จัดจำหน่าย", font=("th sarabun psk", 15), bg="#ffa233", fg="white").place(x=50, y=100, width=1000)

         # ==ตาราง== #

        # ==แถว1== #
        lbl_supplierid = Label(self.root, text="ID", font=("th sarabun psk", 15), bg="white").place(x=50, y=150)
        lbl_name = Label(self.root, text="บริษัท", font=("th sarabun psk", 15), bg="white").place(x=350, y=150)
        lbl_contact = Label(self.root, text="ติดต่อ", font=("th sarabun psk", 15), bg="white").place(x=750, y=150)

        txt_supplierid = Entry(self.root, textvariable=self.var_eid_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=150, width=180)
        txt_name = Entry(self.root, textvariable=self.var_name_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=500, y=150, width=180)
        txt_contact = Entry(self.root, textvariable=self.var_contact_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=850, y=150, width=180)

        # ==แถว2== #
        lbl_email = Label(self.root, text="อีเมล", font=("th sarabun psk", 15), bg="white").place(x=50, y=190)
        lbl_address = Label(self.root, text="ที่อยู่", font=("th sarabun psk", 15), bg="white").place(x=350, y=190)
        lbl_product = Label(self.root, text="สินค้า", font=("th sarabun psk", 15), bg="white").place(x=750, y=190)

        txt_email = Entry(self.root, textvariable=self.var_email_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=190, width=180)
        txt_address = Entry(self.root, textvariable=self.var_address_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=500, y=190, width=180)
        txt_product = Entry(self.root, textvariable=self.var_product_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=850, y=190, width=180)

        # ==แถว3== #
        lbl_supply_date = Label(self.root, text="วันที่จัดจำหน่าย", font=("th sarabun psk", 15), bg="white").place(x=50, y=230)

        txt_supply_date = Entry(self.root, textvariable=self.var_supply_date_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=200, y=230, width=180)

        # ==ปุ่ม== #
        btn_add = Button(self.root, text="บันทึก", command=self.add, font=("th sarabun psk", 15), bg="lightblue", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="เพิ่ม", command=self.update, font=("th sarabun psk", 15), bg="lightgreen", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="ลบ", command=self.delete, font=("th sarabun psk", 15), bg="red", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="ล้าง", command=self.clear, font=("th sarabun psk", 15), bg="black", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)

        # ==ตารางผู้จัดจำหน่าย== #
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.SupplierTable = ttk.Treeview(emp_frame, columns=("eid", "name", "contact", "email", "product", "address", "supply_date"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("eid", text="ID")
        self.SupplierTable.heading("name", text="บริษัท")
        self.SupplierTable.heading("contact", text="ติดต่อ")
        self.SupplierTable.heading("email", text="อีเมล")
        self.SupplierTable.heading("product", text="สินค้าที่จัดจำหน่าย")
        self.SupplierTable.heading("address", text="ที่อยู่")
        self.SupplierTable.heading("supply_date", text="วันที่จัดจำหน่าย")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("eid", width=90)
        self.SupplierTable.column("name", width=100)
        self.SupplierTable.column("contact", width=100)
        self.SupplierTable.column("email", width=100)
        self.SupplierTable.column("product", width=100)
        self.SupplierTable.column("address", width=200)
        self.SupplierTable.column("supply_date", width=120)

        self.SupplierTable.pack(fill=BOTH, expand=1)

        self.SupplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()  # Show data in the table


    def add(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_eid_id.get() == "":  # Check for supplier ID
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสผู้จัดจำหน่าย", parent=self.root)
            else:
                cur.execute("select * from supplier where eid=?", (self.var_eid_id.get(),))  # Corrected table and field name
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "มีรายการดังกล่าวแล้ว", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (eid, name, contact, email, product, address, supply_date) VALUES(?,?,?,?,?,?,?)", (
                        self.var_eid_id.get(),  # Correct supplier ID variable
                        self.var_name_id.get(),
                        self.var_contact_id.get(),
                        self.var_email_id.get(),
                        self.var_product_id.get(),
                        self.var_address_id.get(),
                        self.var_supply_date_id.get()
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
            cur.execute("select * from supplier")  # Use supplier table
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())  # Use SupplierTable
            for row in rows:
                self.SupplierTable.insert('', END, values=row)  # Use SupplierTable

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.SupplierTable.focus()  # Corrected to use SupplierTable
        content = self.SupplierTable.item(f)  # Corrected to use SupplierTable
        row = content['values']
        print(row)  # แสดงค่า row เพื่อตรวจสอบ
        
        # กำหนดค่าตัวแปรตามลำดับ row[0] - row[10]
        self.var_eid_id.set(row[0])  # Corrected variable names for supplier data
        self.var_name_id.set(row[1])
        self.var_contact_id.set(row[2])
        self.var_email_id.set(row[3])
        self.var_product_id.set(row[4])
        self.var_address_id.set(row[5])
        self.var_supply_date_id.set(row[6])  # Date of supply

    def update(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_eid_id.get() == "":
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสผู้จัดจำหน่าย", parent=self.root)
            else:
                cur.execute("select * from supplier where eid=?", (self.var_eid_id.get(),))  # Use supplier table
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "ไม่พบข้อมูลผู้จัดจำหน่าย", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE supplier SET name=?, contact=?, email=?, product=?, address=?, supply_date=? WHERE eid=?", 
                        (
                            self.var_name_id.get(),
                            self.var_contact_id.get(),
                            self.var_email_id.get(),
                            self.var_product_id.get(),
                            self.var_address_id.get(),
                            self.var_supply_date_id.get(),
                            self.var_eid_id.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "ข้อมูลผู้จัดจำหน่ายอัพเดทสำเร็จ", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def delete(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:
            if self.var_eid_id.get() == "":
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสผู้จัดจำหน่าย", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE eid=?", (self.var_eid_id.get(),))  # Use supplier table
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "ไม่พบข้อมูลผู้จัดจำหน่าย", parent=self.root)
                else:
                    confirm = messagebox.askyesno("Confirm", "คุณต้องการลบข้อมูลผู้จัดจำหน่ายนี้หรือไม่?", parent=self.root)
                    if confirm:
                        cur.execute("DELETE FROM supplier WHERE eid=?", (self.var_eid_id.get(),))  # Use supplier table
                        con.commit()
                        messagebox.showinfo("Success", "ลบข้อมูลสำเร็จ", parent=self.root)
                        self.show()
                        self.clear_fields()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear_fields(self):
        # ฟังก์ชันนี้ล้างข้อมูลในฟิลด์ต่าง ๆ
        self.var_eid_id.set("")
        self.var_name_id.set("")
        self.var_contact_id.set("")
        self.var_email_id.set("")
        self.var_address_id.set("")
        self.var_product_id.set("")
        self.var_supply_date_id.set("")
        self.var_searchby_id.set("เลือก")
        self.var_searchtxt_id.set("")

    def clear(self):
        self.var_eid_id.set("")
        self.var_name_id.set("")
        self.var_contact_id.set("")
        self.var_email_id.set("")
        self.var_address_id.set("")
        self.var_product_id.set("")
        self.var_supply_date_id.set("")
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
                cur.execute("select * from supplier where "+self.var_searchby_id.get()+" LIKE ?", 
                            ('%' + self.var_searchtxt_id.get() + '%',))  # Use supplier table
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())  # Use SupplierTable
                    for row in rows:
                        self.SupplierTable.insert('', END, values=row)  # Use SupplierTable
                else:
                    messagebox.showerror("Error", "ไม่พบบันทึก!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)  
  

if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
