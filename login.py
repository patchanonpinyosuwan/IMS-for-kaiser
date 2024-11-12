# login.py
import sqlite3
from tkinter import *  # pip install tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class LoginClass:
    def __init__(self, root):
        self.root = root
        self.root.title("บริษัท ไกเซอร์ เทเลมาร์ท จำกัด")
        self.root.geometry("400x400")
        
        # กำหนดตัวแปรสำหรับรหัสพนักงานและรหัสผ่าน
        self.employee_id = StringVar()
        self.password = StringVar()

        # เฟรมสำหรับล็อกอิน

        self.MenuLogo = Image.open("images/KSlogo.png")
        self.MenuLogo = self.MenuLogo.resize((100, 100), Image.LANCZOS)  # Resize the image to fit the label
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=50, y=50, height=300, width=300)

        # Logo at the top
        lbl_menuLogo = Label(Frame_login, image=self.MenuLogo, bg="white")  # Background set to white to match the frame
        lbl_menuLogo.pack(side=TOP, fill=X, pady=10)  # Add padding for better spacing

        # ชื่อและช่องกรอกข้อมูล

        lbl_user = Label(Frame_login, text="Username", font=("th sarabun psk", 15, "bold"), fg="gray", bg="white")
        lbl_user.place(x=30, y=90)
        txt_employee_id = Entry(Frame_login, textvariable=self.employee_id, font=("th sarabun psk", 15), bg="lightgray")
        txt_employee_id.place(x=30, y=120, width=240)

        lbl_pass = Label(Frame_login, text="Password", font=("th sarabun psk", 15, "bold"), fg="gray", bg="white")
        lbl_pass.place(x=30, y=160)
        txt_password = Entry(Frame_login, textvariable=self.password, font=("th sarabun psk", 15), bg="lightgray", show="*")
        txt_password.place(x=30, y=190, width=240)

        # ปุ่มล็อกอิน
        btn_login = Button(self.root, text="Login", command=self.login, font=("th sarabun psk", 15, "bold"), fg="white", bg="#d77337")
        btn_login.place(x=150, y=300, width=100, height=40)

    def login(self):
        # เชื่อมต่อกับฐานข้อมูล
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            # ตรวจสอบว่าช่องกรอกข้อมูลว่างหรือไม่
            if self.employee_id.get() == "" or self.password.get() == "":
                messagebox.showerror('Error', "กรุณากรอกข้อมูลให้ครบ", parent=self.root)
            else:
                # คำสั่ง SQL เพื่อตรวจสอบข้อมูลพนักงาน
                cur.execute("SELECT * FROM employee WHERE eid=? AND pass=?", (self.employee_id.get(), self.password.get()))
                user = cur.fetchone()
                
                # ตรวจสอบว่ามีผู้ใช้นี้อยู่หรือไม่
                if user is None:
                    messagebox.showerror('Error', "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง", parent=self.root)
                else:
                    messagebox.showinfo('Success', "เข้าสู่ระบบสำเร็จ", parent=self.root)
                    messagebox.showinfo('Success', f"ยินดีต้อนรับ {user[1]}", parent=self.root)
                    self.root.destroy()
                    
                    os.system("python index.py")
                    return user[1]  # คืนค่าชื่อพนักงานที่เข้าสู่ระบบ
                    
                 
        except Exception as ex:
            messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    app = LoginClass(root)
    root.mainloop()
