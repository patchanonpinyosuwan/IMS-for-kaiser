from tkinter import *  # pip install tk
from PIL import Image, ImageTk  # pip install pillow
from employee import employeeClass  # นำเข้า employeeClass จากไฟล์ employee.py
from supplier import SupplierClass
from customer import customerClass
from Product import ProductClass
from login import LoginClass
import os
import sqlite3
from tkinter import messagebox
from datetime import datetime

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("บริษัท ไกเซอร์ เทเลมาร์ท จำกัด")
        self.root.config(bg="white")

        # ==หัวข้อ== #
        self.icon_title=PhotoImage(file="images/KSlogo.png")
        title = Label(self.root, text="บริษัท ไกเซอร์ เทเลมาร์ท จำกัด", font=("th sarabun psk ๙", 50, "bold"), bg="#ffa233", fg="white")
        title.place(x=0, y=0, relwidth=1)

        # ==เวลา== #
        self.lbl_clock = Label(self.root, text="ยินดีต้อนรับ \t\t วันที่: DD-MM-YYYY เวลา: HH:MM:SS", font=("th sarabun psk ๙", 10), bg="#4d536d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_time()
   

        # ==เมนูด้านซ้าย== #
        self.MenuLogo=Image.open("images/KSlogo.png")
        self.MenuLogo = self.MenuLogo.resize((200,200), Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        
        
        Label(LeftMenu, text="เมนู", font=("th sarabun psk ๙", 20, "bold"), bg="#ffa233").pack(side=TOP, fill=X)

        # ==ปุ่มเปิดหน้าต่างใหม่== #
        btn_employee = Button(LeftMenu, text="พนักงาน", font=("th sarabun psk ๙", 20, "bold"), bg="#f1f1f1", command=self.employee ,cursor="hand2")
        btn_employee.pack(side=TOP, fill=X)

        btn_supplier = Button(LeftMenu, text="ผู้จัดจำหน่าย", font=("th sarabun psk ๙", 20, "bold"), bg="#f1f1f1", command=self.supplier ,cursor="hand2")
        btn_supplier.pack(side=TOP, fill=X)

        btn_customer = Button(LeftMenu, text="ลูกค้า", font=("th sarabun psk ๙", 20, "bold"), bg="#f1f1f1", command=self.customer ,cursor="hand2") 
        btn_customer.pack(side=TOP, fill=X)

        btn_Product = Button(LeftMenu, text="สินค้า", font=("th sarabun psk ๙", 20, "bold"), bg="#f1f1f1", command=self.Product ,cursor="hand2")
        btn_Product.pack(side=TOP, fill=X)

        btn_logout = Button(LeftMenu, text="ออกจากระบบ", font=("th sarabun psk ๙", 20, "bold"), bg="#f1f1f1", command=self.login, cursor="hand2")
        btn_logout.pack(side=TOP, fill=X)

         #==contnet==#

        self.lbl_Product=Label(self.root,text="คลังรวม\n[0]",bg="#ff5900",fg="white",font=("th sarabun psk ๙",20,"bold"))
        self.lbl_Product.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier=Label(self.root,text="ผู้จัดจำหน่าย\n[0]",bg="#ff5900",fg="white",font=("th sarabun psk ๙",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_customer=Label(self.root,text="จำนวนลูกค้า\n[0]",bg="#ff5900",fg="white",font=("th sarabun psk ๙",20,"bold"))
        self.lbl_customer.place(x=1000,y=120,height=150,width=300)

        self.lbl_employee=Label(self.root,text="จำนวนพนักงาน\n[0]",bg="#ff5900",fg="white",font=("th sarabun psk ๙",20,"bold"))
        self.lbl_employee.place(x=300,y=300,height=150,width=300)

        # ==ส่วนท้าย== #
        lbl_footer = Label(self.root, text="บริษัท ไกเซอร์ เทเลมาร์ท โปรแกรมโดย ภัทรชนน ภิญโญสุวรรณ", font=("th sarabun psk ๙", 10), bg="white")
        lbl_footer.place(x=0, y=670, relwidth=1)

        self.update_content()

    # ฟังก์ชัน employee สำหรับเปิดหน้าต่างใหม่
    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)
    
    def supplier(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = SupplierClass(self.new_win)

    def customer(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = customerClass(self.new_win)

    def Product(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = ProductClass(self.new_win)

    def update_time(self):
        # ดึงวันที่และเวลาปัจจุบัน
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        # อัปเดตข้อความใน lbl_clock พร้อมชื่อพนักงานที่ต้อนรับ
        self.lbl_clock.config(text=f"ยินดีต้อนรับ \t\t วันที่: {current_time}")
        
        # ตั้งค่าให้อัปเดตทุก 1 วินาที (1000 มิลลิวินาที)
        self.root.after(1000, self.update_time)

    def update_content(self):
        con = sqlite3.connect(database='ims.db')
        cur = con.cursor()
        try:

            cur.execute("select * from Product")
            Product=cur.fetchall()
            self.lbl_Product.config(text=f'คลังรวม\n[ {str(len(Product))} ]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'ผู้จัดจำหน่าย\n[ {str(len(supplier))} ]')

            cur.execute("select * from customer")
            customer=cur.fetchall()
            self.lbl_customer.config(text=f'จำนวนลูกค้า\n[ {str(len(customer))} ]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'จำนวนพนักงาน\n[ {str(len(employee))} ]')

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
 

    def login(self):
        self.new_win = Toplevel(self.root) 
        self.new_obj = LoginClass(self.new_win)
        self.root.destroy()
        os.system("python login.py")

    

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()