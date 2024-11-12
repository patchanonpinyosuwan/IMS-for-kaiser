import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # pip install pillow

class StockClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("ระบบจัดการสต็อกสินค้า")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==รวมตัวแปร== #
        self.var_searchby_id = StringVar()
        self.var_searchtxt_id = StringVar()
        self.var_product_id = StringVar()
        self.var_name_id = StringVar()
        self.var_quantity_id = StringVar()
        self.var_price_id = StringVar()
        self.var_status_id = StringVar()

        # ==ค้นหา== #
        SearchFrame = LabelFrame(self.root, bg="white", text="ค้นหาสินค้า", font=("th sarabun psk", 12, "bold"))
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # ==เพิ่มเติม== #
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby_id, values=("เลือก", "product_id", "name"),
                                  state="readonly", justify=CENTER, font=("th sarabun psk", 15), cursor="hand2")
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, command=self.search, text="ค้นหา", font=("th sarabun psk", 15), bg="lightgreen", cursor="hand2").place(x=430, y=7, width=140, height=30)

        # ==หัวข้อ== #
        title = Label(self.root, text="รายละเอียดสินค้า", font=("th sarabun psk", 15), bg="#ffa233", fg="white").place(x=50, y=100, width=1000)

        # ==ตาราง== #

        # ==แถว1== #
        lbl_productid = Label(self.root, text="รหัสสินค้า", font=("th sarabun psk", 15), bg="white").place(x=50, y=150)
        lbl_name = Label(self.root, text="ชื่อสินค้า", font=("th sarabun psk", 15), bg="white").place(x=350, y=150)
        lbl_quantity = Label(self.root, text="จำนวนสินค้าคงเหลือ", font=("th sarabun psk", 15), bg="white").place(x=750, y=150)

        txt_productid = Entry(self.root, textvariable=self.var_product_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=150, width=180)
        txt_name = Entry(self.root, textvariable=self.var_name_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=500, y=150, width=180)
        txt_quantity = Entry(self.root, textvariable=self.var_quantity_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=850, y=150, width=180)

        # ==แถว2== #
        lbl_price = Label(self.root, text="ราคา", font=("th sarabun psk", 15), bg="white").place(x=50, y=190)
        lbl_status = Label(self.root, text="สถานะสินค้า", font=("th sarabun psk", 15), bg="white").place(x=350, y=190)

        txt_price = Entry(self.root, textvariable=self.var_price_id, font=("th sarabun psk", 15), bg="lightyellow").place(x=150, y=190, width=180)
        txt_status = ttk.Combobox(self.root, textvariable=self.var_status_id, values=("พร้อมจำหน่าย", "ไม่พร้อมจำหน่าย"), font=("th sarabun psk", 15), state="readonly").place(x=500, y=190, width=180)

        # ==ปุ่ม== #
        btn_add = Button(self.root, text="บันทึก", command=self.add, font=("th sarabun psk", 15), bg="lightblue", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="อัพเดท", command=self.update, font=("th sarabun psk", 15), bg="lightgreen", cursor="hand2").place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="ลบ", command=self.delete, font=("th sarabun psk", 15), bg="red", cursor="hand2").place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="ล้าง", command=self.clear, font=("th sarabun psk", 15), bg="black", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)

        # ==ตารางสินค้า== #
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=150)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.ProductTable = ttk.Treeview(emp_frame, columns=("product_id", "name", "quantity", "price", "status"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("product_id", text="รหัสสินค้า")
        self.ProductTable.heading("name", text="ชื่อสินค้า")
        self.ProductTable.heading("quantity", text="จำนวนสินค้าคงเหลือ")
        self.ProductTable.heading("price", text="ราคา")
        self.ProductTable.heading("status", text="สถานะสินค้า")

        self.ProductTable["show"] = "headings"

        self.ProductTable.column("product_id", width=90)
        self.ProductTable.column("name", width=150)
        self.ProductTable.column("quantity", width=120)
        self.ProductTable.column("price", width=100)
        self.ProductTable.column("status", width=130)

        self.ProductTable.pack(fill=BOTH, expand=1)

        self.ProductTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()  # Show data in the table


    def add(self):
        con = sqlite3.connect(database='ims.db')  # เปลี่ยนเป็น ims.db
        cur = con.cursor()
        try:
            if self.var_product_id.get() == "":  # Check for product ID
                messagebox.showerror("Error", "จำเป็นต้องมีรหัสสินค้า", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE product_id=?", (self.var_product_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "มีรายการสินค้านี้แล้ว", parent=self.root)
                else:
                    cur.execute("INSERT INTO product (product_id, name, quantity, price, status) VALUES(?,?,?,?,?)", (
                        self.var_product_id.get(),
                        self.var_name_id.get(),
                        self.var_quantity_id.get(),
                        self.var_price_id.get(),
                        self.var_status_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "บันทึกสำเร็จ", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def show(self):
        con = sqlite3.connect(database='ims.db')  # เปลี่ยนเป็น ims.db
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for row in rows:
                self.ProductTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.ProductTable.focus()
        content = self.ProductTable.item(f)
        row = content['values']
        self.var_product_id.set(row[0])
        self.var_name_id.set(row[1])
        self.var_quantity_id.set(row[2])
        self.var_price_id.set(row[3])
        self.var_status_id.set(row[4])

    def search(self):
        con = sqlite3.connect(database='ims.db')  # เปลี่ยนเป็น ims.db
        cur = con.cursor()
        try:
            searchby = self.var_searchby_id.get()
            searchtxt = self.var_searchtxt_id.get()
            if searchtxt != "":
                cur.execute(f"SELECT * FROM product WHERE {searchby} LIKE ?", ('%' + searchtxt + '%',))
                rows = cur.fetchall()
                self.ProductTable.delete(*self.ProductTable.get_children())
                for row in rows:
                    self.ProductTable.insert('', END, values=row)
            else:
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def update(self):
        con = sqlite3.connect(database='ims.db')  # เปลี่ยนเป็น ims.db
        cur = con.cursor()
        try:
            if self.var_product_id.get() == "":
                messagebox.showerror("Error", "กรุณาเลือกข้อมูลที่จะอัพเดท", parent=self.root)
            else:
                cur.execute("UPDATE product SET name=?, quantity=?, price=?, status=? WHERE product_id=?", (
                    self.var_name_id.get(),
                    self.var_quantity_id.get(),
                    self.var_price_id.get(),
                    self.var_status_id.get(),
                    self.var_product_id.get()
                ))
                con.commit()
                messagebox.showinfo("Success", "อัพเดทข้อมูลเรียบร้อย", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        con = sqlite3.connect(database='ims.db')  # เปลี่ยนเป็น ims.db
        cur = con.cursor()
        try:
            if self.var_product_id.get() == "":
                messagebox.showerror("Error", "กรุณาเลือกข้อมูลที่จะลบ", parent=self.root)
            else:
                cur.execute("DELETE FROM product WHERE product_id=?", (self.var_product_id.get(),))
                con.commit()
                messagebox.showinfo("Success", "ลบข้อมูลเรียบร้อย", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_product_id.set("")
        self.var_name_id.set("")
        self.var_quantity_id.set("")
        self.var_price_id.set("")
        self.var_status_id.set("")
        self.var_searchby_id.set("เลือก")
        self.var_searchtxt_id.set("")
        self.show()

root = Tk()
obj = StockClass(root)
root.mainloop()
