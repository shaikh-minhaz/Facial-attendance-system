import tkinter as tk
from PIL import Image, ImageTk
from student_details import student
from FCAS import Fcas
from attendance import Attendance

class AnimatedBackground(tk.Label):
    def __init__(self, master, gif_path):
        super().__init__(master)
        self.master = master
        self.gif_path = gif_path
        self.delay = 100  # Delay between frames in milliseconds
        self.frames = []
        self.idx = 0
        self.load_frames()
        self.animate()

    def load_frames(self):
        gif = Image.open(self.gif_path)
        try:
            while True:
                frame = ImageTk.PhotoImage(gif)
                self.frames.append(frame)
                gif.seek(len(self.frames))
        except EOFError:
            gif.seek(0)

    def animate(self):
        self.idx %= len(self.frames)
        self.config(image=self.frames[self.idx])
        self.idx += 1
        self.master.after(self.delay, self.animate)

    def add_image(self, image_path, x, y, text, command=None):
        img = Image.open(image_path)
        img = img.resize((200, 200), Image.BICUBIC)
        photo_img = ImageTk.PhotoImage(img)
        label = tk.Label(self.master, image=photo_img)
        label.image = photo_img
        label.place(x=x, y=y)

        button = tk.Button(self.master, text=text, font=("calibri", 15, "bold"), bg="darkblue", fg="white", cursor="hand2", command=command)
        button.place(x=x, y=y+200, width=205)




class Face_recog:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1440x900+0+0")
        self.root.title("FACIAL RECOGNITION ATTENDANCE SYSTEM")
        self.show_animated_background()
        self.add_buttons_and_labels()

    def show_animated_background(self):
        gif_path = r"C:\Users\Macbook Air\Anti Spoofing\imgs\fc2.gif"
        self.animated_bg = AnimatedBackground(self.root, gif_path)
        self.animated_bg.place(x=0, y=0, relwidth=1, relheight=1)

    def add_buttons_and_labels(self):
        # Student Details Button
        self.animated_bg.add_image(r"C:\Users\Macbook Air\Anti Spoofing\imgs\stu.png", x=200, y=300, text="Student Details", command=self.student_details)

        # Take Attendance Button
        self.animated_bg.add_image(r"C:\Users\Macbook Air\Anti Spoofing\imgs\fc1.png", x=610, y=300, text="Take Attendance", command=self.face_r)

        # View Attendance Button
        self.animated_bg.add_image(r"C:\Users\Macbook Air\Anti Spoofing\imgs\ar.png", x=1040, y=300, text="View Attendance",command=self.atten)


        # Title
        heading = tk.Label(self.root, text="Facial Recognition Attendance System", font=("Exotc350 DmBd BT", 35, "bold"), bg="black", fg="white")
        heading.place(relx=0.5, rely=0.09, anchor="center")

    def student_details(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = student(self.new_window)

    def face_r(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = Fcas(self.new_window)

    def atten(self):
        self.new_window = tk.Toplevel(self.root)
        self.app = Attendance(self.new_window)

def main():
    root = tk.Tk()
    app = Face_recog(root)
    root.mainloop()

if __name__ == "__main__":
    main()
