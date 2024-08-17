#login.py
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from main_window import Face_recog

window = tk.Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
# window.state('zoomed')
window.geometry("1440x850+0+0")
window.resizable(0,0)
window.title('Login Page')


# Window Icon Photo
icon = ImageTk.PhotoImage(file='images\\pic-icon.png')
window.iconphoto(True, icon)

LoginPage = tk.Frame(window)
RegistrationPage = tk.Frame(window)

for frame in (LoginPage, RegistrationPage):
    frame.grid(row=0, column=0, sticky='nsew')

background_frame = tk.Frame(LoginPage, bg='#1e85d0')
background_frame.place(relx=0, rely=0, relwidth=1, relheight=1)


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)

design_frame1 = tk.Listbox(LoginPage, bg='#0c71b9', width=119, height=70, highlightthickness=0, borderwidth=0)
design_frame1.place(x=0, y=0)

design_frame2 = tk.Listbox(LoginPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame2.place(x=716, y=0)

design_frame3 = tk.Listbox(LoginPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=110, y=106)

design_frame4 = tk.Listbox(LoginPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=716, y=106)

# ====== Email ====================
email_entry = tk.Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry.place(x=174, y=170, width=256, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = tk.Label(design_frame4, text='• Username', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=170, y=140)

# ==== Password ==================
password_entry1 = tk.Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
password_entry1.place(x=174, y=250, width=256, height=34)
password_entry1.config(highlightbackground="black", highlightcolor="black")
password_label = tk.Label(design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
password_label.place(x=170, y=220)


# function for show and hide password
def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')


def mw():
    new_window = tk.Toplevel()
    # new_window.geometry("1400x900")  # Adjust the size according to your screen resolution
    app = Face_recog(new_window)
    # window.destroy()


def login_bt():
    if email_entry.get() == "MHSSCE" and password_entry1.get() == "mhssce@123":
        mw()

    else:
        messagebox.showerror("Access Denied", "Incorrect username or password")


# ====== checkbutton ==============
checkButton = tk.Checkbutton(design_frame4, bg='#f8f8f8', command=password_command, text='show password')
checkButton.place(x=170, y=288)


# ===== Welcome Label ==============
welcome_label = tk.Label(design_frame4, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=210, y=15)

# ======= top Login Button =========
login_button = tk.Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                         borderwidth=0, activebackground='#1b87d2', cursor='hand2')
login_button.place(x=845, y=175)

login_line = tk.Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
login_line.place(x=840, y=203)

# ==== LOGIN  down button ============
loginBtn1 = tk.Button(design_frame4, fg='#f8f8f8', text='Login', command=login_bt, bg='#1b87d2',font=("yu gothic ui bold", 15), cursor='hand2', activebackground='#1b87d2')
loginBtn1.place(x=173, y=340, width=256, height=50)

# ======= ICONS =================

# ===== Email icon =========
email_icon = Image.open('images\\email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = tk.Label(design_frame4, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=135, y=174)

# ===== password icon =========
password_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = tk.Label(design_frame4, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=135, y=254)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = tk.Label(design_frame4, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=340, y=5)

# ===== Left Side Picture ============
side_image = Image.open('images\\vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = tk.Label(design_frame3, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=50, y=10)

window.mainloop()
