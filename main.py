from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False, False)

        self.bg=ImageTk.PhotoImage(file="images/uni.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=330, y=150, width=500, height=400) #frame

        title=Label(frame_login, text="Login Here", font=("Impact", 35, "bold"),fg="dark blue", bg="white").place(x=90, y=30)
        subtitle = Label(frame_login, text="Members Login Here", font=("Goudy old style", 15, "bold"), fg="black", bg="white").place(x=90,y=100)

        #username
        lbl_user = Label(frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90,y=140)
        self.username = Entry(frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)

        #password
        lbl_pswd = Label(frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white").place(x=90, y=210)
        self.pswd = Entry(frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.pswd.place(x=90, y=240, width=320, height=35)

        #button
        forget_btn = Button(frame_login, text="Forgot Password? ",cursor="hand2",bd=0, font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=90, y=280)
        submit_btn = Button(frame_login,command=self.check_func,cursor="hand2", text="Submit ", bd=0, font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=180, height=40)


    def check_func(self):
        if self.username.get()=="" or self.pswd.get()=="":
            messagebox.showerror("Error", "Cant be empty!",parent=self.root)

        elif self.username.get() != "Naina" or self.pswd.get() != "12345":
            messagebox.showerror("Error", "Invalid Username or Password!", parent=self.root)

        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")




root = Tk()
obj = Login(root)
root.mainloop()